# qg.sq029_sobchak_romance — Following the River

## 当前判断

- 状态：`journal-located`
- 候选影响：`relationship` / `ending`
- 置信度：高

## Journal 定位

关键 phase：`quests/side_quest/sq029_sobchak_romance/drink_with_river`

候选 objective：

- `drink_with_river/hang_out_with_river` — Sit with River.
- `breakfast/talk_with_river` — Talk to River.

## 外部交叉验证

Cyberpunk Wiki 与 PowerPyx 一致指出：水塔对话包含决定是否进入 River 恋爱线的关键选择；次日对话会确认关系是否继续。该关系状态会改变后续 epilogue 表现。

## 游戏资源 fact 证据

RedSync 的 `sq029` quest/questphase fact 集合中确认存在：

- `sq029_05_morning_after`
- `sq029_05a_ch_rom_yes` / `sq029_05b_ch_rom_no`
- `sq029_06a_sex`
- `sq029_romance_end`
- `sq029_sobchak_romance`

同时该任务图还引用 `sq021_good_farm_chosen`、`sq021_river_dead`、`sq021_sobchak_friend`，说明 Following the River 的图资源确实依赖 The Hunt 留下的状态。

这已经把“River 关系线存在持久状态”从攻略结论提升到了游戏资源存在性证据；但尚未确认每个 fact 的 Set/Condition 节点。

## 阶段提示候选

- `drink_with_river/hang_out_with_river` → `important`
- `breakfast/talk_with_river` → `important`

## 下一步

确认 `sq029_05a_ch_rom_yes` / `sq029_05b_ch_rom_no` 与水塔 Journal objective 的 node 映射，并确认 `sq029_romance_end` / `sq029_sobchak_romance` 在后续 epilogue 中的读取。
