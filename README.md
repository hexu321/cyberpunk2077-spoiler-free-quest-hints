# Cyberpunk 2077 Spoiler-Free Quest Hints

一个面向《赛博朋克 2077》的“无剧透剧情重要性提示”Mod 项目。

目标不是告诉玩家“选哪个”“会发生什么”或“哪个结局最好”，而是在原生任务日志附近，用极少的信息提醒玩家：**当前任务 / 当前 objective 是否值得特别留意**。

## 设计目标

- **无剧透优先**：不显示结局名称、角色去向、奖励、死亡/存活、阵营结果或推荐选项。
- **按当前 objective 判断**：同一个大任务可以包含多个连续的小步骤；提示不能只固定在整条 Quest 上，而要能随着当前 objective 变化。
- **原生 Journal UI 优先**：最终目标是在游戏原生 Journal / 任务详情附近显示简短标签，而不是额外弹窗或攻略窗口。
- **手柄友好**：不新增必须依赖键盘的操作。
- **数据与 UI 分离**：剧情重要性规则独立于 UI Hook，便于校对和长期维护。
- **保守提示**：证据不足时宁可不提示，不猜测“这个选项影响结局”。

## 提示等级

| 等级 | 建议显示 | 含义 |
| --- | --- | --- |
| `none` | 不显示 | 普通推进，不需要额外提醒 |
| `notice` | `值得留意` | 当前阶段可能有后续影响，但不需要打断游玩 |
| `important` | `重要阶段` | 建议认真看当前剧情/目标，不要机械跳过 |
| `critical` | `关键节点 · 建议存档` | 当前阶段存在较强的长期影响证据，但仍不告诉玩家具体后果 |

> 这些标签只描述“重要性”，不描述“正确答案”。

## 当前状态

**Milestone 1：原生 Journal + HUD 技术底座已验证，正在扩充真实规则库。**

已经完成并在实际游戏环境验证：

- Journal 左侧任务列表可显示整条任务的 `影响：……` 摘要。
- Journal 右侧 objective 可按当前 active objective 显示重要性标签。
- 正常游玩 HUD 的任务标题和 objective 同样支持对应提示。
- 运行时使用真实 Journal path，不依赖中英文任务标题做匹配。
- `data/hints.json` 使用两层规则：`questImpacts` 负责总任务影响类型，`stageHints` 负责具体阶段重要性。
- 规则经 Python 校验并生成 `GeneratedRules.reds`，再由 redscript 编译进游戏。
- QuestGuide 只作为交互/API 研究参考，不复制其源码、资产或打包文件。

仍在进行：

- 扩充并人工复核真实剧情规则数据库。
- 用对应存档逐条验证 exact objective 规则只在目标阶段显示。
- 可安装 release / Vortex 打包。

## 仓库结构

```text
data/
  hints.json             # 经人工复核的真实规则
  hints.schema.json      # 两层规则文件约束
  hints.example.json     # 无剧情内容的示例

docs/
  architecture.md        # 运行时架构与 UI 方向
  spoiler-policy.md      # 什么能写、什么不能写
  research-notes.md      # 已验证资料和待验证问题

research/
  candidates.jsonl       # 候选剧情影响研究队列；不会直接进游戏
  cases/                 # 单任务详细调查记录
  sources/               # 归一化后的来源快照/种子数据

tools/
  validate_hints.py                # 正式规则离线校验
  generate_runtime_rules.py        # JSON -> GeneratedRules.reds
  validate_research_candidates.py  # 研究候选 JSONL 校验

src/
  r6/scripts/SpoilerFreeQuestHints/
    GeneratedRules.reds          # 自动生成的运行时规则
    HintResolver.reds            # 任务影响 / objective 提示解析
    JournalHintAdapter.reds      # Journal 右侧 objective 提示
    QuestListImpactAdapter.reds  # Journal 左侧总任务影响
    HudQuestTrackerAdapter.reds  # 正常游玩 HUD 提示
    JournalPath.reds             # Journal path 构建与归属 quest 查找
```

## 开发原则

1. 先验证游戏 API，再写 Hook。
2. 每一条 `critical` 规则必须有来源和人工复核记录。
3. 数据中禁止保存“推荐选项”“结局名字”“谁会死”等直接剧透字段。
4. UI 只显示当前玩家已经到达的任务阶段对应标签。
5. 不扫描未解锁剧情并把未来内容暴露给玩家。

## 目标运行环境

研究阶段以 2026 年社区文档中常用的 Windows 基线为参考：Cyberpunk 2077 2.31/2.31a、RED4ext、redscript 0.5.31。最终 release 前仍需在用户实际安装版本上验证。

## 项目边界

这个项目不是剧情攻略，也不是结局选择器。它更像游戏里的一个“谨慎提醒层”：

> **“这一步值得你认真一点。”**

然后把选择权完整留给玩家。
