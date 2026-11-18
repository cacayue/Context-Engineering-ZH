#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = ["lxml==6.1.3", "pypdf==7.1.0"]
# ///
"""从中文阅读路径生成六册及合订本，或显式发布到 GitHub Releases。"""

import argparse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
from tempfile import TemporaryDirectory
import unicodedata
from zipfile import ZIP_DEFLATED, ZipFile

from pdf_export import layout
from pdf_export.combined import COMPLETE, build_combined
from pdf_export.volumes import build_volumes

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "zh/dist/pdf"
REPO = "cacayue/Context-Engineering-ZH"
REF = "refs/heads/zh/main"
ARCHIVE = "Context-Engineering-ZH-Volumes.zip"


def run(*args, capture=False):
    return subprocess.run(args, cwd=ROOT, check=True, capture_output=capture, text=True).stdout


def git(*args):
    return run("git", *args, capture=True).strip()


def gh(*args):
    return run("gh", *args, "--repo", REPO, capture=True)


def clean_release_head(commit, tag):
    if not re.fullmatch(r"zh-pdf-\d{4}\.\d{2}\.\d{2}(?:\.\d+)?", tag):
        raise ValueError("Release 标签应为 zh-pdf-YYYY.MM.DD（同日可加 .2 等后缀）")
    if git("symbolic-ref", "--quiet", "HEAD") != REF or git("status", "--porcelain"):
        raise ValueError("Release 只能从干净的 zh/main 分支构建")
    remote = git("remote", "get-url", "origin").removesuffix(".git")
    if remote not in (f"git@github.com:{REPO}", f"https://github.com/{REPO}", f"ssh://git@github.com/{REPO}"):
        raise ValueError(f"origin 不是 {REPO}")
    if git("rev-parse", "HEAD") != commit or git("ls-remote", "origin", REF) != f"{commit}\t{REF}":
        raise ValueError("本机 HEAD、刚导出的版本和 origin/zh/main 必须一致；请先同步分支")
    if git("ls-remote", "origin", f"refs/tags/{tag}"):
        raise ValueError(f"远端标签 {tag} 已存在，请使用新标签")


def publish(tag, commit, assets, notes):
    if any(r["tagName"] == tag for r in json.loads(gh("release", "list", "--limit", "100", "--json", "tagName"))):
        raise ValueError(f"Release {tag} 已存在（含草稿），不会覆盖")
    title = f"上下文工程 · 中文 PDF（{tag.removeprefix('zh-pdf-')}）"
    gh("release", "create", tag, "--draft", "--target", commit, "--title", title, "--notes-file", str(notes),
       *(str(OUT / name) for name in assets))

    def checked_release(is_draft):
        release = json.loads(gh("release", "view", tag, "--json", "assets,isDraft,targetCommitish,url"))
        expected = {name: (OUT / name).stat().st_size for name in assets}
        actual = {asset["name"]: asset["size"] for asset in release["assets"] if asset.get("state") == "uploaded"}
        if release["isDraft"] != is_draft or actual != expected:
            raise ValueError(f"Release 状态或附件不完整，请在 GitHub 检查 {tag}，本机文件不受影响")
        return release

    draft = checked_release(True)
    if draft["targetCommitish"] != commit:
        raise ValueError(f"草稿 {tag} 未指向导出的提交")
    gh("release", "edit", tag, "--draft=false", "--latest")
    live = checked_release(False)
    if git("ls-remote", "origin", f"refs/tags/{tag}") != f"{commit}\trefs/tags/{tag}":
        raise ValueError(f"发布后的 {tag} 未指向导出的提交")
    print(f"GitHub Release：{live['url']}", flush=True)


def extract(pdf):
    return subprocess.run(["pdftotext", "-layout", str(pdf), "-"], check=True, capture_output=True).stdout


def verify_text(volumes, combined_pages, out):
    def clean(text):
        return re.sub(r"\s+", "", unicodedata.normalize("NFKC", text))

    pdfs = [out / f"{v['volume']:02}.pdf" for v in volumes] + [out / COMPLETE]
    with ThreadPoolExecutor(max_workers=3) as pool:
        texts = list(pool.map(extract, pdfs))
    for vol, text in zip(volumes, texts):
        pages = text.decode("utf-8").split("\f")
        assert pages[-1] == "" and len(pages) - 1 == vol["pages"]
        for chapter in vol["chapters"]:
            assert clean(chapter["title"]) in clean(pages[chapter["page"] - 1]), chapter["target"]
    front, body = texts[-1].split(b"\f", 1)
    assert "总目录" in front.decode("utf-8") and len(texts[-1].split(b"\f")) - 1 == combined_pages
    assert body == b"".join(texts[:-1]), "合订本正文与分册不一致"
    print("已核对各篇篇首及合订本全部正文的文字和顺序。", flush=True)


def package(out, report, volumes, combined_pages, links, tag):
    count = sum(v["count"] for v in volumes)
    volfiles = [f"{v['volume']:02}.pdf" for v in volumes]
    assets = [COMPLETE, ARCHIVE, *volfiles]
    edition = report["commit"][:12] + ("（含本地修改）" if report["dirty"] else "")
    text = (f"# 上下文工程 · 中文阅读版\n\n{count} 篇，合订本 {combined_pages:,} 页。"
            f"首册另附《阅读路径》和《术语表》。源版本：`{edition}`。\n")
    url = f"{layout.ORIGIN}/releases/download/{tag}/" if tag else ""
    table = "\n".join(f"| [{v['volume']:02} · {v['title']}]({url}{name}) | {v['count']} | {v['pages']} |"
                      for v, name in zip(volumes, volfiles))
    exceptions = Counter(item[3] for item in report["unresolved"])
    for vol in volumes:
        exceptions["跨册节锚点未打印，已跳篇首"] += len(vol["downgraded"])
    summary = "；".join(f"{key} {value} 项" for key, value in exceptions.items() if value)
    text += f"""
- [合订本 PDF]({url}{COMPLETE})：首页总目录，册间可在同一文件跳转。
- [六册 ZIP]({url}{ARCHIVE})：解压后保留六份 PDF 的文件名与相对位置。跨文件跳转需阅读器支持。

| 分册 | 篇数 | 页数 |
| --- | ---: | ---: |
{table}

已核对所有篇首、目录页码、合订本正文和 {links:,} 个文件内跳转。
"""
    if summary:
        text += f"\n源链接与图像例外：{summary}。\n"
    if report["warnings"]:
        text += f"\nPandoc 提示：{len(report['warnings'])} 篇；详见 export-report.json。\n"
    text += f"\n原作者：davidkimai。译文与排版遵循 MIT 许可。[重导说明]({layout.ORIGIN}/blob/{report['commit']}/zh/PDF.md)。\n"
    (out / "README.md").write_text(text, encoding="utf-8")
    if tag:
        (out / "release-notes.md").write_text(text, encoding="utf-8")
        for name in assets:
            text = text.replace(f"({url}{name})", f"({name})")
        (out / "README.md").write_text(text, encoding="utf-8")

    with ZipFile(out / ARCHIVE, "w", ZIP_DEFLATED, compresslevel=5) as bundle:
        for name in volfiles:
            bundle.write(out / name, name)
        bundle.writestr("README.txt", "六册文件请放在同一目录，不要改名。\n" +
                       "\n".join(f"{name}  {v['title']}" for name, v in zip(volfiles, volumes)))
        bundle.write(ROOT / "LICENSE", "LICENSE")
    with ZipFile(out / ARCHIVE) as bundle:
        assert bundle.namelist() == [*volfiles, "README.txt", "LICENSE"] and bundle.testzip() is None
    report.update(volumes=volumes, combined_pages=combined_pages, combined_links=links,
                  assets={name: (out / name).stat().st_size for name in assets})
    (out / "export-report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return assets


def main():
    parser = argparse.ArgumentParser(description="从 zh/manifest.json 导出六册和合订 PDF")
    parser.add_argument("--release", metavar="TAG", help="校验后发布新的 GitHub Release；默认只生成本地文件")
    args = parser.parse_args()
    if not __debug__:
        raise ValueError("不能关闭导出校验，请取消 PYTHONOPTIMIZE")
    tools = ["git", "pandoc", "google-chrome", "curl", "fc-match", "pdftotext"]
    if args.release:
        tools.append("gh")
    missing = [tool for tool in tools if not shutil.which(tool)]
    if missing:
        raise ValueError("缺少本机工具：" + "、".join(missing))
    for font in ("Noto Sans CJK SC", "Noto Serif CJK SC", "Noto Sans Mono CJK SC"):
        if font not in run("fc-match", "-f", "%{family}", font, capture=True):
            raise ValueError(f"缺少中文字体 {font}")
    commit = git("rev-parse", "HEAD")
    dirty = bool(git("status", "--porcelain"))
    if args.release:
        clean_release_head(commit, args.release)

    OUT.mkdir(parents=True, exist_ok=True)
    with TemporaryDirectory(prefix=".build-", dir=OUT) as scratch:
        stage = Path(scratch)
        work = stage / "work"
        work.mkdir()
        report = layout.render(ROOT, work, commit, dirty)
        volumes = build_volumes(report, work, stage)
        pages, links = build_combined(volumes, work, stage)
        verify_text(volumes, pages, stage)
        assets = package(stage, report, volumes, pages, links, args.release)
        if args.release:
            clean_release_head(commit, args.release)
        # Do not replace the previous export until every artifact has passed validation.
        for name in [*assets, "README.md", "export-report.json"]:
            (stage / name).replace(OUT / name)
        print(f"导出目录：{OUT}", flush=True)
        if args.release:
            publish(args.release, commit, assets, stage / "release-notes.md")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, subprocess.CalledProcessError, subprocess.TimeoutExpired) as error:
        print(f"PDF 导出失败：{error}", file=sys.stderr)
        if isinstance(error, subprocess.CalledProcessError) and error.stderr:
            print(error.stderr, file=sys.stderr)
        sys.exit(1)
