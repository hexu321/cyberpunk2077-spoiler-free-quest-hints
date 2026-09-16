# Research workspace

这个目录用于维护“可能影响剧情的任务/阶段”的研究过程，不直接驱动游戏运行时。

## 目录职责

```text
research/
├─ candidates.jsonl                  # 一行一个候选大任务；机器可读的研究队列
├─ stage-candidates.jsonl            # 精确到 objective 的候选提示阶段
├─ cases/                            # 单个候选的详细调查记录
│  └─ TEMPLATE.md
└─ sources/
   ├─ questguide-1.5.0-seed.json     # 从本地 QuestGuide 1.5.0 归一化出的种子集合
   ├─ redmodding-quest-roots.json    # 已确认的官方 questPath / title 根信息
   ├─ source-policy.md               # 剧情影响来源、证据门槛与误报控制
   └─ guide-coverage-audit.md        # 已扫攻略平台、覆盖区域与明确排除项
```

正式进入游戏的规则仍然只来自：

```text
data/hints.json
```

研究队列中的候选在完成核验前，不得自动进入 `data/hints.json`。

## 候选状态

默认按下面的顺序推进：

```text
candidate
  -> source-verified
  -> journal-located
  -> in-game-verified
  -> ready
  -> shipped
```

含义：

- `candidate`：已有线索认为值得调查，但还没有达到入库证据标准。
- `source-verified`：至少一个高质量、系统性资料明确说明该任务/选择会造成 `relationship` / `followup` / `ending` 之一的持续影响。官方资料有明确说明时优先使用；官方没有完整选择后果表时，可使用长期维护且明确覆盖 lasting consequences 的成熟攻略/Wiki。
- `journal-located`：已经用 CDPR / REDmodding Journal 数据确认稳定的 questPath / phase / objectivePath，可把提醒挂到具体游戏阶段。
- `in-game-verified`：已在真实游戏里确认提示出现位置和时机正确；不要求为了入库再做 A/B 剧情实验。
- `ready`：证据足够，可进入 `data/hints.json`。
- `shipped`：已经随正式规则发布。
- `logic-verified`：保留给过去已经完成的 `.scene` / `.questphase` / Quest Fact 级验证，属于比 `source-verified` 更强的可选附加证据，**不再是新规则的必经门槛**。

## 数据源优先级

1. **CDPR / 官方第一方说明**：只要明确说明某个选择影响关系、后续内容或结局，就直接作为高优先级剧情证据。
2. **系统性成熟攻略 / Wiki**：用于覆盖官方没有提供完整选择后果表的部分。优先选择明确区分“长期影响”和“仅改变一句对白”的资料；基础游戏目前以 PowerPyx Story Choices / Romance / Endings 系列作为主要筛选源之一。
3. **CDPR / REDmodding Journal 数据**：负责确认 quest ID、questPath、phase、objectivePath 和 objective 描述；它负责“挂在哪里”，不负责单独判断剧情后果。
4. **本地 QuestGuide 1.5.0**：作为人工筛过的高价值候选种子，不作为唯一事实来源。
5. **游戏内实际触发**：最终检查提示是否出现在正确阶段、是否过早/过晚。
6. **游戏真实资源 / Quest Fact**：仅在来源互相矛盾、objective 无法准确定位或需要排疑时使用，不再作为常规入库要求。

## QuestGuide 使用边界

本地参考源码位于被 Git 忽略的：

```text
references/QuestGuide-1.5.0/
```

只允许用它来识别“哪些任务值得调查”和理解公开可观察的分类思路；不要复制其实现、源码块、资产或 UI 文本到本项目。

当前 `sources/questguide-1.5.0-seed.json` 只保存我们自己归一化后的任务 ID、候选影响类型和来源位置，不保存 QuestGuide 的实现代码。

## 候选记录原则

- `suspectedImpacts` 只是“待验证影响类型”，不是正式结论。
- 不在研究队列中记录推荐选项、角色命运、结局名称等玩家可见剧透字段。
- 能定位到具体 objective 时，优先把阶段提示缩窄到 `stage-candidates.jsonl`，而不是整条 quest fallback。
- 大任务重要不等于每个 objective 都重要。若任务只是后续链路前置、内部选项本身无后果，则保留 quest-level `followup`，不创建 stage candidate。
- `critical` 优先用于不可逆、直接改变重要后续/结局资格或非常适合提前存档的阶段；普通人物关系选择默认用 `important` / `notice`。
- 如果后续证据推翻候选，保留调查记录并标记为 `rejected` / 在 notes 中说明，而不是悄悄删除研究历史。
