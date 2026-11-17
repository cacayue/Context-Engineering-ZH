"""围栏（fenced code block）解析与可译字节计算。

共享模块，被 manifest.py / plan_chunks.py / check.py 复用。
仅用标准库。

围栏规则（任务卡 §6 第 0 步）：
  - ``` 与 ~~~ 两种定界符
  - 3 个及以上反引号/波浪号
  - 允许 0-3 空格缩进
  - info string 可含字母数字
  - 关闭围栏需同字符、长度 >= 开启长度
  - 未闭合围栏按到文末处理
"""

import re

# 框线字符集（任务卡 §6 第 3 步）
BOX_CHARS = "─│┌┐└┘├┤┬┴┼╭╮╰╯╔╗╚╝║═"
BOX_RE = re.compile("[" + re.escape(BOX_CHARS) + "]")

# 开启围栏：0-3 空格缩进 + 3 个以上同字符 + info string
FENCE_OPEN_RE = re.compile(r"^( {0,3})(`{3,}|~{3,})(.*)$")

# 可译文本块内出现这些字符即判定"含全角"（G2）
CJK_RE = re.compile(r"[\u4e00-\u9fff\u3000-\u303f\uff00-\uffef]")

PLACEHOLDER_RE = re.compile(r"\{\{[^}]+\}\}")


class Fence:
    """一个围栏块。start/end 为 0 基行号，end 含关闭行；未闭合时 end = 行数-1。"""

    __slots__ = ("start", "end", "lang", "indent", "closed", "bytes", "kind")

    def __init__(self, start, end, lang, indent, closed, nbytes, kind):
        self.start = start
        self.end = end
        self.lang = lang
        self.indent = indent
        self.closed = closed
        self.bytes = nbytes
        self.kind = kind  # "code" | "art" | "text"

    def __repr__(self):  # pragma: no cover - 仅调试用
        return (
            f"<Fence {self.start + 1}-{self.end + 1} lang={self.lang!r} "
            f"{self.kind} {self.bytes}B>"
        )


def _line_bytes(lines, idx):
    return len(lines[idx].encode("utf-8"))


def scan_fences(text):
    """返回 (fences, lines)。

    lines 为 text.splitlines(keepends=True)。行号 0 基。
    块字节 = 块内各行 UTF-8 字节之和（含开启/关闭围栏行）。
    """
    lines = text.splitlines(keepends=True)
    n = len(lines)
    fences = []
    i = 0
    while i < n:
        m = FENCE_OPEN_RE.match(lines[i].rstrip("\r\n"))
        if not m:
            i += 1
            continue
        indent, marker, info = m.group(1), m.group(2), m.group(3)
        char = marker[0]
        length = len(marker)
        # info string：去除首尾空白；语言标记取首个 token
        info = info.strip()
        lang = ""
        if info:
            # 允许 ```{.python} ``` 之类，取首个单词并剥离花括号/点
            first = info.split()[0]
            first = first.strip("{}.")
            if first and re.fullmatch(r"[A-Za-z0-9_+.#-]*", first):
                lang = first
        # 找关闭行：同字符、长度 >= 开启长度、仅允许尾随空白
        close_re = re.compile(
            r"^ {0,3}" + re.escape(char) + "{" + str(length) + r",}\s*$"
        )
        j = i + 1
        closed = False
        while j < n:
            if close_re.match(lines[j].rstrip("\r\n")):
                closed = True
                break
            j += 1
        last = j if closed else n - 1
        block_bytes = sum(_line_bytes(lines, k) for k in range(i, last + 1))
        body = "".join(lines[k] for k in range(i + 1, last + 1))
        if lang:
            kind = "code"
        elif BOX_RE.search(body):
            kind = "art"
        else:
            kind = "text"
        fences.append(Fence(i, last, lang, len(indent), closed, block_bytes, kind))
        i = last + 1
    return fences, lines


def translatable_bytes(text):
    """可译字节 = 文件总字节 − 不可译块字节。

    - 有语言标记块（code）：整块（含围栏行）不可译。
    - 含框线无标记块（art）：仅图体（不含围栏定界行）不可译——
      围栏行本身属于 Markdown 结构，不属于 ASCII 图内容。
      这条口径是复现 676 段的必要条件（实测差 1 段：
      `60_protocols/shells/recursive.memory.attractor.shell.md` 18424 → 18456 字节）。
    - 无标记纯文本块（text）：可译，不扣除。
    """
    fences, lines = scan_fences(text)
    total = len(text.encode("utf-8"))
    untranslatable = 0
    for f in fences:
        if f.kind == "code":
            untranslatable += f.bytes
        elif f.kind == "art":
            untranslatable += f.bytes - _fence_line_bytes(lines, f)
    return total - untranslatable


def _fence_line_bytes(lines, f):
    """围栏定界行的字节数（未闭合块只有开启行）。"""
    n = _line_bytes(lines, f.start)
    if f.closed:
        n += _line_bytes(lines, f.end)
    return n


def chunks_for(translatable, file_bytes, chunk_bytes=6144):
    """段数 = max(1, ceil(可译字节 / chunk_bytes))；空文件（<5 字节）为 0。"""
    if file_bytes < 5:
        return 0
    if translatable <= 0:
        return 1
    return max(1, -(-translatable // chunk_bytes))


def strip_fences(text):
    """返回把不可译块替换为空行后的文本，用于散文区搜索（G1/G7）。"""
    fences, lines = scan_fences(text)
    out = list(lines)
    for f in fences:
        if f.kind in ("code", "art"):
            for k in range(f.start, f.end + 1):
                out[k] = "\n" if out[k].endswith("\n") else ""
    return "".join(out)


def block_sequence(text):
    """代码块语言序列（G3 用）。无标记块记为 ""。"""
    fences, _ = scan_fences(text)
    return [f.lang for f in fences]


def h2_titles(text):
    """围栏外的 H2 标题列表（G9 用）。"""
    fences, lines = scan_fences(text)
    inside = set()
    for f in fences:
        inside.update(range(f.start, f.end + 1))
    out = []
    for k, line in enumerate(lines):
        if k in inside:
            continue
        if re.match(r"^ {0,3}##[ \t]+\S", line.rstrip("\r\n")):
            out.append(line.rstrip("\r\n").strip())
    return out


def h3_titles(text):
    fences, lines = scan_fences(text)
    inside = set()
    for f in fences:
        inside.update(range(f.start, f.end + 1))
    out = []
    for k, line in enumerate(lines):
        if k in inside:
            continue
        if re.match(r"^ {0,3}###[ \t]+\S", line.rstrip("\r\n")):
            out.append(line.rstrip("\r\n").strip())
    return out


def placeholders(text):
    """{{...}} 多重集（排序后列表）。"""
    return sorted(PLACEHOLDER_RE.findall(text))
