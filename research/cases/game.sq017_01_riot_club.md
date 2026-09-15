# game.sq017_01_riot_club

## 基本信息

- Quest ID：`sq017_01_riot_club`
- Quest title：`I Don't Wanna Hear It`
- 当前状态：`logic-verified`
- 候选影响：`followup`
- 当前置信度：`high`

## 候选来源

这一条不是来自 QuestGuide 的 ending 白名单，而是在扩展研究 Kerry / Us Cracks 任务链时发现的“纯后续任务影响”案例。

外部资料把 `Every Breath You Take` 描述为需要此前与 Us Cracks 达成可继续合作的结果，并在相关 Kerry 任务链推进后触发；这只作为交叉验证，最终判断以游戏资源为主。

## Journal 定位

- questPath：`quests/side_quest/sq017_01_riot_club`
- 关键 objective：`quests/side_quest/sq017_01_riot_club/nightclub/talk_us_cracks`
- objective 文本：`Talk to Us Cracks.`
- 后续任务：`quests/minor_quest/mq028_stalker`（Every Breath You Take）

## 游戏逻辑证据

从用户当前安装的 `basegame_4_gamedata.archive` 只读提取：

### 1. 具体对话 Scene

`base\quest\side_quests\sq017\scenes\sq017_10_us_crack_intro.scene`

直接包含：

- Journal objective `.../nightclub/talk_us_cracks`
- `scnChoiceNode`
- `questFactsDBManagerNodeDefinition`
- `questFactsDBCondition`
- `sq017_us_cracks_no_deal`
- `end_no_deal`

说明这段对话本身会产生可供后续逻辑读取的 Us Cracks 结果状态。

### 2. sq017 收尾逻辑

`base\quest\side_quests\sq017\phases\sq017_cleanup.questphase`

同一 phase 中同时包含：

- `questFactsDBCondition`
- `questFactsDBManagerNodeDefinition`
- `sq017_us_cracks_no_deal`
- `sq017_mq028_start`

失败收尾 `sq017_fail_cleanup.questphase` 中没有这组桥接关系。

这证明正常收尾时，游戏会依据 Us Cracks 结果状态进入 FactsDB 条件逻辑，并写入专门指向 mq028 的桥接状态。

### 3. 后续任务内部 ID

用户安装的游戏资源中存在：

- `base\quest\minor_quests\mq028\mq028.quest`
- `base\quest\minor_quests\mq028\mq028.questphase`

Journal / REDmodding 任务 ID 映射把 `mq028_stalker` 对应到 `Every Breath You Take`。

## 因果链

```text
I Don't Wanna Hear It
  -> nightclub/talk_us_cracks
  -> Us Cracks 对话 ChoiceNode
  -> sq017_us_cracks_no_deal 等结果状态
  -> sq017_cleanup.questphase 条件判断
  -> sq017_mq028_start
  -> mq028 / Every Breath You Take 后续任务链
```

因此这条适合我们的：

- questImpact：`followup`
- stageHint：`important`

## 游戏内验收

- 测试游戏版本：待实测确认
- 真实存档 A/B：待测试
- 提示时机：待测试

## 无剧透规则建议

### questImpacts

```json
{
  "questPath": "quests/side_quest/sq017_01_riot_club",
  "impacts": ["followup"]
}
```

### stageHints

```json
{
  "questPath": "quests/side_quest/sq017_01_riot_club",
  "objectivePath": "quests/side_quest/sq017_01_riot_club/nightclub/talk_us_cracks",
  "level": "important"
}
```

## 结论

- 当前状态：`logic-verified`
- 是否进入正式 `data/hints.json`：暂不进入
- 剩余门槛：游戏内实际到达该 objective，确认 `[重要阶段]` 的显示时机自然且没有提前剧透，然后再升 `in-game-verified / ready`。
