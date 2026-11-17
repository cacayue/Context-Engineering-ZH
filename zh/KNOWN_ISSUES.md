# 已知失效链接（上游问题）

本文件记录**上游仓库既有**的失效内部链接，共 **36 条**。它们不是本次中文化引入的，
而是 `base_commit: 6158def` 时点上游本身的状态。

用途有两个：

1. **审计留痕**：让后来者知道这些链接为什么在 `zh/` 里也点不开。
2. **G5 白名单**：`zh/tools/check.py` 的 G5（相对链接可达性）从本文件 `## 明细` 表第 2 列读取白名单，
   命中即跳过，不算 FAIL。**除本表之外**新增的失效链接一律 FAIL。
   明细 36 行，但 `../../.github/CONTRIBUTING.md` 在两个文件里重复出现，
   按 href 去重后白名单为 **35 条**——G5 按 href 匹配，不受行数影响。

修复原则见 `zh/STYLE.md` R7：翻译时把内部链接改为 `zh/` 内可达路径；
上游本身就断的链接，保留原目标并在译文里加脚注说明「上游已失效」，**不要静默删链接**。

## 统计

| 源文件 | 条数 |
|---|---:|
| `20_templates/README.md` | 8 |
| `40_reference/README.md` | 8 |
| `60_protocols/README.md` | 5 |
| `60_protocols/digests/README.md` | 5 |
| `60_protocols/digests/attractor.co.emerge.digest.md` | 3 |
| `cognitive-tools/cognitive-templates/composition.md` | 2 |
| `00_COURSE/05_memory_systems/README.md` | 1 |
| `00_COURSE/07_multi_agent_systems/03_emergent_behaviors.md` | 1 |
| `00_COURSE/09_evaluation_methodologies/00_evaluation_frameworks.md` | 1 |
| `cognitive-tools/README.md` | 1 |
| `cognitive-tools/cognitive-programs/basic-programs.md` | 1 |
| **合计** | **36** |

## 明细

列说明：**源文件** = 出现失效链接的文件（仓库根相对）；**失效链接** = Markdown 里写的原始 href
（G5 白名单按此列精确匹配）；**行** = 该链接在源文件中的行号；**类型/建议** = 成因与修法。

| 源文件 | 失效链接 | 行 | 类型 | 建议 |
|---|---|---:|---|---|
| `00_COURSE/05_memory_systems/README.md` | `03_reconstructive_memory.md` | 190 | 重命名 | 改为 `04_reconstructive_memory.md` |
| `00_COURSE/07_multi_agent_systems/03_emergent_behaviors.md` | `../08_field_integration/` | 2814 | 重命名 | 目录已改名，改为 `../08_field_theory_integration/` |
| `00_COURSE/09_evaluation_methodologies/00_evaluation_frameworks.md` | `10_orchestration_capstone.md` | 2544 | 缺失 | 该文件从未提交，改为指回 `README.md` 或删除链接 |
| `20_templates/README.md` | `./resonance_measurement.py` | 106 | 缺失 | 脚本未提交；改为指向 `field_resonance_measure.py` |
| `20_templates/README.md` | `./attractor_detection.py` | 107 | 缺失 | 脚本未提交；译文保留文字、去掉链接或加脚注 |
| `20_templates/README.md` | `./symbolic_residue_tracker.py` | 108 | 缺失 | 同上 |
| `20_templates/README.md` | `./meta_recursive_patterns.py` | 116 | 缺失 | 同上 |
| `20_templates/README.md` | `./unified_field_engine.py` | 117 | 缺失 | 同上 |
| `20_templates/README.md` | `./interpretability_scaffolding.py` | 118 | 缺失 | 同上 |
| `20_templates/README.md` | `./collaborative_evolution_framework.py` | 119 | 缺失 | 同上 |
| `20_templates/README.md` | `./cross_modal_context_bridge.py` | 120 | 缺失 | 同上 |
| `40_reference/README.md` | `./boundary_operations.md` | 137 | 缺失 | 该参考页未提交；加脚注「上游已失效」 |
| `40_reference/README.md` | `./quantum_semantic_metrics.md` | 143 | 缺失 | 同上 |
| `40_reference/README.md` | `./unified_field_operations.md` | 144 | 缺失 | 同上 |
| `40_reference/README.md` | `./meta_recursive_patterns.md` | 145 | 缺失 | 同上 |
| `40_reference/README.md` | `./interpretability_metrics.md` | 146 | 缺失 | 同上 |
| `40_reference/README.md` | `./collaborative_evolution_guide.md` | 147 | 缺失 | 同上 |
| `40_reference/README.md` | `./cross_modal_context_handbook.md` | 148 | 缺失 | 同上 |
| `40_reference/README.md` | `../../.github/CONTRIBUTING.md` | 295 | 层级 | 仓库根无 `.github/CONTRIBUTING.md`；改为 `../CONTRIBUTING.md`（若存在）或删链接 |
| `60_protocols/README.md` | `../../00_foundations/08_neural_fields_foundations.md` | 360 | 层级 | 多了 `../`，改为 `../00_foundations/08_neural_fields_foundations.md` |
| `60_protocols/README.md` | `../../00_foundations/11_emergence_and_attractor_dynamics.md` | 361 | 层级 | 同上，去掉一层 `../` |
| `60_protocols/README.md` | `../../00_foundations/12_symbolic_mechanisms.md` | 362 | 层级 | 同上 |
| `60_protocols/README.md` | `../../20_templates/field_resonance_measure.py` | 363 | 层级 | 同上 |
| `60_protocols/README.md` | `../../70_agents/01_residue_scanner/` | 364 | 缺失 | 目录不存在；加脚注 |
| `60_protocols/digests/README.md` | `./recursive.emergence.digest.md` | 60 | 缺失 | digest 未提交；`digests/` 下只有 `attractor.co.emerge.digest.md` |
| `60_protocols/digests/README.md` | `./recursive.memory.digest.md` | 61 | 缺失 | 同上 |
| `60_protocols/digests/README.md` | `./field.resonance.digest.md` | 62 | 缺失 | 同上 |
| `60_protocols/digests/README.md` | `./field.self_repair.digest.md` | 63 | 缺失 | 同上 |
| `60_protocols/digests/README.md` | `./context.memory.digest.md` | 64 | 缺失 | 同上 |
| `60_protocols/digests/attractor.co.emerge.digest.md` | `../shells/attractor.co.emerge.shell` | 116 | 扩展名 | 缺 `.md`，改为 `../shells/attractor.co.emerge.shell.md` |
| `60_protocols/digests/attractor.co.emerge.digest.md` | `../../../00_foundations/11_emergence_and_attractor_dynamics.md` | 117 | 层级 | 多了 `../`，改为 `../../00_foundations/11_emergence_and_attractor_dynamics.md` |
| `60_protocols/digests/attractor.co.emerge.digest.md` | `../../../20_templates/field_resonance_measure.py` | 118 | 层级 | 同上，去掉一层 `../` |
| `cognitive-tools/README.md` | `../../.github/CONTRIBUTING.md` | 180 | 层级 | 仓库根无该文件；删链接或改为 `../CONTRIBUTING.md` |
| `cognitive-tools/cognitive-programs/basic-programs.md` | `./program-examples.ipynb` | 828 | 缺失 | notebook 未提交；加脚注 |
| `cognitive-tools/cognitive-templates/composition.md` | `../integration/with-rag.md` | 596 | 缺失 | `integration/` 目录不存在；加脚注 |
| `cognitive-tools/cognitive-templates/composition.md` | `../integration/with-memory.md` | 596 | 缺失 | 同上 |

## 复现方法

```bash
python zh/tools/check.py --module M7      # 含 G5；白名单命中不报错
python zh/tools/check.py --all            # 全量
```

想复算这 36 条（不经 G5），对每个源文件跑一遍链接存在性检查即可；
判据是「相对 href 规范化后目标不存在」。

## 状态

| 状态 | 含义 |
|---|---|
| `open` | 上游未修，本表全部为 `open` |
| `fixed-upstream` | 上游已修 → 从本表删除，G5 随之收紧 |
| `fixed-downstream` | `zh/` 译文里已改为可达路径 → 该行可移除（R7） |

本表 36 行当前全部为 `open`。上游若修复，请同步删行；`zh/manifest.json` 的
`base_commit` 变化时，应整表重扫。
