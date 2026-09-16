# 任务规则维护指南

这份文档专门记录 **Spoiler-Free Quest Hints** 中“大任务”和“子任务 / objective”应该如何添加、修改、验证和发布，避免再次出现“研究库里已经有，但 UI 没显示”或“只记得左侧大任务提示，忘了右侧子任务提示”的情况。

## 先记住：项目有两层 UI

本项目不是只有左侧任务列表提示。

### 大任务（Quest）

数据入口：`data/hints.json` → `questImpacts`

显示位置：

- Journal 左侧任务列表：`任务名  影响：人物关系 / 后续任务 / 结局条件`
- 正常游玩 HUD 的任务标题：同样显示 `影响：...`

运行时实现：

- `QuestListImpactAdapter.reds`
- `HudQuestTrackerAdapter.reds`
- `HintResolver.reds` 中的 `QOHResolveImpact()`
- `GeneratedRules.reds` 中的 `QOHResolveQuestImpactLabel()`

### 子任务 / Objective

数据入口：`data/hints.json` → `stageHints`

显示位置：

- Journal 右侧 objective 文本后面：`[值得留意]` / `[重要阶段]` / `[关键节点 · 建议存档]`
- 正常游玩 HUD 的 objective 文本后面：同样显示阶段提示

运行时实现：

- `JournalHintAdapter.reds`
- `HudQuestTrackerAdapter.reds`
- `HintResolver.reds` 中的 `QOHResolveLabel()`
- `GeneratedRules.reds` 中的 `QOHResolveExactObjectiveLabel()` / `QOHResolveQuestFallbackLabel()`

> 这个“右侧子任务提示”不是新想法。Git 历史里的 `feature/native-journal-objective-hints` 分支就已经实现过，并通过 PR #1 合并。当前 `master` 也仍然保留 `JournalHintAdapter.reds` 的 objective 级显示逻辑。

## 数据分层：研究库不等于游戏运行库

项目目前至少有三层数据：

1. `research/candidates.jsonl`
   - 大任务研究记录。
   - 记录 `questPath`、影响类型、证据、置信度、研究状态等。

2. `research/stage-candidates.jsonl`
   - 子任务 / objective 研究记录。
   - 记录 `objectivePath`、提示等级、证据、研究状态等。

3. `data/hints.json`
   - **真正的正式运行规则源**。
   - 游戏最终是否显示提示，以这里是否存在对应规则为准。

`GeneratedRules.reds` 是从 `data/hints.json` 生成的运行时代码，不应把 research 层当成游戏会自动读取的数据。

换句话说：

> **研究完成 ≠ 已经进入 UI。**
>
> 研究条目只有被晋升到 `data/hints.json`，再生成 `GeneratedRules.reds`，游戏里才会显示。

---

# 1. 如何添加任务

## 1.1 添加一个“大任务”提示

适用情况：希望整个任务在左侧列表 / HUD 标题上显示：

- `影响：人物关系`
- `影响：后续任务`
- `影响：结局条件`
- 或以上组合

### 第一步：确认研究记录

在：

`research/candidates.jsonl`

确认或新增该任务的研究条目，至少要有：

- `id`
- `questId`
- `questPath`
- `title`
- `suspectedImpacts`
- `status`
- `confidence`
- `sourceRef`
- `journalVerified`
- `externalCorroborated`

不要因为“这条人物线看起来很重要”就直接加正式规则；要确认确实属于当前支持的影响分类。

### 第二步：加入正式规则

编辑：

`data/hints.json`

在 `questImpacts` 中增加：

```json
{
  "id": "research.source.example",
  "questPath": "quests/.../example",
  "impacts": ["relationship"],
  "source": "research/candidates.jsonl"
}
```

允许的影响类型：

- `relationship` → 人物关系
- `followup` → 后续任务
- `ending` → 结局条件

可以组合：

```json
"impacts": ["relationship", "followup", "ending"]
```

### 第三步：生成运行时规则

不要手改 `GeneratedRules.reds` 作为长期做法。

运行：

```bash
python tools/generate_runtime_rules.py data/hints.json src/r6/scripts/SpoilerFreeQuestHints/GeneratedRules.reds
```

生成后，该任务应出现在：

`QOHResolveQuestImpactLabel()`

中。

### 第四步：验证

运行：

```bash
python tools/validate_hints.py data/hints.json
python -m unittest discover -s tests -v
```

实机重点检查：

- Journal 左侧任务列表
- HUD 任务标题

两处都应显示一致的 `影响：...`。

---

## 1.2 添加一个“子任务 / objective”提示

适用情况：不是整条任务都关键，而是其中某一步、某次对话、某个选择前需要提醒玩家。

例如：

- 某次对话会影响人物关系
- 某个选择会决定后续任务是否可用
- 某个阶段直接进入结局分支

### 第一步：确认 objectivePath

在：

`research/stage-candidates.jsonl`

确认或新增该阶段，最关键的是：

- `questPath`
- `objectivePath`
- `objectiveDescription`
- `suspectedLevel`
- `suspectedImpacts`

`objectivePath` 必须定位到**实际会显示在 Journal / HUD 的 JournalQuestObjective**。

不能只知道“某句对话有影响”，却把提示挂在错误的上一阶段或下一阶段。

### 第二步：选择提示等级

当前等级：

- `notice` → `值得留意`
- `important` → `重要阶段`
- `critical` → `关键节点 · 建议存档`

原则：

- 软性关系对白、额外互动：通常 `notice`
- 明确影响后续任务、关系线的重要选择：通常 `important`
- 直接大分岔、结局路线、非常适合提前存档的节点：`critical`

### 第三步：加入正式规则

编辑：

`data/hints.json`

在 `stageHints` 中增加：

```json
{
  "id": "research.stage.example",
  "questPath": "quests/.../example",
  "objectivePath": "quests/.../example/phase/objective",
  "level": "notice",
  "label": "值得留意",
  "source": "research/stage-candidates.jsonl"
}
```

### 第四步：生成运行时规则

运行：

```bash
python tools/generate_runtime_rules.py data/hints.json src/r6/scripts/SpoilerFreeQuestHints/GeneratedRules.reds
```

生成后应进入：

`QOHResolveExactObjectiveLabel()`

### 第五步：验证右侧 UI 和 HUD

实机必须检查两处：

1. Journal 右侧 objective：

```text
和某人交谈。  [值得留意]
```

2. 正常游玩 HUD objective：

```text
和某人交谈。  [值得留意]
```

如果左侧“大任务影响”已经显示，但右侧没有显示，不要先怀疑 UI hook。先检查：

- 当前 objective 是否真的是 `stageHints` 中那个 `objectivePath`
- objective 当前状态是否为 `Active`
- `objectivePath` 是否定位错了一层
- `data/hints.json` 是否真的包含该 stage rule
- 游戏目录里的 `GeneratedRules.reds` 是否还是旧版本

`QOHResolveLabel()` 当前只给 **Active objective** 返回提示。

---

# 2. 如何修改任务

## 2.1 修改“大任务”影响类型

例如原本：

```text
影响：人物关系
```

后来证据证明还会影响后续任务：

```text
影响：人物关系 / 后续任务
```

需要同步修改两处：

1. `research/candidates.jsonl`
   - 修正研究事实、来源、`suspectedImpacts`、notes 等。

2. `data/hints.json`
   - 修正对应 `questImpacts[].impacts`。

然后重新生成 `GeneratedRules.reds`，再跑校验和测试。

不要只改 `GeneratedRules.reds`，否则下一次生成会被覆盖。

## 2.2 修改“子任务 / objective”挂载位置

这是最容易出错的一类。

例如研究上知道：

> “是否陪竹村侦察”会产生人物关系差异。

但如果实际玩家看到的选择发生在另一个 objective，而规则却挂在：

`.../01_market/01c_sit_down`

那么 UI 就可能提前显示、延后显示，或者玩家当前选中的右侧 objective 根本看不到提示。

正确修改流程：

1. 在 `research/stage-candidates.jsonl` 修正 `objectivePath` 和说明。
2. 在 `data/hints.json` 修正对应 `stageHints[].objectivePath`。
3. 重新生成 `GeneratedRules.reds`。
4. 实机进入该任务阶段，确认**提示出现时机**。

如果只是改等级，例如 `notice` → `important`，同样要同步 research 和 `data/hints.json`。

## 2.3 修改提示文案

正式 UI 文案来自 `data/hints.json` 的 `label`，例如：

```json
"level": "important",
"label": "重要阶段"
```

如果以后统一改提示文案，需要同时检查：

- `tools/generate_runtime_rules.py`
- `tools/validate_hints.py`
- 测试文件
- README 中的等级说明

不要只改某一条生成出来的 `.reds`。

---

# 3. 大任务和子任务可以同时存在

一个任务完全可以同时有：

### Quest 级

```text
危险游戏  影响：人物关系
```

用于告诉玩家：

> 这整条任务里存在值得留意的人物关系内容。

### Objective 级

```text
和竹村核对一下计划。  [值得留意]
```

用于告诉玩家：

> 真正应该开始注意选择的是这个具体阶段。

这两层不是重复，而是不同粒度：

- Quest 级回答“这条任务会影响什么？”
- Objective 级回答“什么时候开始需要留意？”

维护规则时，不能因为已经有 Quest 级提示，就省略已经定位清楚的 Objective 级提示。

---

# 4. 运行时链路

完整链路如下：

```text
research/candidates.jsonl
research/stage-candidates.jsonl
        ↓ 人工复核 / 晋升
     data/hints.json
        ↓ generate_runtime_rules.py
     GeneratedRules.reds
        ↓
  HintResolver.reds
   ↙            ↘
Quest 级       Objective 级
   ↓              ↓
左侧 Journal     右侧 Journal
HUD 任务标题     HUD objective
```

对应 UI Adapter：

```text
QuestListImpactAdapter.reds
  → Journal 左侧大任务

JournalHintAdapter.reds
  → Journal 右侧子任务 / objective

HudQuestTrackerAdapter.reds
  → HUD 大任务 + HUD 子任务
```

---

# 5. 发布前必须做的检查

每次新增或修改规则后至少完成：

```bash
python tools/validate_hints.py data/hints.json
python -m unittest discover -s tests -v
python tools/generate_runtime_rules.py data/hints.json src/r6/scripts/SpoilerFreeQuestHints/GeneratedRules.reds
```

然后确认：

- `GeneratedRules.reds` 与 `data/hints.json` 同步
- 游戏目录里的 6 个 runtime `.reds` 已更新
- 如果通过 Vortex 安装，Vortex staging / deploy 的版本不是旧 Release
- 完全退出并重启游戏，让 redscript 重新编译
- 大任务左侧 UI 正常
- 子任务右侧 UI 正常
- HUD 大任务正常
- HUD objective 正常

如果仓库正确、游戏 UI 却仍显示旧规则，优先对比：

```text
仓库 GeneratedRules.reds 的 SHA256
游戏目录 GeneratedRules.reds 的 SHA256
```

哈希不一致时，先解决部署版本问题，不要继续误判规则逻辑。

---

# 6. 维护时的硬规则

1. **Research 不是 Runtime。** 研究完成后必须检查是否已晋升到 `data/hints.json`。
2. **大任务和子任务是两套规则。** `questImpacts` 与 `stageHints` 都要分别检查。
3. **右侧子任务提示是正式功能，不是临时测试。** 不要只验证左侧任务名。
4. **不要长期手改 `GeneratedRules.reds`。** 正式源是 `data/hints.json`。
5. **修改 objective 规则时最重要的是出现时机。** 路径“存在”不代表路径“挂得对”。
6. **实机验证必须看四处 UI：左侧 Journal、右侧 Journal、HUD 标题、HUD objective。**
7. **发布 Release 前确认 ZIP 内文件哈希与当前仓库一致。**
8. **游戏已启动时替换 `.reds` 不代表立即生效。** 必须完整重启游戏。
