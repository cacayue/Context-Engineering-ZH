"""Make a single reading copy from the six verified PDFs."""
from collections import Counter
from html import escape
from itertools import accumulate

from pypdf import PdfReader, PdfWriter
from pypdf.generic import ArrayObject, DictionaryObject, NameObject, TextStringObject

from .layout import MODULES
from .volumes import destination_index, print_pdf

COMPLETE = "Context-Engineering-ZH-Complete.pdf"
MARKER = "https://ce-combined.invalid/"

def build_combined(vols, work, out):
    readers = [PdfReader(out / f"{v['volume']:02}.pdf") for v in vols]
    assert [len(r.pages) for r in readers] == [v["pages"] for v in vols]
    base = list(accumulate((len(r.pages) for r in readers), initial=1))
    count = sum(v["count"] for v in vols)
    locs = [destination_index(r) for r in readers]
    toc_rows = "".join(
        f"""<a href="{MARKER}{i}" class="row">
            <span class="num">{i:02}</span><strong>{escape(v["title"])}</strong>
            <span class="amount">{v["count"]} 篇</span><span class="pg">{base[i-1]+locs[i-1]["contents"][0]+1:,}</span>
        </a>"""
        for i, v in enumerate(vols, 1)
    )
    front = work / "front.html"
    front.write_text(f"""<!doctype html><html lang="zh-CN"><meta charset="utf-8">
    <title>上下文工程 · 中文合订本</title>
    <style>
    @page {{ size: A4; margin: 19mm 20mm; }}
    * {{box-sizing:border-box}}
    body {{margin:0;color:#172b33;font:11pt/1.65 "Noto Sans CJK SC",sans-serif;print-color-adjust:exact}}
    header {{border-top:3pt solid #145951;padding-top:5mm}}
    .kicker {{font-size:9pt;color:#145951;letter-spacing:.16em}}
    h1 {{font:700 46pt/1.25 "Noto Serif CJK SC",serif;letter-spacing:-.05em;margin:12mm 0 1.8mm}}
    .en {{font:10pt "Noto Sans CJK SC";letter-spacing:.20em;color:#53656a}}
    .summary {{margin:7mm 0 11mm;color:#436366}}
    .main {{border-top:.6pt solid #b7c9c1;padding-top:4mm}}
    h2 {{margin:0;font-size:18pt}}
    .row {{display:grid;grid-template-columns:13mm minmax(0,1fr) 18mm 20mm;align-items:baseline;gap:2mm;
           border-bottom:.55pt solid #d1dcd9;text-decoration:none;color:#172b33;padding:3mm 1mm}}
    .row:nth-of-type(even) {{background:#f1f5f2}}
    .row strong {{font-weight:600}}
    .row .num {{font-size:9pt;color:#145951}}
    .row .amount,.pg {{font-size:9pt;color:#53656a;text-align:right;font-variant-numeric:tabular-nums}}
    .legend {{font-size:9pt;color:#53656a;margin:1mm 0 4mm}}
    footer {{font-size:9pt;color:#53656a;margin-top:8mm}}
    </style>
    <header><div class="kicker">中文阅读版　/　六册合订</div>
    <h1>上下文工程</h1><div class="en">CONTEXT ENGINEERING</div>
    <p class="summary">{count} 篇 · {base[-1]:,} 页 · 附阅读路径和术语表</p></header>
    <main class="main"><h2>总目录</h2>
    <p class="legend">点击册名进入该册目录。右栏是合订本页码，正文保留原分册页码。</p>
    {toc_rows}</main><footer>原作者 davidkimai　/　中文译本 Context-Engineering-ZH　/　MIT License</footer>
    </html>""")
    print_pdf(front, work / "front.pdf")
    front_pdf = PdfReader(work / "front.pdf")
    assert len(front_pdf.pages) == 1

    writer = PdfWriter()
    writer.root_object[NameObject("/Lang")] = TextStringObject("zh-CN")
    inputs = [front_pdf, *readers]
    for reader in inputs:
        for page in reader.pages:
            writer.add_page(page, excluded_keys=["/Annots", "/StructParents"])
    writer.add_metadata({"/Title": "上下文工程 · 中文合订本", "/Author": "davidkimai / Context-Engineering-ZH",
                         "/Subject": "Context Engineering 中文阅读版 · 六册合订"})
    writer.add_outline_item(title="总目录", page_number=0)
    expected_bookmarks = []
    for i, (v, index) in enumerate(zip(vols, locs)):
        offset = base[i]
        volmark = writer.add_outline_item(title=f"第 {i+1:02} 册 · {v['title']}", page_number=offset, is_open=False)
        writer.add_outline_item(title="本册目录", page_number=offset + index["contents"][0], parent=volmark)
        module = None
        for chapter in v["chapters"]:
            pg = offset + chapter["page"] - 1
            assert pg == offset + index[chapter["id"]][0]
            if chapter["module"] != module:
                module = chapter["module"]
                group = writer.add_outline_item(title=MODULES[module], page_number=pg, parent=volmark, is_open=False)
            writer.add_outline_item(title=chapter["title"], page_number=pg, parent=group)
            expected_bookmarks.append((chapter["title"], pg))
        writer.add_outline_item(title="版本与许可", page_number=offset + index["imprint"][0], parent=volmark)

    expected = Counter()
    for ri, reader in enumerate(inputs):
        start = 0 if ri == 0 else base[ri-1]
        for j, page in enumerate(reader.pages, start):
            for ref in page.get("/Annots", ()):
                obj = ref.get_object()
                assert obj["/Subtype"] == "/Link"
                # Every link is rebuilt against the merged page references.
                keep = {k: obj[k].clone(writer) for k in map(NameObject, ("/Type", "/Subtype", "/F", "/Border", "/Rect")) if k in obj}
                action = obj.get("/A", {})
                uri = str(action.get("/URI", ""))
                if ri == 0:
                    vi = int(uri.removeprefix(MARKER)) - 1
                    pg, d = locs[vi]["contents"]
                    fit = d.dest_array[1:]
                    target = base[vi] + pg
                elif action.get("/S") == "/GoToR":
                    vi = int(action["/F"].removesuffix(".pdf")) - 1
                    fit = action["/D"][1:]
                    target = base[vi] + int(action["/D"][0])
                elif "/Dest" in obj:
                    pg, d = locs[ri-1][str(obj["/Dest"]).lstrip("/")]
                    fit = d.dest_array[1:]
                    target = start + pg
                else:
                    assert action.get("/S") == "/URI" and uri
                    keep[NameObject("/A")] = action.clone(writer)
                    writer.add_annotation(page_number=j, annotation=DictionaryObject(keep))
                    expected[(j, uri)] += 1
                    continue
                keep[NameObject("/Dest")] = ArrayObject([writer.pages[target].indirect_reference, *fit])
                writer.add_annotation(page_number=j, annotation=DictionaryObject(keep))
                expected[(j, target)] += 1

    target_file = out / COMPLETE
    writer.write(target_file)
    proof = PdfReader(target_file)
    assert len(proof.pages) == base[-1]
    page_by_ref = {p.indirect_reference.idnum: i for i, p in enumerate(proof.pages)}
    actual = Counter()
    for j, page in enumerate(proof.pages):
        for ref in page.get("/Annots", ()):
            a = ref.get_object()
            if "/Dest" in a:
                actual[(j, page_by_ref[a["/Dest"][0].idnum])] += 1
            else:
                assert a["/A"]["/S"] == "/URI"
                actual[(j, str(a["/A"]["/URI"]))] += 1
    assert actual == expected
    assert sum(c for (_, k), c in actual.items() if isinstance(k, int)) == 6 + sum(
        v["links"]["same_volume"] + v["links"]["cross_volume"] for v in vols
    )
    assert len(proof.outline) == 1 + 2 * len(vols)
    all_c = []
    for main in proof.outline:
        if isinstance(main, list):
            for group in main:
                if isinstance(group, list):
                    all_c.extend((ch.title, proof.get_destination_page_number(ch)) for ch in group)
    assert all_c == expected_bookmarks
    links = sum(c for (_, k), c in actual.items() if isinstance(k, int))
    print(f"合订本：{len(proof.pages):,} 页，{len(all_c)} 个篇首书签，{links} 个文件内跳转。", flush=True)
    return len(proof.pages), links
