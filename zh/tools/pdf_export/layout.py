"""Export the repository's Chinese reading path. Python + lxml, Pandoc, Chrome."""
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from html import escape
import json
from pathlib import Path, PurePosixPath
import posixpath
import re
import subprocess
import unicodedata
from urllib.parse import quote, unquote, urlsplit

from lxml import etree, html

HERE = Path(__file__).resolve().parent
VOLUMES = [
    ("入口与概念地基", "导读", "从第一个提示词出发，建立理解上下文的共同语言。", ["M1", "M2"]),
    ("课程基础与进阶", "课程", "把上下文检索、处理、管理与记忆组成可运行的系统。", ["M3", "M4"]),
    ("工程资产与认知架构", "工程", "从提示词模板到协议，再到可复用的认知工具与架构。", ["M6", "M9"]),
    ("前沿课程与参考手册", "前沿", "进入多智能体、场论与评估，并保留可随时翻查的技术参考。", ["M5", "M7"]),
    ("无代码实践", "实践", "不依赖编程环境，从示例和练习入手设计上下文。", ["M8"]),
    ("研究与扩展", "研究", "追溯论据、术语和研究边界，找到可继续探索的方向。", ["M10", "M11"]),
]
MODULES = dict(zip(
    (f"M{i}" for i in range(12)),
    ("阅读导航", "入口层", "概念地基", "课程基础", "课程进阶", "课程前沿",
     "工程资产", "参考手册", "无代码", "认知架构", "研究篇", "扩展导读"),
))
HOSTS = {"github.com", "deepwiki.com", "img.shields.io", "raw.githubusercontent.com", "avatars.githubusercontent.com", "i.ytimg.com", "api.star-history.com"}
MARKER = "https://ce-edition.invalid/"
BOX = re.compile(r"[┌┐└┘┬┴┼├┤│╔╗╚╝╭╮╯╰║─═]")
HEAD = re.compile(r"h[1-6]\Z")
ORIGIN = "https://github.com/cacayue/Context-Engineering-ZH"
# The source/translation H2 sequences of these articles were compared against each other.
LEGACY_FRAGMENT_ARTICLES = {
    "00_COURSE/01_context_retrieval_generation/case_studies/domain_specific_prompting.md",
    "00_COURSE/01_context_retrieval_generation/case_studies/retrieval_optimization.md",
    "cognitive-tools/cognitive-schemas/user-schemas.md",
}
PATH_CORRECTIONS = {
    "zh/00_COURSE/05_memory_systems/03_reconstructive_memory.md": "zh/00_COURSE/05_memory_systems/04_reconstructive_memory.md",
    "zh/00_COURSE/08_field_integration": "zh/00_COURSE/08_field_theory_integration",
    "zh/20_templates/resonance_measurement.py": "20_templates/field_resonance_measure.py",
}


def run(args, **kw):
    return subprocess.run(args, check=True, **kw)


def pathkey(entry):
    path = entry["target"]
    if entry["module"] == "M1":
        if path == "zh/README.md":
            return -3, ()
        if path.startswith("zh/masterclass_content/"):
            return -2, tuple(PurePosixPath(path).parts)
        if path == "zh/Complete_Guide.md":
            return -1, ()
    return 0, tuple((part != "README.md", part.casefold()) for part in PurePosixPath(path).parts)


def read_chapter(job):
    root, entry = job
    source = root / entry["target"]
    result = run(["pandoc", "-f", "gfm+tex_math_dollars+attributes", "-t", "html5", "--mathml",
                  "--no-highlight", "--wrap=none", str(source)], capture_output=True)
    doc = html.fragment_fromstring(result.stdout.decode(), create_parent="div")
    for node in doc.xpath(".//script|.//style|.//iframe|.//object|.//embed|.//link|.//base|.//form"):
        node.drop_tree()
    for node in doc.xpath(".//details"):
        node.set("open", "open")
    first = next(iter(doc.xpath(".//h1")), None)
    zh_h2 = doc.xpath(".//h2/@id")
    source_name = entry["target"].removeprefix("zh/")
    fm = source.read_text(encoding="utf-8").split("\n---\n", 1)[0]
    title = first.text_content() if first is not None else next(
        (ln[7:].strip().strip("\"'") for ln in fm.splitlines() if ln.startswith("title: ")), source.stem
    )
    entry["title"] = " ".join(title.split()) or source.stem
    anchors = {}
    for j, node in enumerate(doc.xpath(".//*[@id] | .//a[@name]"), 1):
        dest = entry["id"] if node is first else f"{entry['id']}a{j}"
        for key in ("id", "name"):
            if node.get(key):
                anchors.setdefault(node.get(key), dest)
        node.attrib.pop("name", None)
        node.set("id", dest)
    if first is not None:
        if first.xpath(".//a[@href] | .//img"):
            first.tag = "p"
            first.attrib.pop("id", None)
        else:
            first.drop_tree()
    for node in doc.iter():
        if not isinstance(node.tag, str):
            continue
        if HEAD.fullmatch(node.tag):
            node.tag = "h" + str(min(6, int(node.tag[1]) + 1))
        for attr in tuple(node.attrib):
            if attr.lower().startswith("on") or attr == "srcset":
                del node.attrib[attr]
    if source_name in LEGACY_FRAGMENT_ARTICLES:
        english = run(["pandoc", "-f", "gfm+tex_math_dollars+attributes", "-t", "html5",
                       "--no-highlight", "--wrap=none", str(root / source_name)], capture_output=True).stdout
        en_h2 = html.fragment_fromstring(english.decode(), create_parent="div").xpath(".//h2/@id")
        assert len(en_h2) == len(zh_h2), source_name
        for src_id, zh_id in zip(en_h2, zh_h2):
            anchors.setdefault(src_id, anchors[zh_id])
    entry["anchors"] = anchors
    return doc, result.stderr.decode()


def draw_width(line):
    return sum(0 if unicodedata.combining(c) else
               2 if unicodedata.east_asian_width(c) in "FW" else 1 for c in line.expandtabs(4))


def decorate_pre(node):
    raw = node.text_content().rstrip("\n")
    lines = raw.splitlines()
    if sum(len(BOX.findall(line)) >= 2 for line in lines) < 2 or any(len(line) > 260 for line in lines):
        return None
    width = max(map(draw_width, lines))
    wide = width > 142 and not node.xpath("ancestor::td|ancestor::th|ancestor::li|ancestor::blockquote")
    size = min(8.4, (1370 if wide else 888) / max(1, width))
    if not wide and node.xpath("ancestor::td|ancestor::th"):
        return None
    node.set("class", " ".join(filter(None, [node.get("class"), "diagram", "wide" if wide else ""])))
    node.set("style", f"font-size:{size:.2f}pt")


def fetch_asset(url, work, number):
    parts = urlsplit(url)
    if parts.scheme not in {"http", "https"} or parts.hostname not in HOSTS or parts.username or parts.password:
        return None
    filename = work / "assets" / f"{number:03}"
    filename.parent.mkdir(exist_ok=True)
    fetch = subprocess.run(["curl", "-fLsS", "-A", "Mozilla/5.0", "--connect-timeout", "5", "--max-time", "15",
                            "--max-filesize", "16000000", "--proto", "=https", "--proto-redir", "=https",
                            "-w", "%{content_type}", "-o", str(filename), url], capture_output=True, text=True)
    suffix = {"image/png": ".png", "image/jpeg": ".jpg", "image/svg+xml": ".svg", "image/webp": ".webp",
              "image/gif": ".gif", "image/avif": ".avif"}.get(fetch.stdout.split(";")[0])
    if fetch.returncode or not suffix:
        return None
    target = filename.with_suffix(suffix)
    filename.rename(target)
    return target.as_uri()


def prepare(root):
    manifest = json.loads((root / "zh/manifest.json").read_text())
    original = manifest["files"]
    if len({e["target"] for e in original}) != len(original) or len(original) != manifest["totals"]["files"]:
        raise ValueError("manifest 文件数或译文路径重复")
    incomplete = [e["target"] for e in original
                  if e["status"] not in ("published", "authored")
                  or sorted(e["chunks_done"]) != list(range(1, e["chunks"] + 1))]
    if incomplete:
        raise ValueError("manifest 中尚未完成：" + "、".join(incomplete))
    extras = [{"target": p, "module": "M0", "task": "M0-03"} for p in ("zh/LEARNING_PATH.md", "zh/GLOSSARY.md")]
    ordered = []
    for vol, (_, _, _, modlist) in enumerate(VOLUMES, 1):
        if vol == 1:
            ordered.extend(dict(entry, volume=vol) for entry in extras)
        for mod in modlist:
            group = list(filter(lambda f: f["module"] == mod, original))
            ordered.extend(dict(entry, volume=vol) for entry in sorted(group, key=pathkey))
    if {e["target"] for e in ordered if e["module"] != "M0"} != {e["target"] for e in original}:
        raise ValueError("manifest 有未编入阅读路径的模块，请先更新分册映射")
    for i, entry in enumerate(ordered, 1):
        entry["id"] = f"d{i:03}"
    for entry in ordered:
        path = (root / entry["target"]).resolve()
        if not path.is_relative_to(root / "zh") or not path.is_file():
            raise ValueError(f"译文不可读或不在 zh/ 目录：{entry['target']}")
    return ordered


def render(root, work, commit, dirty):
    entries = prepare(root)
    by_path = {entry["target"]: entry for entry in entries}
    assert len(by_path) == len(entries)
    edition = commit[:7] + ("（含本地修改）" if dirty else "")
    license_text = (root / "LICENSE").read_text()
    web = f"{ORIGIN}/blob/{commit}/"
    stats = Counter()
    unresolved = []
    warnings = []
    assets = {}
    with ThreadPoolExecutor(max_workers=4) as pool:
        docs = list(pool.map(read_chapter, ((root, e) for e in entries)))
    for entry, (doc, err) in zip(entries, docs):
        path, vol = entry["target"], entry["volume"]
        if err:
            warnings.append((path, err))
        for node in doc.xpath(".//a[@href]"):
            raw = node.get("href").strip()
            try:
                url = urlsplit(raw)
            except ValueError:
                unresolved.append((vol, path, raw, "无效 URL"))
                node.attrib.pop("href", None)
                continue
            if url.scheme or url.netloc:
                if url.scheme and url.scheme not in {"https", "http", "mailto"}:
                    node.attrib.pop("href", None)
                    unresolved.append((vol, path, raw, "非出版链接协议"))
                continue
            f = unquote(url.path)
            target = posixpath.normpath(posixpath.join(posixpath.dirname(path), f)) if f else path
            if f.startswith("/"):
                target = f.lstrip("/")
            target = PATH_CORRECTIONS.get(target, target)
            dst = by_path.get(target) or by_path.get(posixpath.join(target, "README.md"))
            anchor = unquote(url.fragment)
            if dst:
                dest = dst["anchors"].get(anchor, "") if anchor else dst["id"]
                if not dest:
                    if path == dst["target"]:
                        node.tag = "span"
                        del node.attrib["href"]
                        node.set("class", "inactive-link")
                        unresolved.append((vol, path, raw, "原文目录无此节，保留条目"))
                        continue
                    dest = dst["id"]
                    unresolved.append((vol, path, raw, "未匹配节锚点，已跳篇首"))
                if dst["volume"] == vol:
                    new = f"#{dest}"
                    stats["within"] += 1
                else:
                    new = f"{MARKER}{dst['volume']:02}.pdf#{dest}"
                    stats["between"] += 1
            else:
                # Keep original-text links online; published files outside the book are not local dependencies.
                if target.startswith("zh/") and not (root / target).exists() and (root / target[3:]).exists():
                    target = target[3:]
                exists = not target.startswith("../") and (root / target).exists()
                if not exists:
                    unresolved.append((vol, path, raw, "仓库路径不存在，保留网页地址"))
                endpoint = web if not (root / target).is_dir() else web.replace("/blob/", "/tree/")
                new = endpoint + quote(target) + (f"?{url.query}" if url.query else "") + (f"#{quote(anchor)}" if anchor else "")
                stats["repository"] += 1
            node.set("href", new)
        for img in doc.xpath(".//img[@src]"):
            raw = img.get("src").strip().rstrip('"')
            parts = urlsplit(raw)
            if parts.scheme or parts.netloc:
                if raw not in assets:
                    assets[raw] = fetch_asset(raw, work, len(assets) + 1)
                asset = assets[raw]
            else:
                path_in_repo = (root / path).parent.joinpath(unquote(parts.path)).resolve()
                asset = path_in_repo.as_uri() if path_in_repo.is_relative_to(root) and path_in_repo.is_file() else None
            if asset:
                img.set("src", asset)
                stats["images"] += 1
            else:
                alt = img.get("alt") or "原图"
                label = html.Element("span", {"class": "asset-note"})
                label.text = f"［{alt}："
                if img.xpath("ancestor::a[@href]"):
                    label.text = alt
                elif parts.scheme in {"http", "https"}:
                    a = etree.SubElement(label, "a", href=raw)
                    a.text, a.tail = "查看原图", "］"
                else:
                    label.text += "源文件未找到］"
                label.tail = img.tail
                img.getparent().replace(img, label)
                unresolved.append((vol, path, raw, "图片未嵌入"))
        for vid in doc.xpath(".//video | .//audio"):
            if vid.getparent() is not None:
                source = vid.get("src") or next(iter(vid.xpath("./source/@src")), "")
                if source and urlsplit(source).scheme in {"http", "https"}:
                    rep = html.Element("a", href=source)
                    rep.text = "打开原始媒体"
                else:
                    rep = html.Element("span")
                    rep.text = "［媒体见原始仓库］"
                rep.tail = vid.tail
                vid.getparent().replace(vid, rep)
                stats["media"] += 1
        blocks = doc.xpath(".//pre")
        for node in blocks:
            decorate_pre(node)
        entry["body"] = (escape(doc.text) if doc.text else "") + "".join(
            html.tostring(node, encoding="unicode", method="html") for node in doc)
        stats["codeblocks"] += len(blocks)
        stats["tables"] += len(doc.xpath(".//table"))
        stats["formulas"] += len(doc.xpath(".//math"))
    css = (HERE / "book.css").read_text(encoding="utf-8")
    index = []
    for vol, (subtitle, _, desc, modlist) in enumerate(VOLUMES, 1):
        group = [entry for entry in entries if entry["volume"] == vol]
        count = len([entry for entry in group if entry["module"] != "M0"])
        contents, chapters = [], []
        for position, entry in enumerate(group, 1):
            k, mod, title, path = (entry[key] for key in ("id", "module", "title", "target"))
            n = f"{position:02}"
            if position == 1 or mod != group[position - 2]["module"]:
                contents.append(f'<h2 class="contents-group">{MODULES[mod]}</h2>')
            contents.append(f'<div class="contents-item"><a href="#{k}"><span>{n}</span><strong>{escape(title)}</strong><small class="entry-page" data-for="{k}"></small></a></div>')
            chapters.append(f"""<article class="chapter" id="{k}">
<header class="chapter-heading"><span class="eyebrow">{MODULES[mod]} · {n}</span>
<h1>{escape(title)}</h1><div class="chapter-ref"><a href="{web}{quote(path)}">{escape(path.removeprefix("zh/"))}</a>　·　<a href="#contents">本册目录</a></div></header>
{entry["body"]}</article>""")
        track = "".join(f'<span{" class= current" if v == vol else ""}>{v:02}　{label}</span>'
                        for v, (_, label, _, _) in enumerate(VOLUMES, 1))
        colophon = f"""<section class="endmatter imprint" id="imprint"><span class="eyebrow">关于本书</span>
<h1>版本与许可</h1>
<p>原作者：davidkimai。原文为 <a href="https://github.com/jasontang-ai/Context-Engineering">Context-Engineering</a>。
译文源自 <a href="{ORIGIN}">Context-Engineering-ZH</a>，排版基于提交 <code>{edition}</code>。</p>
<p>这是一份面向离线阅读的中文排版版。正文按阅读路径重组，原始代码与项目文件可从各篇标题下的来源链接查阅。
跨册链接依赖 PDF 阅读器支持，请将六册 PDF 放在同一目录。</p>
<pre>{escape(license_text)}</pre></section>"""
        data = f"""<!doctype html><html lang="zh-CN"><head><meta charset="utf-8">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; img-src file: data:; style-src 'unsafe-inline'; base-uri 'none'; form-action 'none'">
<title>上下文工程 · 第 {vol} 册 · {escape(subtitle)}</title><style>{css}
@page {{ @top-right {{ content: "第 {vol:02} 册  /  {escape(subtitle)}"; }} }}
@page cover {{ @top-right {{ content: none; }} }}</style></head><body>
<section class="cover" aria-label="封面">
<div class="cover-line"><span>中文阅读版</span><span>第 {vol:02} 册 / 共 06 册</span></div>
<div class="cover-hero"><h1>上下文工程</h1><div class="cover-english">CONTEXT ENGINEERING</div></div>
<div class="cover-band"><strong>{escape(subtitle)}</strong><p>{escape(desc)}</p></div>
<div class="track">{track}</div>
<div class="cover-watermark" aria-hidden="true">{vol:02}</div>
<div class="cover-credit">原作者　davidkimai　/　中文译本　Context-Engineering-ZH<br>源版本　{edition}　·　MIT License　·　{count} 篇</div>
</section>
<nav class="contents" id="contents"><span class="eyebrow">第 {vol:02} 册　/　阅读目录</span><h1>本册目录</h1>
<p class="contents-intro">点击篇名进入正文。右侧为页码，每篇篇首均可返回目录。　<a href="#imprint">版本与许可</a></p>
<div class="contents-grid">{"".join(contents)}</div></nav>
{"".join(chapters)}{colophon}</body></html>"""
        html_path = work / f"{vol:02}.html"
        html_path.write_text(data, encoding="utf-8")
        # All same-volume links must point to real, uniquely named destinations.
        parsed = html.fromstring(data)
        ids = parsed.xpath("//@id")
        assert len(ids) == len(set(ids)), (vol, Counter(ids).most_common(3))
        idset = set(ids)
        assert all(href[1:] in idset for href in parsed.xpath("//a[starts-with(@href,'#')]/@href"))
        assert len(parsed.xpath("//nav//a[starts-with(@href,'#d')]")) == len(parsed.xpath("//article")) == len(group)
        index.append({"volume": vol, "title": subtitle, "count": count, "chapters": [
            {k: e[k] for k in ("target", "module", "id", "title")} for e in group]})
        print(f"{vol:02}  {count:3} 篇 + {len(group)-count} 附录  {html_path.stat().st_size:,} B", flush=True)
    print(f"版式完成：{len(entries)} 篇（含附录），{len(unresolved)} 项源链接或图像例外。", flush=True)
    return dict(commit=commit, dirty=dirty, stats=dict(stats), unresolved=unresolved,
                warnings=warnings, volumes=index)
