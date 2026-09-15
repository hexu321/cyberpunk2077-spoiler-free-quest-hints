# qg.sq031_rogue — Chippin' In

## 当前判断

- 状态：`journal-located`
- 候选影响：`followup` / `ending`
- 置信度：高
- 这是当前最优先的 scene/fact 核验对象之一。

## Journal 定位

关键 phase：`quests/side_quest/sq031_rogue/grave`

候选 objective：

- `grave/04_sit_grave` — Sit next to Johnny.
- `grave/06_talk_to_johnny` — Talk to Johnny.

CDPR Journal 数据确认以上路径。

## 外部交叉验证

Cyberpunk Wiki 与 PowerPyx Ending/Chippin' In 指南一致指出：油田墓地与 Johnny 的特定对话序列会改变隐藏结局资格，并会影响 Rogue 后续任务是否出现。

因此本任务不是“完成即可”那么简单，而是存在真实的选择敏感阶段。

## 游戏资源 fact 证据

RedSync 的 `sq031` quest/questphase fact 集合中确认存在专门的墓地阶段状态：

- `sq031_03_ch_grave`
- `sq031_05_grave`
- `sq031_05_grave_in`
- `sq031_05_sm_grave`
- `sq031_05_follow_up_in`
- `sq031_06_rogue_call`

这些事实名进一步证明墓地并不是纯演出段，而是独立的任务状态阶段。不过当前 RedSync 的 quest-only fact dump 中没有直接定位到社区常提到的隐藏结局资格 fact，因此仍不能仅凭这份 dump 完成内部因果证明。

## 阶段提示候选

- `grave/04_sit_grave` → `critical`：作为进入关键对话前的提前警告。
- `grave/06_talk_to_johnny` → `critical`：覆盖真正的选择序列。

## 下一步

从 `sq031` 对应 `.scene/.questphase` 中找到墓地对话真正写入的状态，并追踪 Nocturne/隐藏结局条件的读取。达到该证据后才升级到 `logic-verified`。
