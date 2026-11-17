"""模块与任务映射（任务卡 §4 §5）。

纯函数，按序匹配，首个命中即采用。被 manifest.py / check.py / progress.py 复用。
"""

import os
import re

MODULES = ["M1", "M2", "M3", "M4", "M5", "M6", "M7", "M8", "M9", "M10", "M11"]

# 模块名（PROGRESS.md §1 的「名称」列）
MODULE_NAMES = {
    "M0": "基础设施",
    "M1": "入口层",
    "M2": "概念地基",
    "M3": "课程·基础",
    "M4": "课程·进阶",
    "M5": "课程·前沿",
    "M6": "工程资产",
    "M7": "参考手册",
    "M8": "无代码",
    "M9": "认知架构",
    "M10": "研究篇",
    "M11": "空目录写作",
}

# 任务名（PROGRESS.md §2 的「名称」列）
TASK_NAMES = {
    "M1-01": "根文档",
    "M1-02": "仓库手册",
    "M1-03": "结构说明",
    "M1-04": "大师课 8 篇",
    "M1-05": "导航页",
    "M2-01": "原子与分子",
    "M2-02": "细胞与器官",
    "M2-03": "工具与编程",
    "M3-01": "数学基础",
    "M3-02": "检索与生成",
    "M3-03": "上下文处理",
    "M3-04": "上下文管理",
    "M4-01": "RAG",
    "M4-02": "记忆系统",
    "M4-03": "工具推理",
    "M5-01": "多智能体",
    "M5-02": "场论集成",
    "M5-03": "评估方法",
    "M5-04": "编排毕业设计",
    "M6-01": "模板库",
    "M6-02": "协议壳",
    "M6-03": "零到一指南",
    "M6-04": "示例工程",
    "M6-05": "命令集",
    "M7-01": "检索与索引",
    "M7-02": "残差与涌现",
    "M7-03": "吸引子与场",
    "M7-04": "模式与预算",
    "M7-05": "Schema 与索引",
    "M8-01": "基础篇",
    "M8-02": "心智模型",
    "M8-03": "实用协议",
    "M8-04": "场域技法",
    "M8-05": "高级集成",
    "M9-01": "架构总览",
    "M9-02": "模式与模板",
    "M9-03": "程序库",
    "M10-01": "场论与符号",
    "M10-02": "统一场论与语义",
    "M10-03": "证据与安全",
    "M10-04": "播客与 CI",
    "M11-01": "空目录写作",
}

ROOT_DOCS = [
    "README.md",
    "CLAUDE.md",
    "GEMINI.md",
    "Complete_Guide.md",
    "CITATIONS.md",
    "CITATIONS_v2.md",
    "CITATIONS_v3.md",
]

FOUNDATION_RE = re.compile(r"^00_foundations/(\d{2})_")


def _course_num(src):
    """00_COURSE/NN_... 的 NN，非课程文件返回 None。"""
    m = re.match(r"^00_COURSE/(\d{2})_", src)
    return int(m.group(1)) if m else None


def _foundation_num(src):
    m = FOUNDATION_RE.match(src)
    return int(m.group(1)) if m else None


def module_of(src):
    """任务卡 §4 模块映射，按序首个命中。"""
    if src in ROOT_DOCS:
        return "M1"
    if src.startswith("STRUCTURE/") or src.startswith("masterclass_content/"):
        return "M1"
    if src in ("00_foundations/README.md", "00_COURSE/README.md", "30_examples/README.md"):
        return "M1"
    fn = _foundation_num(src)
    if fn is not None and 1 <= fn <= 7:
        return "M2"
    cn = _course_num(src)
    if cn is not None and 0 <= cn <= 3:
        return "M3"
    if cn is not None and 4 <= cn <= 6:
        return "M4"
    if cn is not None and 7 <= cn <= 10:
        return "M5"
    if src.startswith(("20_templates/", "60_protocols/", ".claude/",
                       "10_guides_zero_to_hero/", "30_examples/")):
        return "M6"
    if src.startswith("40_reference/"):
        return "M7"
    if src.startswith("NOCODE/"):
        return "M8"
    if src.startswith("cognitive-tools/"):
        return "M9"
    if fn is not None and 8 <= fn <= 14:
        return "M10"
    if src.startswith(("00_EVIDENCE/", "SECURITY_RESEARCH/", "PODCASTS/", ".github/")):
        return "M10"
    if src.startswith(("50_contrib/", "70_agents/", "80_field_integration/", "context-schemas/")):
        return "M11"
    return "M11"


def task_of(src, module=None):
    """任务卡 §5 任务映射，按序首个命中。"""
    module = module or module_of(src)
    base = src.rsplit("/", 1)[-1]

    if module == "M1":
        if src in ("CLAUDE.md", "GEMINI.md"):
            return "M1-02"
        if src in ROOT_DOCS:
            return "M1-01"
        if src.startswith("STRUCTURE/"):
            return "M1-03"
        if src.startswith("masterclass_content/"):
            return "M1-04"
        return "M1-05"

    if module == "M2":
        n = _foundation_num(src) or 0
        if n in (1, 2):
            return "M2-01"
        if n in (3, 4):
            return "M2-02"
        return "M2-03"

    if module == "M3":
        return "M3-0%d" % (min(4, (_course_num(src) or 0) + 1))

    if module == "M4":
        return "M4-0%d" % ((_course_num(src) or 4) - 3)

    if module == "M5":
        return "M5-0%d" % ((_course_num(src) or 7) - 6)

    if module == "M6":
        if src.startswith("20_templates/"):
            return "M6-01"
        if src.startswith("60_protocols/"):
            return "M6-02"
        if src.startswith("10_guides_zero_to_hero/"):
            return "M6-03"
        if src.startswith("30_examples/"):
            return "M6-04"
        return "M6-05"

    if module == "M7":
        if base != "README.md" and re.search(r"(retrieval|latent)", base):
            return "M7-01"
        if re.search(r"(residue|emergence)", base):
            return "M7-02"
        if re.search(r"(attractor|field_mapping)", base):
            return "M7-03"
        # M7-05 = README.md 及 *schema*；其余（pattern*/token_budgeting*/eval_checklist）归 M7-04
        if base == "README.md" or "schema" in base:
            return "M7-05"
        return "M7-04"

    if module == "M8":
        if src.startswith("NOCODE/00_foundations/"):
            return "M8-01"
        if src.startswith("NOCODE/10_mental_models/"):
            return "M8-02"
        if src.startswith("NOCODE/20_practical_protocols/"):
            return "M8-03"
        if src.startswith(("NOCODE/30_field_techniques/", "NOCODE/40_protocol_design/")):
            return "M8-04"
        return "M8-05"

    if module == "M9":
        if src.startswith("cognitive-tools/cognitive-schemas/") or src.startswith(
            "cognitive-tools/cognitive-templates/"
        ):
            return "M9-02"
        if src.startswith("cognitive-tools/cognitive-programs/"):
            return "M9-03"
        return "M9-01"

    if module == "M10":
        n = _foundation_num(src) or 0
        if n in (8, 9, 11, 12):
            return "M10-01"
        if n in (10, 13, 14):
            return "M10-02"
        if src.startswith(("00_EVIDENCE/", "SECURITY_RESEARCH/")):
            return "M10-03"
        return "M10-04"

    return "M11-01"


def walk_sources(root="."):
    """枚举仓库根下的源 .md（排除 zh/ 与 .git/），返回仓库根相对 posix 路径，字典序。"""
    out = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if d not in (".git", "zh", "node_modules"))
        for fn in filenames:
            if not fn.endswith(".md"):
                continue
            full = os.path.join(dirpath, fn)
            rel = os.path.relpath(full, root).replace(os.sep, "/")
            out.append(rel)
    out.sort()
    return out


def target_of(src):
    return "zh/" + src
