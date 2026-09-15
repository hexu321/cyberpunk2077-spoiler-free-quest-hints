# qg.sq030_judy_romance — Pyramid Song

## 当前判断

- 状态：`journal-located`
- 候选影响：`relationship` / `ending`
- 置信度：高

## Journal 定位

关键 phase：`quests/side_quest/sq030_judy_romance/hut`

候选 objective：

- `hut/check_judy` — Check on Judy.
- `hut/sit_morning` — Sit beside Judy.

## 外部交叉验证

Cyberpunk Wiki 与 PowerPyx 一致把小屋浴室对话列为 Judy 关系线的关键节点，并指出次日湖边/早晨对话会确认或拒绝持续关系。该关系状态会在后续 epilogue 中体现。

## 游戏资源 fact 证据

RedSync 从实际 `sq030` quest/questphase 资源中确认存在：

- `sq030_done_romance` / `sq030_done_friendship`
- `sq030_friendship`
- `sq030_judy_lover`
- `sq030_judy_romance`
- `sq030_left_after_sex`
- `sq030_morning`
- `sq030_09_hut_pier_sit`
- `sq030_11_hut_morning` / `sq030_11_morning`

这些命名与我们从 Journal 定位出的 hut / morning 阶段高度吻合，已经证明该任务图内部确实维护 romance / friendship / morning 状态，而不只是攻略推断。

当前仍保持 `gameLogicVerified=false`：fact dump 还不能告诉我们具体哪个节点是 Set、哪个节点是 Condition。

## 阶段提示候选

- `hut/check_judy` → `important`
- `hut/sit_morning` → `important`

## 下一步

确认 `sq030_judy_romance` / `sq030_judy_lover` / `sq030_done_romance` 的 Set 节点分别落在哪段 scene/questphase，并追踪 epilogue 对这些 facts 的读取位置。
