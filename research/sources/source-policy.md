# 剧情影响数据源策略

本项目的目标是给玩家提供无剧透的“这里值得留意”提示，不是建立逐节点的游戏逻辑考古数据库。

## 入库最低证据标准

一条剧情影响规则至少需要：

1. 一个高质量来源明确说明该任务/选择会造成持续影响，影响必须能归入：`relationship`、`followup`、`ending`；
2. CDPR / REDmodding Journal 数据能够把任务或关键阶段定位到稳定的 questPath / objectivePath；
3. 正式发布前在游戏中确认提示挂载时机正确。

不再要求常规规则逐条追踪 `.scene`、`.questphase`、Quest Fact Set/Condition。只有来源冲突、关键 objective 无法判断、或需要排除误报时才进入游戏资源层。

## 当前主要资料

### 第一方 / 官方优先

若 CDPR 官方资料明确说明某一选择影响后续、关系或结局，优先采用。

### PowerPyx Story Choices Guide

用途：基础游戏主线的“长期影响选择”筛选。

它明确区分长期后果与仅改变下一句对白的普通选择，因此适合作为候选发现和剧情后果证据源。重点覆盖 The Pickup、The Heist、I Walk the Line、Search and Destroy、Nocturne Op55N1 等。

### PowerPyx Romance Guides / 单任务 Walkthroughs

用途：Panam、Judy、River、Kerry 等关系线和对应后续任务解锁条件。

只采纳其明确标成 important / romance-defining / next quest unavailable / questline failed 等具有持续影响的阶段，不把纯推荐、风味对白或“可能重要”自动升级为正式规则。

### PowerPyx Endings Guide

用途：基础游戏结局路线的前置任务、Point of No Return、隐藏结局条件。

### PowerPyx Phantom Liberty Walkthrough / Trophy Roadmap

用途：DLC 结局分支。其路线说明明确指出 Firestarter 是主要 ending path split；此前绝大多数决定不会改变 DLC endings。

### REDmodding Quest IDs + journal-quest-data.json

用途：内部路径定位。负责 questPath / phase / objectivePath / description，不单独证明剧情后果。

### QuestGuide 1.5.0

用途：候选种子和优先级排序。只保存归一化后的任务知识，不复制插件源码、资产或 UI 文案。

## 规则强度

- `notice`：有持续影响，但通常只是关系表现、较轻的后续差异，或适合作为温和提醒。
- `important`：明确影响关系线、后续任务是否出现、任务链是否继续，或造成明显持续后果。
- `critical`：Point of No Return、直接决定重要结局路线、隐藏结局资格，或高度适合提前存档的不可逆节点。

## 误报控制

如果成熟来源明确写明“choices do not matter / only changes dialogue / no effect on progression”，默认不创建 stage hint。任务若只是整个链条的必要前置，可以保留 quest-level `followup`，但不应给其中普通对白乱加 `[重要阶段]`。
