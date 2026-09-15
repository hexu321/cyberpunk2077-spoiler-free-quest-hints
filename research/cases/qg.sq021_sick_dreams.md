# qg.sq021_sick_dreams — The Hunt

## 当前判断

- 状态：`journal-located`
- 候选影响：`relationship` / `followup` / `ending`
- 置信度：高

## Journal 定位

关键 objective：

- `quests/side_quest/sq021_sick_dreams/after_bd/after_bd` — Plan the next move with River.
- `quests/side_quest/sq021_sick_dreams/finale/22_go_back_to_river` — Return to River.

辅助信息收集 objective：

- `quests/side_quest/sq021_sick_dreams/bd/09_texas_clues` — Look for clues to help find Randy. [Optional]

## 外部交叉验证

Cyberpunk Wiki 与 PowerPyx 一致指出：BD 阶段收集足够线索会帮助定位正确农场；在 `Plan the next move with River` 阶段选错位置可能导致无法救出 Randy，并锁掉 River 最后的任务/关系线。救援后的 River 对话还会继续影响关系走向。

## 游戏资源 fact 证据

RedSync 从实际 `basegame_4_gamedata.archive` 解出的 `sq021` quest/questphase 资源中确认存在：

- `sq021_afterbd_goodfarm` / `sq021_afterbd_badfarm`
- `sq021_good_farm_chosen`
- `sq021_farm_good_arrive` / `sq021_farm_wrong_arrive`
- `sq021_randy_lives` / `sq021_randy_died`

更重要的是，后续 `sq029`（Following the River）的任务资源中又出现了 `sq021_good_farm_chosen`、`sq021_river_dead`、`sq021_sobchak_friend`。这形成了强跨任务状态引用证据：The Hunt 的结果确实被 River 后续任务链引用。

当前仍不直接升级为 `logic-verified`，因为还需要确认 `after_bd/after_bd` 对应 graph node 是如何 Set/Condition 这些 facts 的。

## 阶段提示候选

- `after_bd/after_bd` → `important`，高置信度。
- `finale/22_go_back_to_river` → `notice`，中置信度，需 scene 映射确认。

`bd/09_texas_clues` 暂不直接提示：它只是提高后续判断的可靠性，并不是最终决定本身。

## 下一步

定位 `sq021_good_farm_chosen` / `sq021_randy_lives` / `sq021_randy_died` 的 Set 节点，以及 `sq029` 中读取这些状态的 Condition 节点；再把具体 Journal objective 与节点对齐。
