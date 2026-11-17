"""极简 YAML 子集解析器（仅标准库，不依赖 pyyaml）。

支持 GLOSSARY.yaml 需要的形态：
  - 顶层列表，元素为映射
  - 标量 ``key: value``（含引号、内联列表 ``[a, b]``）
  - 缩进嵌套：``key:`` 后跟更深缩进的块
  - ``- value`` 与 ``- key: value``（列表内映射）

不支持锚点、多行标量、flow mapping 的嵌套组合——GLOSSARY 用不到。
"""

import re

_KEY_RE = re.compile(r"^([A-Za-z_][\w-]*):(?:\s+(.*))?$")
_INLINE_LIST_RE = re.compile(r"^\[(.*)\]$", re.S)


class YamlError(ValueError):
    pass


def _strip_comment(line):
    out = []
    quote = None
    for i, ch in enumerate(line):
        if quote:
            if ch == quote:
                quote = None
        elif ch in "\"'":
            quote = ch
        elif ch == "#" and (i == 0 or line[i - 1] in " \t"):
            break
        out.append(ch)
    return "".join(out).rstrip()


def _scalar(raw):
    s = raw.strip()
    if not s:
        return None
    if len(s) >= 2 and s[0] == s[-1] and s[0] in "\"'":
        return s[1:-1]
    m = _INLINE_LIST_RE.match(s)
    if m:
        inner = m.group(1).strip()
        if not inner:
            return []
        return [_scalar(p) for p in _split_inline(inner)]
    low = s.lower()
    if low in ("null", "~", "none"):
        return None
    if low in ("true", "yes"):
        return True
    if low in ("false", "no"):
        return False
    if re.fullmatch(r"-?\d+", s):
        return int(s)
    if re.fullmatch(r"-?\d+\.\d+", s):
        return float(s)
    return s


def _split_inline(s):
    parts, cur, quote = [], [], None
    for ch in s:
        if quote:
            cur.append(ch)
            if ch == quote:
                quote = None
        elif ch in "\"'":
            quote = ch
            cur.append(ch)
        elif ch == ",":
            parts.append("".join(cur).strip())
            cur = []
        else:
            cur.append(ch)
    if cur:
        parts.append("".join(cur).strip())
    return [p for p in parts if p]


class _Lines:
    def __init__(self, text):
        self.rows = []
        for raw in text.splitlines():
            if not raw.strip():
                continue
            stripped = _strip_comment(raw)
            if not stripped.strip():
                continue
            if stripped.strip() in ("---", "..."):
                continue
            indent = len(stripped) - len(stripped.lstrip(" "))
            self.rows.append([indent, stripped.strip()])
        self.i = 0

    def peek(self):
        return self.rows[self.i] if self.i < len(self.rows) else None


def _parse_block(L, indent):
    row = L.peek()
    if row is None:
        return None, L.i
    if row[1].startswith("- ") or row[1] == "-":
        return _parse_list(L, indent)
    return _parse_map(L, indent)


def _is_continuation(row):
    """深缩进、不形如 key: 也不形如 - 的行，视为上一个标量的续行。"""
    return not row[1].startswith("- ") and not _KEY_RE.match(row[1])


def _parse_list(L, indent):
    out = []
    while True:
        row = L.peek()
        if row is None or row[0] < indent:
            return out, L.i
        if row[0] > indent:
            raise YamlError("缩进异常：%r" % (row,))
        if not (row[1].startswith("- ") or row[1] == "-"):
            return out, L.i
        body = row[1][2:].strip() if row[1].startswith("- ") else ""
        L.i += 1
        if not body:
            val, _ = _parse_block(L, L.peek()[0] if L.peek() else indent + 2)
            out.append(val)
            continue
        kv = _KEY_RE.match(body)
        if kv:
            # 列表内的映射：当前行是第一个键，后续同层缩进的键接续
            item = {}
            key, raw = kv.group(1), kv.group(2)
            if raw is None or not raw.strip():
                nxt = L.peek()
                if nxt is not None and nxt[0] > indent:
                    val, _ = _parse_block(L, nxt[0])
                else:
                    val = None
                item[key] = val
            else:
                item[key] = _scalar(raw)
            child_indent = indent + 2
            nxt = L.peek()
            if nxt is not None and nxt[0] > indent:
                child_indent = nxt[0]
                more, _ = _parse_map(L, child_indent)
                if isinstance(more, dict):
                    item.update(more)
            out.append(item)
        else:
            out.append(_scalar(body))


def _parse_map(L, indent):
    out = {}
    while True:
        row = L.peek()
        if row is None or row[0] < indent:
            return out, L.i
        if row[0] > indent:
            raise YamlError("缩进异常：%r" % (row,))
        if row[1].startswith("- "):
            return out, L.i
        m = _KEY_RE.match(row[1])
        if not m:
            raise YamlError("无法解析：%r" % (row,))
        key, raw = m.group(1), m.group(2)
        L.i += 1
        if raw is None or not raw.strip():
            nxt = L.peek()
            if nxt is not None and nxt[0] > indent:
                val, _ = _parse_block(L, nxt[0])
            elif nxt is not None and nxt[0] == indent and nxt[1].startswith("- "):
                val, _ = _parse_list(L, indent)
            else:
                val = None
            out[key] = val
        else:
            out[key] = _scalar(raw)
            # 续行（折叠标量）：把后续更深缩进的普通文本接上
            while True:
                nxt = L.peek()
                if nxt is None or nxt[0] <= indent or not _is_continuation(nxt):
                    break
                sep = "" if not out[key] else " "
                out[key] = (out[key] or "") + sep + nxt[1]
                L.i += 1


def load(text):
    """解析 YAML 文本，返回 Python 对象。"""
    L = _Lines(text)
    if not L.rows:
        return None
    indent = L.rows[0][0]
    val, _ = _parse_block(L, indent)
    return val


def load_file(path):
    with open(path, encoding="utf-8") as fh:
        return load(fh.read())
