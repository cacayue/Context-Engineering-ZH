"""Add book outlines and portable cross-volume PDF annotations, then verify them."""
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
import re
import subprocess
from tempfile import TemporaryDirectory
from urllib.parse import urlsplit

from pypdf import PdfReader, PdfWriter
from pypdf.generic import ArrayObject, BooleanObject, DictionaryObject, NameObject, NumberObject, TextStringObject

from .layout import MARKER, MODULES

def print_pdf(html, pdf):
    with TemporaryDirectory(prefix="ce-print-") as profile:
        args = ["google-chrome", "--headless", "--disable-background-networking", "--disable-extensions",
                "--no-first-run", "--no-pdf-header-footer", f"--user-data-dir={profile}",
                f"--print-to-pdf={pdf}", html.as_uri()]
        result = subprocess.run(args, capture_output=True, text=True, timeout=240)
    if result.returncode or not pdf.is_file():
        raise ValueError(f"Chrome 未生成 {html.name} 的 PDF：{result.stderr[-2000:]}")

def destination_index(reader):
    return {name.lstrip("/"): (reader.get_destination_page_number(target), target)
            for name, target in reader.named_destinations.items()}


def write_volume(vol, raw, output, destinations, printed):
    number = vol["volume"]
    name = f"{number:02}"
    writer = PdfWriter(clone_from=str(raw))
    here = destinations[number]
    writer.add_outline_item(title="封面", page_number=0)
    writer.add_outline_item(title="本册目录", page_number=here["contents"][0])
    mod = None
    last_page = here["contents"][0]
    chapter_locations = []
    for chapter in vol["chapters"]:
        page = here[chapter["id"]][0]
        assert page > last_page, (name, chapter, page, last_page)
        last_page = page
        chapter_locations.append(dict(chapter, page=page + 1))
        if chapter["module"] != mod:
            mod = chapter["module"]
            parent = writer.add_outline_item(title=MODULES[mod], page_number=page, is_open=False)
        writer.add_outline_item(title=chapter["title"], page_number=page, parent=parent)
    writer.add_outline_item(title="版本与许可", page_number=here["imprint"][0])
    assert printed == {item["id"]: item["page"] for item in chapter_locations}, name
    writer.add_metadata({"/Author": "davidkimai / Context-Engineering-ZH",
                         "/Subject": "Context Engineering 中文阅读版",
                         "/Keywords": "上下文工程, Context Engineering"})
    links = Counter()
    downgraded = set()
    for page in writer.pages:
        for ref in page.get("/Annots", ()):
            annotation = ref.get_object()
            if "/Dest" in annotation:
                dest = annotation["/Dest"]
                if isinstance(dest, str):
                    assert dest.lstrip("/") in here, (name, dest)
                links["same_volume"] += 1
            action = annotation.get("/A")
            if not action:
                continue
            action = action.get_object()
            uri = str(action.get("/URI", ""))
            if not uri.startswith(MARKER):
                if uri:
                    assert not uri.lower().startswith("file:"), (name, uri)
                    links["external"] += 1
                continue
            url = urlsplit(uri)
            filename, dest = url.path.lstrip("/"), url.fragment
            target = destinations[int(filename.removesuffix(".pdf"))]
            if dest not in target:
                downgraded.add((filename, dest))
                dest = dest.split("a", 1)[0]
            page_no, dest_obj = target[dest]
            array = ArrayObject([NumberObject(page_no), *dest_obj.dest_array[1:]])
            annotation[NameObject("/A")] = DictionaryObject({
                NameObject("/S"): NameObject("/GoToR"),
                NameObject("/F"): TextStringObject(filename),
                NameObject("/D"): array,
                NameObject("/NewWindow"): BooleanObject(True),
            })
            links["cross_volume"] += 1
    writer.write(output)
    # Reopen the actual handoff artifact, not the Chromium intermediate.
    result = PdfReader(output)
    count = len(result.pages)
    assert count == len(writer.pages)
    assert len(result.outline) >= 5 and sum(len(x) for x in result.outline if isinstance(x, list)) == len(chapter_locations)
    assert len(result.named_destinations) == len(here)
    cross_checked = 0
    landscape = 0
    for page in result.pages:
        landscape += page.mediabox.width > page.mediabox.height
        for ref in page.get("/Annots", ()):
            note = ref.get_object()
            action = note.get("/A", {})
            assert not str(action.get("/URI", "")).startswith(MARKER)
            if action.get("/S") == "/GoToR":
                target = int(action["/F"].removesuffix(".pdf"))
                assert 0 <= action["/D"][0] <= max(page for page, _ in destinations[target].values())
                cross_checked += 1
    assert cross_checked == links["cross_volume"]
    print(f"第 {name} 册：{count} 页，{len(chapter_locations)} 个篇首书签，{cross_checked} 个跨册跳转。", flush=True)
    return dict(vol, chapters=chapter_locations, pages=count, landscape=landscape,
                links=dict(links), downgraded=sorted(downgraded), bytes=output.stat().st_size)


def fill_folios(vol, src, raw):
    name = f"{vol['volume']:02}"
    positions = destination_index(PdfReader(raw))
    pages = {c["id"]: positions[c["id"]][0] + 1 for c in vol["chapters"]}
    markup, count = re.subn(r'(<small class="entry-page" data-for="(d\d+)">)\d*(</small>)',
                            lambda m: f"{m[1]}{pages[m[2]]}{m[3]}", src.read_text())
    assert count == len(pages), (name, count, len(pages))
    src.write_text(markup)
    return pages


def build_volumes(report, work, output):
    vols = report["volumes"]
    html = [work / f"{v['volume']:02}.html" for v in vols]
    raw = [p.with_suffix(".pdf") for p in html]
    with ThreadPoolExecutor(max_workers=2) as pool:
        list(pool.map(print_pdf, html, raw))
        printed = [fill_folios(v, page, pdf) for v, page, pdf in zip(vols, html, raw)]
        # Remove only the temporary first pass, so a missing second pass is visible.
        for pdf in raw:
            pdf.unlink()
        list(pool.map(print_pdf, html, raw))
    positions = {v["volume"]: destination_index(PdfReader(pdf)) for v, pdf in zip(vols, raw)}
    return [write_volume(v, pdf, output / pdf.name, positions, folios)
            for v, pdf, folios in zip(vols, raw, printed)]
