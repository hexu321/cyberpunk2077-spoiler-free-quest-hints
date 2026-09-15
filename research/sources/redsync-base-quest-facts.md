# RedSync base-game quest/fact extraction

## 来源

- Repository: `https://github.com/nobody71004/RedSync`
- Provenance page: `release/BASE-QUEST-WHITELIST.md`
- Fact dump: `release/base_facts_per_quest.json`
- Extracted archive: `archive/pc/content/basegame_4_gamedata.archive`
- Extraction date reported by source: 2026-08-18
- Coverage reported by source: 439 decompressed `.quest` / `.questphase` files and 10,580 distinct fact strings.

本项目不复制 RedSync 的代码或整份资源，只记录与候选任务核验相关的事实名和来源位置。

## 证据强度边界

`base_facts_per_quest.json` 能证明：某个 fact 字符串确实被该 quest 的已解包 `.quest/.questphase` 资源引用。

它**不能单独证明**：

- 该 fact 在这个文件里是 Set 还是 Condition/Get；
- 具体是哪一个 scene / graph node 触发；
- 哪个 Journal objective 与该 node 精确对应。

因此 fact dump 用于把候选从“纯攻略推断”提高到“游戏资源存在性 / 跨任务引用证据”，但在没有 node-level 映射之前，不单独把 stage candidate 提升为 `logic-verified`。

## 当前高价值发现

### sq030 — Pyramid Song / Judy

已在 `sq030` 图资源 fact 集合中确认：

- `sq030_done_romance`
- `sq030_done_friendship`
- `sq030_friendship`
- `sq030_judy_lover`
- `sq030_judy_romance`
- `sq030_left_after_sex`
- `sq030_morning`
- `sq030_09_hut_pier_sit`
- `sq030_11_hut_morning`
- `sq030_11_morning`
- `sq030_romance`

这与我们已经定位的 `hut/check_judy` / `hut/sit_morning` 阶段高度吻合，但还需要 node-level Set/Condition 映射。

### sq028 — Boat Drinks / Kerry

已在 `sq028` 图资源 fact 集合中确认：

- `sq028_05_no_kiss`
- `sq028_05_sex`
- `sq028_kerry_romance`
- `sq028_kerry_romance3`
- `sq028_kerry_sexa`
- `sq028_06_wrap_up`
- `sq028_kerry_cruiser_end`
- `sq028_kerry_goes_home_alone`

证明该任务资源确实维护了 kiss / sex / romance / wrap-up 等分支状态；仍需把这些 facts 映射到 `help_kerry` 与最终 `Talk to Kerry` objective。

### sq029 — Following the River / River

已在 `sq029` 图资源 fact 集合中确认：

- `sq029_05_morning_after`
- `sq029_05a_ch_rom_yes`
- `sq029_05b_ch_rom_no`
- `sq029_06a_sex`
- `sq029_romance_end`
- `sq029_sobchak_romance`

另外，`sq029` 图资源还引用：

- `sq021_good_farm_chosen`
- `sq021_river_dead`
- `sq021_sobchak_friend`

这是当前最强的跨任务证据之一：River 后续任务资源明确携带了前一任务 `The Hunt` 的状态 fact。

### sq021 — The Hunt

已在 `sq021` 图资源 fact 集合中确认：

- `sq021_afterbd_goodfarm`
- `sq021_afterbd_badfarm`
- `sq021_good_farm_chosen`
- `sq021_good_farm`
- `sq021_farm_good_arrive`
- `sq021_farm_wrong_arrive`
- `sq021_randy_lives`
- `sq021_randy_died`

结合 `sq029` 对 `sq021_good_farm_chosen` 等 fact 的跨任务引用，已经确认“农场判断 / Randy 状态”不是攻略虚构，而是后续任务图确实关心的持久状态。

### sq031 — Chippin' In / Johnny

已在 `sq031` 图资源 fact 集合中确认专门的墓地阶段状态：

- `sq031_03_ch_grave`
- `sq031_05_grave`
- `sq031_05_grave_in`
- `sq031_05_sm_grave`
- `sq031_05_follow_up_in`
- `sq031_06_rogue_call`

但目前 fact dump 中没有直接找到社区常提到的 `sq032_johnny_friend`，因此暂时不能只靠这个 dump 完成“墓地对话 -> 隐藏结局资格”的内部因果证明。下一步仍需 scene 或 condition node 级别证据。
