# qg.sq004_riders_on_the_storm

## 基本信息

- Quest ID：`sq004_riders_on_the_storm`
- Quest title：`Riders on the Storm`
- 当前状态：`journal-located`
- 候选影响：`relationship` / `followup` / `ending`
- 当前置信度：`high`（任务级）；具体 fact 仍待验证

## 种子来源

- 来源：QuestGuide 1.5.0
- 来源位置：`QGEndingSideIds()` / `QGEndingReason()`
- 来源给出的候选理由：QuestGuide 将该任务归入会影响结局路线的任务集合。

> 这里只记录归一化后的候选结论，不复制 QuestGuide 的实现代码。

## Journal 定位

- questPath：`quests/side_quest/sq004_riders_on_the_storm`
- phases：
  - `quests/side_quest/sq004_riders_on_the_storm/01_camp`
  - `quests/side_quest/sq004_riders_on_the_storm/02_infiltration`
  - `quests/side_quest/sq004_riders_on_the_storm/03_escape`
- 后半段值得继续调查的 objectives：
  - `quests/side_quest/sq004_riders_on_the_storm/03_escape/sit_down` — Optional — Sit on the couch.
  - `quests/side_quest/sq004_riders_on_the_storm/03_escape/panam_talk` — Talk with Panam.
  - `quests/side_quest/sq004_riders_on_the_storm/03_escape/morning_after` — Talk with Panam.
  - `quests/side_quest/sq004_riders_on_the_storm/03_escape/return` — Talk with Panam.
- 是否已确认 Journal 数据：是
- 是否已确认运行时 path：尚未用实际存档验证

来源：REDmodding / CDPR `journal-quest-data.json`。

## 游戏逻辑证据

- `.quest`：待查
- `.questphase`：待查
- `.scene`：待查
- 写入的 Quest Fact：待查
- 后续读取位置：待查
- 因果链摘要：尚未达到 `logic-verified`；下一步必须从游戏资源确认具体对话选择写入了什么状态，以及后续任务/结局如何读取。

## 外部交叉验证

- REDmodding Quest IDs：确认根路径和任务名。
- REDmodding Journal JSON：确认 `01_camp` / `02_infiltration` / `03_escape` 与具体 objective 路径。
- PowerPyx Riders on the Storm：将本任务列为 Panam 后续任务链第一环，并标注沙发后的对话和次日 Panam 对话为关系线的重要选择。
- Cyberpunk Wiki：记录任务如果因离开过久而失败，会使后续 Panam jobs、romance 以及相关 ending route 不可用。
- PowerPyx Endings Guide：将本任务列为解锁 Panam ending route 的前置任务链之一。

## 当前研究判断

### 整个任务

存在较强证据表明：

- 完成本任务是 Panam 后续任务链的前置条件之一；
- 任务失败会切断后续任务；
- 因为后续链条与结局路线有关，因此候选影响包括 `followup` + `ending`；
- 任务后半段还包含关系线相关对话，因此同时候选 `relationship`。

### 具体阶段

当前已经进入 `stage-candidates.jsonl` 的阶段：

1. `03_escape/sit_down` → `important`：外部资料一致把坐下后的连续对话视为 Panam 关系线的重要阶段。
2. `03_escape/morning_after` → `notice`：次日对话还有一次关系信号选择。

`03_escape/panam_talk` / `03_escape/return` 仍保留在调查范围，但目前没有足够证据证明它们需要单独提示。任务失败触发点也不一定对应单一 objective，需要从 questphase / facts 定位。

这些仍只是研究候选，不能直接写进正式 `stageHints`；需要先找到游戏内部逻辑证据。

## 游戏内验收

- 测试游戏版本：待查
- 存档位置：待查
- A 路径：待查
- B 路径：待查
- 实际差异：待查
- 提示出现时机是否正确：待查

## 无剧透规则结论

### questImpacts

```json
null
```

### stageHints

```json
null
```

## 结论

- 最终状态：`journal-located`
- 是否进入 `data/hints.json`：否
- 下一步：从游戏 `.questphase` / `.scene` / Quest Fact 中定位任务失败条件，以及 `sit_down` / `panam_talk` 相关对话真正写入的状态。
