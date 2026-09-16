module SpoilerFreeQuestHints

// Generated from data/hints.json. Do not edit by hand.

public func QOHResolveQuestImpactLabel(questPath: String) -> String {
  if QOHPathMatches(questPath, "quests/meta/02_sickness") {
    return "结局条件";
  };
  if QOHPathMatches(questPath, "quests/side_quest/sq004_riders_on_the_storm") {
    return "人物关系 / 后续任务 / 结局条件";
  };
  if QOHPathMatches(questPath, "quests/side_quest/sq031_rogue") {
    return "后续任务 / 结局条件";
  };
  if QOHPathMatches(questPath, "quests/side_quest/sq030_judy_romance") {
    return "人物关系 / 结局条件";
  };
  if QOHPathMatches(questPath, "quests/side_quest/sq029_sobchak_romance") {
    return "人物关系 / 结局条件";
  };
  if QOHPathMatches(questPath, "quests/side_quest/sq021_sick_dreams") {
    return "人物关系 / 后续任务 / 结局条件";
  };
  if QOHPathMatches(questPath, "quests/side_quest/sq028_kerry_romance") {
    return "人物关系 / 结局条件";
  };
  if QOHPathMatches(questPath, "quests/side_quest/sq011_kerry") {
    return "后续任务";
  };
  if QOHPathMatches(questPath, "quests/side_quest/sq017_kerry") {
    return "后续任务";
  };
  if QOHPathMatches(questPath, "quests/side_quest/sq011_concert") {
    return "后续任务";
  };
  if QOHPathMatches(questPath, "quests/side_quest/sq011_johnny") {
    return "后续任务";
  };
  if QOHPathMatches(questPath, "quests/side_quest/sq017_02_lounge") {
    return "人物关系 / 结局条件";
  };
  if QOHPathMatches(questPath, "quests/side_quest/sq017_01_riot_club") {
    return "后续任务";
  };
  if QOHPathMatches(questPath, "quests/main_quest/prologue/q003_maelstrom") {
    return "人物关系 / 后续任务";
  };
  if QOHPathMatches(questPath, "quests/main_quest/prologue/q005_heist") {
    return "后续任务 / 结局条件";
  };
  if QOHPathMatches(questPath, "quests/main_quest/act_01/q110_voodoo") {
    return "后续任务";
  };
  if QOHPathMatches(questPath, "quests/main_quest/act_01/q112_04_hideout") {
    return "结局条件";
  };
  if QOHPathMatches(questPath, "quests/side_quest/sq026_04_hiromi") {
    return "人物关系 / 后续任务";
  };
  if QOHPathMatches(questPath, "quests/side_quest/sq027_01_basilisk_convoy") {
    return "人物关系 / 后续任务 / 结局条件";
  };
  if QOHPathMatches(questPath, "quests/side_quest/sq027_02_raffen_shiv_attack") {
    return "人物关系 / 结局条件";
  };
  if QOHPathMatches(questPath, "ep1/quests/main_quest/q304_deal") {
    return "后续任务 / 结局条件";
  };
  if QOHPathMatches(questPath, "quests/side_quest/sq018_jackie") {
    return "人物关系";
  };
  if QOHPathMatches(questPath, "quests/main_quest/act_01/q105_dollhouse") {
    return "后续任务";
  };
  if QOHPathMatches(questPath, "quests/main_quest/act_01/q112_03_dashi_parade") {
    return "结局条件";
  };
  if QOHPathMatches(questPath, "ep1/quests/main_quest/q306_devils_bargain") {
    return "后续任务 / 结局条件";
  };
  if QOHPathMatches(questPath, "ep1/quests/main_quest/q305_bunker") {
    return "后续任务 / 结局条件";
  };
  if QOHPathMatches(questPath, "quests/side_quest/sq023_hit_order") {
    return "后续任务";
  };
  if QOHPathMatches(questPath, "quests/side_quest/sq023_bd_passion") {
    return "后续任务";
  };
  if QOHPathMatches(questPath, "quests/side_quest/sq024_santo_domingo_race") {
    return "人物关系 / 后续任务";
  };
  if QOHPathMatches(questPath, "quests/side_quest/sq024_the_big_race") {
    return "人物关系 / 后续任务";
  };
  if QOHPathMatches(questPath, "quests/minor_quest/mq019_paparazzi") {
    return "后续任务";
  };
  if QOHPathMatches(questPath, "ep1/quests/main_quest/q302_reed") {
    return "后续任务";
  };
  if QOHPathMatches(questPath, "quests/main_quest/epilogues/q201_heir") {
    return "结局条件";
  };
  if QOHPathMatches(questPath, "quests/side_quest/sq026_03_pizza") {
    return "后续任务";
  };
  if QOHPathMatches(questPath, "quests/main_quest/act_01/q116_cyberspace") {
    return "结局条件";
  };
  if QOHPathMatches(questPath, "quests/minor_quest/mq040_biosculpt") {
    return "人物关系";
  };
  if QOHPathMatches(questPath, "ep1/quests/main_quest/q307_before_tomorrow") {
    return "结局条件";
  };
  return "";
}

public func QOHResolveExactObjectiveLabel(objectivePath: String) -> String {
  if QOHPathMatches(objectivePath, "quests/side_quest/sq031_rogue/grave/04_sit_grave") {
    return "关键节点 · 建议存档";
  };
  if QOHPathMatches(objectivePath, "quests/side_quest/sq031_rogue/grave/06_talk_to_johnny") {
    return "关键节点 · 建议存档";
  };
  if QOHPathMatches(objectivePath, "quests/side_quest/sq004_riders_on_the_storm/03_escape/sit_down") {
    return "重要阶段";
  };
  if QOHPathMatches(objectivePath, "quests/side_quest/sq004_riders_on_the_storm/03_escape/morning_after") {
    return "值得留意";
  };
  if QOHPathMatches(objectivePath, "quests/side_quest/sq030_judy_romance/hut/check_judy") {
    return "重要阶段";
  };
  if QOHPathMatches(objectivePath, "quests/side_quest/sq030_judy_romance/hut/sit_morning") {
    return "重要阶段";
  };
  if QOHPathMatches(objectivePath, "quests/side_quest/sq021_sick_dreams/after_bd/04_choose_farm") {
    return "重要阶段";
  };
  if QOHPathMatches(objectivePath, "quests/side_quest/sq021_sick_dreams/aftermath/talk") {
    return "重要阶段";
  };
  if QOHPathMatches(objectivePath, "quests/side_quest/sq029_sobchak_romance/drink_with_river/hang_out_with_river") {
    return "重要阶段";
  };
  if QOHPathMatches(objectivePath, "quests/side_quest/sq029_sobchak_romance/breakfast/talk_with_river") {
    return "重要阶段";
  };
  if QOHPathMatches(objectivePath, "quests/side_quest/sq017_02_lounge/party/enjoy") {
    return "重要阶段";
  };
  if QOHPathMatches(objectivePath, "quests/side_quest/sq028_kerry_romance/cruiser/help_kerry") {
    return "重要阶段";
  };
  if QOHPathMatches(objectivePath, "quests/side_quest/sq028_kerry_romance/cruiser/talk_kerry3") {
    return "重要阶段";
  };
  if QOHPathMatches(objectivePath, "quests/side_quest/sq017_01_riot_club/nightclub/talk_us_cracks") {
    return "重要阶段";
  };
  if QOHPathMatches(objectivePath, "quests/main_quest/act_01/q110_voodoo/03_mall_job/05_find_netwatch_agent") {
    return "重要阶段";
  };
  if QOHPathMatches(objectivePath, "quests/main_quest/act_01/q112_04_hideout/06_safe_house/06i_save") {
    return "重要阶段";
  };
  if QOHPathMatches(objectivePath, "quests/side_quest/sq026_04_hiromi/02_penthouse/hiromi") {
    return "重要阶段";
  };
  if QOHPathMatches(objectivePath, "quests/side_quest/sq026_04_hiromi/02_penthouse/talk_maiko") {
    return "重要阶段";
  };
  if QOHPathMatches(objectivePath, "quests/side_quest/sq027_01_basilisk_convoy/01a_ratting_out/00_talk_to_saul") {
    return "关键节点 · 建议存档";
  };
  if QOHPathMatches(objectivePath, "quests/side_quest/sq027_01_basilisk_convoy/02_preparations_new/03e_talk_to_panam_view") {
    return "重要阶段";
  };
  if QOHPathMatches(objectivePath, "quests/side_quest/sq027_01_basilisk_convoy/02_preparations_new/05a_look_at_stars") {
    return "值得留意";
  };
  if QOHPathMatches(objectivePath, "quests/side_quest/sq027_02_raffen_shiv_attack/04_panzer/05_talk_panam_again") {
    return "重要阶段";
  };
  if QOHPathMatches(objectivePath, "quests/meta/02_sickness/q115/02_meet_hanako") {
    return "关键节点 · 建议存档";
  };
  if QOHPathMatches(objectivePath, "ep1/quests/main_quest/q304_deal/06b_lab/05_decide") {
    return "关键节点 · 建议存档";
  };
  if QOHPathMatches(objectivePath, "quests/side_quest/sq018_jackie/02_storage/05a_optional_talk_misty") {
    return "值得留意";
  };
  if QOHPathMatches(objectivePath, "quests/main_quest/prologue/q003_maelstrom/militech/02_meet_militech1") {
    return "值得留意";
  };
  if QOHPathMatches(objectivePath, "quests/main_quest/prologue/q003_maelstrom/militech/04_remove_malware") {
    return "重要阶段";
  };
  if QOHPathMatches(objectivePath, "quests/main_quest/prologue/q003_maelstrom/maelstrom_deal/08_make_deal") {
    return "重要阶段";
  };
  if QOHPathMatches(objectivePath, "quests/main_quest/prologue/q003_maelstrom/03_escape/14_save_brick") {
    return "重要阶段";
  };
  if QOHPathMatches(objectivePath, "quests/main_quest/prologue/q005_heist/return/01_talk_to_jackie") {
    return "重要阶段";
  };
  if QOHPathMatches(objectivePath, "quests/main_quest/act_01/q105_dollhouse/04_woodman/interrogate_woodman") {
    return "值得留意";
  };
  if QOHPathMatches(objectivePath, "quests/main_quest/act_01/q112_03_dashi_parade/05_parade/05f2_decide_oda") {
    return "值得留意";
  };
  if QOHPathMatches(objectivePath, "ep1/quests/main_quest/q306_devils_bargain/06_finale/01_talk_to_songbird") {
    return "关键节点 · 建议存档";
  };
  if QOHPathMatches(objectivePath, "ep1/quests/main_quest/q306_devils_bargain/06_finale/04_deal_with_reed") {
    return "关键节点 · 建议存档";
  };
  if QOHPathMatches(objectivePath, "ep1/quests/main_quest/q305_bunker/07c_cynosure_core/talk_with_songbird") {
    return "关键节点 · 建议存档";
  };
  if QOHPathMatches(objectivePath, "quests/side_quest/sq023_hit_order/hook/talk_joshua") {
    return "重要阶段";
  };
  if QOHPathMatches(objectivePath, "quests/side_quest/sq023_bd_passion/glorias_house/talk") {
    return "重要阶段";
  };
  if QOHPathMatches(objectivePath, "quests/side_quest/sq023_bd_passion/restaurant/spear") {
    return "重要阶段";
  };
  if QOHPathMatches(objectivePath, "quests/side_quest/sq024_santo_domingo_race/02_santo_domingo_race/08c_sit") {
    return "重要阶段";
  };
  if QOHPathMatches(objectivePath, "quests/side_quest/sq024_the_big_race/02_santo_domingo_race/05_follow_sampson_or_continue") {
    return "重要阶段";
  };
  if QOHPathMatches(objectivePath, "quests/side_quest/sq021_sick_dreams/bbq/enjoy") {
    return "重要阶段";
  };
  if QOHPathMatches(objectivePath, "quests/minor_quest/mq019_paparazzi/05_holocall/01_call_client") {
    return "重要阶段";
  };
  if QOHPathMatches(objectivePath, "ep1/quests/main_quest/q302_reed/07_oath/04_talk_to_myers_and_reed") {
    return "关键节点 · 建议存档";
  };
  if QOHPathMatches(objectivePath, "quests/main_quest/epilogues/q201_heir/07_cabin_day_4/02_make_final_decision") {
    return "关键节点 · 建议存档";
  };
  if QOHPathMatches(objectivePath, "quests/main_quest/epilogues/q201_heir/08_cabin_day_30_takemura/02_make_final_decision") {
    return "关键节点 · 建议存档";
  };
  if QOHPathMatches(objectivePath, "quests/side_quest/sq026_03_pizza/01_pizza_night/sparing") {
    return "值得留意";
  };
  if QOHPathMatches(objectivePath, "quests/main_quest/act_01/q116_cyberspace/01_cyberspace/03_choose") {
    return "关键节点 · 建议存档";
  };
  if QOHPathMatches(objectivePath, "quests/minor_quest/mq040_biosculpt/mq040_biosculpt/09_choose_side") {
    return "值得留意";
  };
  if QOHPathMatches(objectivePath, "ep1/quests/main_quest/q307_before_tomorrow/00_hook/02_confirm_pickup") {
    return "关键节点 · 建议存档";
  };
  return "";
}

public func QOHResolveQuestFallbackLabel(questPath: String) -> String {
  return "";
}
