#!/usr/bin/env python3
"""chunk → 单文件装配，带结构指纹往返校验（任务卡 §7.5b）。

用法：
    python zh/tools/assemble.py 00_foundations/01_atoms_prompting.md --out zh/00_foundations/01_atoms_prompting.md
    python zh/tools/assemble.py 00_foundations/01_atoms_prompting.md --verify
    python zh/tools/assemble.py 00_foundations/01_atoms_prompting.md --verify --chunks-dir /tmp/c
    python zh/tools/assemble.py --self-test

合并规则：
    1. 读 .chunks/<路径>/chunk-NN.md（若存在），按编号顺序拼接
       （兼容旧式平铺命名 .chunks/<路径>.chunk-NN.md）
    2. 在每段前插入 <a id="chunk-N"></a> 与 <!-- chunk N/M | source_lines A-B | sha xxxx -->
    3. 第一段已含 front matter → 直接前置
    4. 第一段无 front matter → 生成最简 front matter
       （title 取首个 H1，source/chunks/status=todo）
    5. --verify：合并结果去掉 chunk 注释后，与原文的结构指纹必须相等
       ——围栏数、H2 数、{{占位符}}多重集、代码块语言序列
       不等则打印首个差异位置并退出 1

结构指纹与 check.py 的 G3/G4/G9 同源（都走 mdfence），所以三者不会互相打架。
仅用标准库。
"""

import argparse
import hashlib
import os
import re
import shutil
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import mdfence
import plan_chunks

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CHUNKS_BASENAME = ".chunks"

ANCHOR_RE = re.compile(r"^<a id=\"chunk-\d+\"></a>$")
CHUNK_COMMENT_RE = re.compile(r"^<!-- chunk \d+/\d+ \| .* -->$")
H1_RE = re.compile(r"^ {0,3}#[ \t]+\S")
FM_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.S)
CHUNK_NUM_RE = re.compile(r"chunk[-_.]?(\d+)", re.I)


# ─── chunk 发现 ────────────────────────────────────────────────────────────
def _chunk_roots(repo, override=None):
    if override:
        return [override]
    return [
        os.path.join(repo, "zh", CHUNKS_BASENAME),
        os.path.join(repo, CHUNKS_BASENAME),
    ]


def find_chunks(repo, source_rel, override=None):
    """返回 [(n, path)]，按 n 升序。未找到返回 []。

    目录式：<root>/<source>.md/chunk-01.md
    平铺式：<root>/<source>.md.chunk-01.md
    """
    for root in _chunk_roots(repo, override):
        dir_form = os.path.join(root, source_rel)
        if os.path.isdir(dir_form):
            out = []
            for name in os.listdir(dir_form):
                if not name.endswith(".md"):
                    continue
                m = CHUNK_NUM_RE.search(name)
                if m:
                    out.append((int(m.group(1)), os.path.join(dir_form, name)))
            if out:
                return sorted(out)
        flat_dir = os.path.dirname(os.path.join(root, source_rel))
        prefix = os.path.basename(source_rel) + ".chunk-"
        if os.path.isdir(flat_dir):
            out = []
            for name in os.listdir(flat_dir):
                if name.startswith(prefix) and name.endswith(".md"):
                    m = CHUNK_NUM_RE.search(name[len(prefix) - 1:])
                    if m:
                        out.append((int(m.group(1)), os.path.join(flat_dir, name)))
            if out:
                return sorted(out)
    return []


# ─── front matter ──────────────────────────────────────────────────────────
def has_front_matter(text):
    return bool(FM_RE.match(text))


def _first_h1(text):
    fences, lines = mdfence.scan_fences(text)
    inside = set()
    for f in fences:
        inside.update(range(f.start, f.end + 1))
    for k, line in enumerate(lines):
        if k in inside:
            continue
        s = line.rstrip("\r\n")
        if H1_RE.match(s):
            return s.strip().lstrip("#").strip()
    return ""


def synthetic_front_matter(source_rel, title, chunks, module=None, task=None, sha=None):
    """规则 4：第一段无 front matter 时生成最简 front matter。"""
    lines = ["---", "title: %s" % (title or source_rel), "source: %s" % source_rel]
    if module:
        lines.append("module: %s" % module)
    if task:
        lines.append("task: %s" % task)
    if sha:
        lines.append("source_sha256: %s" % sha)
    lines.append("chunks: %d" % chunks)
    lines.append("chunks_done: []")
    lines.append("status: todo")
    lines.append("---")
    return "\n".join(lines) + "\n\n"


# ─── 锚点 ──────────────────────────────────────────────────────────────────
def _rel_link(from_dir, to_path):
    """from_dir 与 to_path 都是仓库根相对路径；返回 POSIX 相对链接。"""
    rel = os.path.relpath(to_path, from_dir or ".").replace(os.sep, "/")
    return rel if rel.startswith("../") else rel


def bilingual_anchor(source_rel, target_rel):
    """双语锚点两行。链接按目标文件所在深度自动生成，译者不要手写。"""
    tdir = os.path.dirname(target_rel)
    return (
        "> 原文：[%s](%s)\n"
        "> 术语对照：[GLOSSARY.md](%s) ｜ 阅读路径：[LEARNING_PATH.md](%s)\n"
        % (
            source_rel,
            _rel_link(tdir, source_rel),
            _rel_link(tdir, "zh/GLOSSARY.md"),
            _rel_link(tdir, "zh/LEARNING_PATH.md"),
        )
    )


def has_bilingual_anchor(text):
    head = "\n".join(text.splitlines()[:40])
    return "> 原文：" in head and "GLOSSARY" in head


def ensure_bilingual_anchor(text, source_rel, target_rel):
    """若无锚点，插在 front matter 之后、正文之前。

    合并文本开头可能先有 chunk 锚点行，故先跳过它们再定位 front matter。
    """
    if has_bilingual_anchor(text):
        return text
    lines = text.splitlines(keepends=True)
    k = 0
    while k < len(lines) and (ANCHOR_RE.match(lines[k].rstrip("\r\n"))
                              or CHUNK_COMMENT_RE.match(lines[k].rstrip("\r\n"))):
        k += 1
    head, rest = "".join(lines[:k]), "".join(lines[k:])
    block = bilingual_anchor(source_rel, target_rel)
    m = re.match(r"\A---\r?\n.*?\r?\n---\r?\n", rest, re.S)
    if m:
        return head + m.group(0) + "\n" + block + rest[m.end():].lstrip("\n")
    return head + block + "\n" + rest


def anchor_block(index, total, a, b, sha8):
    return (
        '<a id="chunk-%d"></a>\n<!-- chunk %d/%d | source_lines %d-%d | sha %s -->\n'
        % (index, index, total, a, b, sha8)
    )


def strip_anchors(text):
    """去掉 chunk 锚点、注释行、双语锚点行，供结构指纹比对。"""
    out = []
    for line in text.splitlines(keepends=True):
        s = line.rstrip("\r\n")
        if ANCHOR_RE.match(s) or CHUNK_COMMENT_RE.match(s):
            continue
        if s.startswith("> 原文：") or (s.startswith("> 术语对照：")):
            continue
        out.append(line)
    return "".join(out)


# ─── 结构指纹 ──────────────────────────────────────────────────────────────
def fingerprint(text):
    """结构指纹：围栏数、H2 数、占位符多重集、代码块语言序列。"""
    fences, lines = mdfence.scan_fences(text)
    inside = set()
    for f in fences:
        inside.update(range(f.start, f.end + 1))
    h2 = 0
    for k, line in enumerate(lines):
        if k in inside:
            continue
        if re.match(r"^ {0,3}##[ \t]+\S", line.rstrip("\r\n")):
            h2 += 1
    return {
        "fences": len(fences),
        "h2": h2,
        "placeholders": mdfence.placeholders(text),
        "langs": [f.lang for f in fences],
    }


def compare_fingerprints(got, want):
    """返回差异描述列表；空列表表示结构相等。"""
    diffs = []
    for key, label in (("fences", "围栏数"), ("h2", "H2 数")):
        if got[key] != want[key]:
            diffs.append("%s %d ≠ 原文 %d" % (label, got[key], want[key]))
    if got["placeholders"] != want["placeholders"]:
        a, b = got["placeholders"], want["placeholders"]
        extra = [x for x in a if x not in b]
        miss = [x for x in b if x not in a]
        diffs.append(
            "占位符多重集不同（多 %s / 缺 %s）" % (extra[:5] or "无", miss[:5] or "无")
        )
    if got["langs"] != want["langs"]:
        for i, (x, y) in enumerate(zip(got["langs"], want["langs"]), 1):
            if x != y:
                diffs.append("代码块语言序列第 %d 块 %r ≠ 原文 %r" % (i, x, y))
                break
        else:
            diffs.append(
                "代码块数量不同（多 %d / 缺 %d）"
                % (
                    len(got["langs"]) - len(want["langs"]),
                    len(want["langs"]) - len(got["langs"]),
                )
            )
    return diffs


def _first_diff_line(got_text, want_text):
    """首个内容差异的行号（1 基），用于打印定位。"""
    a = got_text.splitlines()
    b = want_text.splitlines()
    for i in range(min(len(a), len(b))):
        if a[i] != b[i]:
            return i + 1
    return min(len(a), len(b)) + 1


# ─── 装配 ──────────────────────────────────────────────────────────────────
def target_rel_of(source_rel):
    """源文件 → 译文路径（zh/ 前缀）。manifest 的映射规则，此处只需路径拼接。"""
    return "zh/" + source_rel


def assemble(source_rel, repo=REPO, chunks_dir=None, out_path=None):
    """读 chunk 并合并，返回 (merged_text, info)。

    info = {found, total, plan, missing}
    """
    full = os.path.join(repo, source_rel)
    if not os.path.isfile(full):
        raise FileNotFoundError(source_rel)
    with open(full, "rb") as fh:
        raw = fh.read()
    source_text = raw.decode("utf-8", errors="replace")
    source_sha = hashlib.sha256(raw).hexdigest()

    plan, _lines, _total = plan_chunks.plan(source_text)
    if not plan:
        # 空文件（authored）：无需装配
        return source_text, {"found": 0, "total": 0, "plan": [], "missing": [], "authored": True}

    found = find_chunks(repo, source_rel, chunks_dir)
    if not found:
        return None, {"found": 0, "total": len(plan), "plan": plan, "missing": [], "authored": False}

    total = len(found)
    parts = []
    for idx, (num, path) in enumerate(found, 1):
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            body = fh.read()
        if idx == 1 and not has_front_matter(body):
            body = synthetic_front_matter(source_rel, _first_h1(body), total) + body
        # 段级锚点：行号与 sha 取切分计划里的第 idx 段（越界则用首段）
        a, b, _tb, _titles = plan[min(idx, len(plan)) - 1]
        sha8 = plan_chunks._sha8(source_text, a, b)
        parts.append(anchor_block(idx, total, a, b, sha8) + body)
    merged = "".join(parts)
    if not merged.endswith("\n") and source_text.endswith("\n"):
        merged += "\n"
    merged = ensure_bilingual_anchor(merged, source_rel, target_rel_of(source_rel))

    info = {
        "found": total,
        "total": len(plan),
        "plan": plan,
        "missing": [i for i in range(1, total + 1) if i > total],
        "source_sha256": source_sha,
        "authored": False,
    }
    return merged, info


def verify(source_rel, repo=REPO, chunks_dir=None):
    """结构指纹往返校验。返回 (ok, lines_of_report)。"""
    lines = []
    merged, info = assemble(source_rel, repo=repo, chunks_dir=chunks_dir)
    if not merged:
        lines.append("无 chunk 文件，跳过校验（%s）" % source_rel)
        return True, lines
    with open(os.path.join(repo, source_rel), "r", encoding="utf-8", errors="replace") as fh:
        source_text = fh.read()

    stripped = strip_anchors(merged)
    got = fingerprint(stripped)
    want = fingerprint(source_text)
    diffs = compare_fingerprints(got, want)

    lines.append("源文件  %s" % source_rel)
    lines.append("chunk   %d/%d" % (info["found"], info["total"]))
    lines.append(
        "指纹    围栏 %d/%d  H2 %d/%d  占位符 %d/%d  代码语言序列 %s"
        % (
            got["fences"],
            want["fences"],
            got["h2"],
            want["h2"],
            len(got["placeholders"]),
            len(want["placeholders"]),
            "一致" if got["langs"] == want["langs"] else "不一致",
        )
    )
    if diffs:
        lines.append("FAIL  结构指纹不等：")
        for d in diffs:
            lines.append("      - %s" % d)
        lines.append(
            "      首个内容差异位于第 %d 行" % _first_diff_line(stripped, source_text)
        )
        return False, lines
    lines.append("PASS  往返无损（结构指纹相等）")
    return True, lines


# ─── 自测 ──────────────────────────────────────────────────────────────────
def _pick_multi_chunk(repo=REPO, want=3):
    """挑一个段数 >= want 的源文件，用于多段往返自测。"""
    cands = [
        "00_foundations/07_prompt_programming.md",
        "NOCODE/10_mental_models/02_budget_model.md",
        "40_reference/retrieval_indexing.md",
    ]
    for c in cands:
        full = os.path.join(repo, c)
        if not os.path.isfile(full):
            continue
        with open(full, "r", encoding="utf-8", errors="replace") as fh:
            text = fh.read()
        if len(plan_chunks.plan(text)[0]) >= want:
            return c
    return None


def _roundtrip(src, repo, tmp):
    """把 src 按 plan 拆成 chunk 写入 tmp，再装配回文字。返回 (merged, info, text, plan, lines)。"""
    with open(os.path.join(repo, src), "r", encoding="utf-8", errors="replace") as fh:
        text = fh.read()
    plan, lines, _total = plan_chunks.plan(text)
    chunk_dir = os.path.join(tmp, src)
    os.makedirs(chunk_dir, exist_ok=True)
    for i, (a, b, _tb, _t) in enumerate(plan, 1):
        with open(os.path.join(chunk_dir, "chunk-%02d.md" % i), "w", encoding="utf-8") as fh:
            fh.write("".join(lines[a - 1:b]))
    merged, info = assemble(src, repo=repo, chunks_dir=tmp)
    return merged, info, text, plan, lines


def self_test(repo=REPO, verbose=True):
    """用真实源文件做"原文透传"装配，验证往返与结构指纹。"""
    tmp = tempfile.mkdtemp(prefix="zh_assemble_selftest_")
    ok_all = True
    try:
        # ── 自测 1a：单段文件 ──
        src1 = "00_foundations/02_molecules_context.md"
        if os.path.isfile(os.path.join(repo, src1)):
            merged, info, text, plan, _lines = _roundtrip(src1, repo, tmp)
            stripped = strip_anchors(merged)
            body = FM_RE.sub("", stripped, count=1) if has_front_matter(stripped) else stripped
            body = body.lstrip("\n")  # 合成 front matter 与锚点后多出的空行
            diffs = compare_fingerprints(fingerprint(stripped), fingerprint(text))
            anchors = len(re.findall(r'<a id="chunk-\d+"></a>', merged))
            ok = body == text and not diffs and anchors == len(plan) and info["found"] == len(plan)
            ok_all = ok_all and ok
            if verbose:
                print("自测 1  单段往返        %s（%d 段）" % ("PASS" if ok else "FAIL", len(plan)))
                if not ok:
                    print("        逐字节相等 %s，锚点 %d，围栏 %d/%d，H2 %d/%d" % (
                        body == text, anchors,
                        fingerprint(stripped)["fences"], fingerprint(text)["fences"],
                        fingerprint(stripped)["h2"], fingerprint(text)["h2"]))

        # ── 自测 1b：多段文件（锚点、chunk 顺序、拼接边界） ──
        src2 = _pick_multi_chunk(repo)
        if src2:
            merged, info, text, plan, _lines = _roundtrip(src2, repo, tmp)
            stripped = strip_anchors(merged)
            body = FM_RE.sub("", stripped, count=1) if has_front_matter(stripped) else stripped
            body = body.lstrip("\n")
            diffs = compare_fingerprints(fingerprint(stripped), fingerprint(text))
            anchors = len(re.findall(r'<a id="chunk-\d+"></a>', merged))
            ok = body == text and not diffs and anchors == len(plan) and info["found"] == len(plan)
            ok_all = ok_all and ok
            if verbose:
                print("自测 2  多段往返        %s（%s，%d 段）" % ("PASS" if ok else "FAIL", src2, len(plan)))
                if not ok:
                    print("        逐字节相等 %s，锚点 %d/%d" % (body == text, anchors, len(plan)))
                    for d in diffs:
                        print("        - %s" % d)
        else:
            if verbose:
                print("自测 2  多段往返        SKIP（找不到多段样例）")
            src2 = "00_foundations/02_molecules_context.md"

        if not os.path.isfile(os.path.join(repo, src2)):
            if verbose:
                print("self-test: SKIP（仓库无样例文件）")
            return 0
        merged, info, text, plan, _lines = _roundtrip(src2, repo, tmp)

        # ── 自测 3：篡改代码块语言标记 → 结构指纹必须报错 ──
        bad = merged
        for m in re.finditer(r"^( {0,3})(`{3,}|~{3,})(\w+)", merged, re.M):
            bad = merged[: m.start(3)] + merged[m.end(3):]
            break
        neg_ok = bad != merged and bool(compare_fingerprints(fingerprint(bad), fingerprint(text)))
        ok_all = ok_all and neg_ok
        if verbose:
            print("自测 3  篡改语言标记应 FAIL  %s" % ("PASS" if neg_ok else "FAIL（未检测到差异）"))

        # ── 自测 4：删一个 H2 → H2 数必须报错 ──
        m = re.search(r"^ {0,3}##[ \t]+\S.*\n", merged, re.M)
        neg2 = True
        if m:
            bad2 = merged[: m.start()] + merged[m.end():]
            neg2 = bool(compare_fingerprints(fingerprint(bad2), fingerprint(text)))
        ok_all = ok_all and neg2
        if verbose:
            print("自测 4  删 H2 应 FAIL       %s" % ("PASS" if neg2 else "FAIL（未检测到差异）"))

        # ── 自测 5：丢一个占位符 → 多重集必须报错 ──
        phs = mdfence.placeholders(text)
        neg3 = True
        if phs:
            bad3 = merged.replace(phs[0], "", 1)
            neg3 = bool(compare_fingerprints(fingerprint(bad3), fingerprint(text)))
        ok_all = ok_all and neg3
        if verbose:
            print("自测 5  丢占位符应 FAIL     %s" % ("PASS" if neg3 else "FAIL（未检测到差异）"))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    if verbose:
        print("self-test: %s" % ("PASS" if ok_all else "FAIL"))
    return 0 if ok_all else 1


def main(argv=None):
    ap = argparse.ArgumentParser(description="chunk → 单文件装配")
    ap.add_argument("source", nargs="?", help="源文件，仓库根相对")
    ap.add_argument("--out", metavar="PATH", help="输出路径（仓库根相对或绝对）")
    ap.add_argument("--verify", action="store_true", help="只校验结构指纹往返")
    ap.add_argument("--chunks-dir", metavar="DIR", help="chunk 根目录（默认 zh/.chunks 或 .chunks）")
    ap.add_argument("--self-test", action="store_true", help="内置正反样例自测")
    args = ap.parse_args(argv)

    if args.self_test:
        return self_test()

    if not args.source:
        ap.error("需要 <源文件路径>，或用 --self-test")

    src = args.source.replace(os.sep, "/")
    if args.verify:
        ok, lines = verify(src, chunks_dir=args.chunks_dir)
        print("\n".join(lines))
        return 0 if ok else 1

    merged, info = assemble(src, chunks_dir=args.chunks_dir)
    if merged is None:
        print("未找到 chunk 文件：%s（需要 %d 段）" % (src, info["total"]), file=sys.stderr)
        return 2
    if not args.out:
        sys.stdout.write(merged)
        return 0
    out = args.out if os.path.isabs(args.out) else os.path.join(REPO, args.out)
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(merged)
    print("已写出 %s（%d 段，%d 字节）" % (args.out, info["found"], len(merged.encode("utf-8"))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
