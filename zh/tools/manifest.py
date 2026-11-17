#!/usr/bin/env python3
"""扫描源 .md 与 zh/ 译文，生成 zh/manifest.json。

用法：
    python zh/tools/manifest.py             # 扫描全部，写 zh/manifest.json
    python zh/tools/manifest.py --check     # 只比对，不写；有漂移则退出码 1
    python zh/tools/manifest.py --module M2 # 只处理该模块

仅用标准库。
"""

import argparse
import hashlib
import json
import os
import re
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import mdfence
import zmap

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MANIFEST = os.path.join(REPO, "zh", "manifest.json")
CHUNK_BYTES = 6144
EMPTY_THRESHOLD = 5
BASE_COMMIT = "6158def"

FM_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.S)


def _sha256(data):
    return hashlib.sha256(data).hexdigest()


def read_front_matter(text):
    """极简 front matter 解析：只取顶层标量与列表。

    返回 dict；无 front matter 返回 None。
    """
    m = FM_RE.match(text)
    if not m:
        return None
    fm = {}
    key = None
    for raw in m.group(1).splitlines():
        line = raw.rstrip()
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if re.match(r"^\s+-\s*", line) and key:
            fm.setdefault(key, [])
            if isinstance(fm[key], list):
                fm[key].append(line.strip()[1:].strip())
            continue
        km = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if not km:
            continue
        key, val = km.group(1), km.group(2).strip()
        if val.startswith("[") and val.endswith("]"):
            inner = val[1:-1].strip()
            fm[key] = [v.strip() for v in inner.split(",") if v.strip()] if inner else []
        elif val == "":
            fm[key] = []
        else:
            fm[key] = val.strip("'\"")
    return fm


def _as_int_list(val):
    if not isinstance(val, list):
        return []
    out = []
    for v in val:
        try:
            out.append(int(str(v).strip()))
        except ValueError:
            pass
    return sorted(set(out))


def entry_for(rel):
    src_path = os.path.join(REPO, rel)
    with open(src_path, "rb") as fh:
        raw = fh.read()
    text = raw.decode("utf-8", errors="replace")
    source_bytes = len(raw)
    todo = mdfence.translatable_bytes(text)
    chunks = mdfence.chunks_for(todo, source_bytes, CHUNK_BYTES)
    is_empty = source_bytes < EMPTY_THRESHOLD

    module = zmap.module_of(rel)
    task = zmap.task_of(rel, module)
    target = zmap.target_of(rel)

    status = "authored" if is_empty else "todo"
    chunks_done = []

    tgt_path = os.path.join(REPO, target)
    if os.path.isfile(tgt_path):
        with open(tgt_path, "rb") as fh:
            ttext = fh.read().decode("utf-8", errors="replace")
        fm = read_front_matter(ttext)
        if fm is None:
            status = "draft"
        else:
            status = str(fm.get("status") or ("authored" if is_empty else "draft"))
            chunks_done = _as_int_list(fm.get("chunks_done"))

    return {
        "source": rel,
        "target": target,
        "module": module,
        "task": task,
        "source_bytes": source_bytes,
        "source_sha256": _sha256(raw),
        "todo_bytes": todo,
        "chunks": chunks,
        "chunks_done": chunks_done,
        "status": status,
        "authored": is_empty,
    }


def build(module_filter=None):
    files = []
    for rel in zmap.walk_sources(REPO):
        if module_filter and zmap.module_of(rel) != module_filter:
            continue
        files.append(entry_for(rel))
    files.sort(key=lambda e: e["source"])
    files_done = sum(e["chunks"] for e in files)
    return {
        "base_commit": BASE_COMMIT,
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "chunk_bytes": CHUNK_BYTES,
        "totals": {
            "files": len(files),
            "chunks": files_done,
            "chunks_done": sum(len(e["chunks_done"]) for e in files),
            "authored": sum(1 for e in files if e["authored"]),
            "published": sum(1 for e in files if e["status"] == "published"),
        },
        "files": files,
    }


def summarise(data):
    print(
        "manifest: %d files / %d chunks / %d authored"
        % (data["totals"]["files"], data["totals"]["chunks"], data["totals"]["authored"])
    )
    per_mod = {}
    for e in data["files"]:
        f, c = per_mod.get(e["module"], (0, 0))
        per_mod[e["module"]] = (f + 1, c + e["chunks"])
    parts = []
    for m in zmap.MODULES:
        f, c = per_mod.get(m, (0, 0))
        parts.append("%s %d篇/%d段" % (m, f, c))
    print("模块分布: " + "  ".join(parts))


def compare(data):
    """--check：与磁盘上的 manifest.json 比对关键字段。"""
    if not os.path.isfile(MANIFEST):
        print("manifest.json 不存在，请先运行 python zh/tools/manifest.py", file=sys.stderr)
        return 1
    with open(MANIFEST, encoding="utf-8") as fh:
        old = json.load(fh)
    old_map = {e["source"]: e for e in old.get("files", [])}
    new_map = {e["source"]: e for e in data["files"]}
    drift = 0
    for src in sorted(set(old_map) | set(new_map)):
        a, b = old_map.get(src), new_map.get(src)
        if a is None or b is None:
            print("漂移 %s: %s" % (src, "新增" if a is None else "丢失"))
            drift += 1
            continue
        for key in ("source_sha256", "source_bytes", "chunks", "todo_bytes", "module", "task"):
            if a.get(key) != b.get(key):
                print(
                    "漂移 %s: %s %r -> %r" % (src, key, a.get(key), b.get(key))
                )
                drift += 1
    if old.get("totals", {}).get("files") != data["totals"]["files"]:
        print("漂移 totals.files: %s -> %s" % (old.get("totals", {}).get("files"), data["totals"]["files"]))
        drift += 1
    if old.get("totals", {}).get("chunks") != data["totals"]["chunks"]:
        print("漂移 totals.chunks: %s -> %s" % (old.get("totals", {}).get("chunks"), data["totals"]["chunks"]))
        drift += 1
    summarise(data)
    if drift:
        print("漂移项: %d" % drift, file=sys.stderr)
        return 1
    print("manifest 无漂移")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description="扫描源文件与译文，生成 zh/manifest.json")
    ap.add_argument("--check", action="store_true", help="只比对，不写；有漂移则退出码 1")
    ap.add_argument("--module", metavar="M2", help="只处理该模块")
    ap.add_argument("--stdout", action="store_true", help="只打印，不写文件")
    args = ap.parse_args(argv)

    data = build(args.module)
    summarise(data)

    if args.module:
        # 单模块模式：仅打印，不改动全局 manifest
        if args.stdout:
            json.dump(data, sys.stdout, ensure_ascii=False, indent=2)
            print()
        return 0

    if args.check:
        return compare(data)

    if args.stdout:
        json.dump(data, sys.stdout, ensure_ascii=False, indent=2)
        print()
        return 0

    os.makedirs(os.path.dirname(MANIFEST), exist_ok=True)
    with open(MANIFEST, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print("写入 %s" % os.path.relpath(MANIFEST, REPO))
    return 0


if __name__ == "__main__":
    sys.exit(main())
