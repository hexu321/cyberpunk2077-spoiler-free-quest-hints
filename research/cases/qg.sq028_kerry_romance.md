# qg.sq028_kerry_romance — Boat Drinks

## 当前判断

- 状态：`journal-located`
- 候选影响：`relationship` / `ending`
- 置信度：高（任务级）

## Journal 定位

关键 phase：`quests/side_quest/sq028_kerry_romance/cruiser`

候选 objective：

- `cruiser/help_kerry` — Help Kerry.
- `cruiser/talk_kerry3` — Talk to Kerry.（暂定为最终岸边关系确认对话）

## 外部交叉验证

PowerPyx 将帮助 Kerry 时出现的互动标为关键亲密节点，并指出上岸后的最终对话决定是否建立持续关系；关系状态会在 epilogue 中体现。

## 游戏资源 fact 证据

RedSync 的 `sq028` quest/questphase fact 集合中确认存在：

- `sq028_05_no_kiss`
- `sq028_05_sex`
- `sq028_kerry_romance`
- `sq028_kerry_romance3`
- `sq028_kerry_sexa`
- `sq028_06_wrap_up`
- `sq028_kerry_cruiser_end`
- `sq028_kerry_goes_home_alone`

这些事实名直接证明 Boat Drinks 的任务图维护 kiss / sex / romance / wrap-up 等分支状态，和攻略描述的亲密节点高度一致。

当前仍需 node-level 映射，特别是确定 `help_kerry` 与 `talk_kerry2/talk_kerry3` 分别对应哪些 Set/Condition。

## 阶段提示候选

- `cruiser/help_kerry` → `important`，高置信度。
- `cruiser/talk_kerry3` → `important`，中置信度；`talk_kerry2` / `talk_kerry3` 的精确场景映射仍需验证。

## 下一步

确认 `sq028_05_no_kiss` / `sq028_05_sex` / `sq028_kerry_romance` 的写入节点与 Journal objective 对齐关系，并追踪 epilogue 读取。
