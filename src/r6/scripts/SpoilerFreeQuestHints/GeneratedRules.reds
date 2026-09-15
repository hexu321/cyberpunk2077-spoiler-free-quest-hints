module SpoilerFreeQuestHints

// Generated from data/hints.json. Do not edit by hand.

public func QOHResolveQuestImpactLabel(questPath: String) -> String {
  if Equals(questPath, "quests/side_quest/sq018_jackie") {
    return "人物关系";
  };
  if Equals(questPath, "quests/meta/02_sickness") {
    return "结局条件";
  };
  if Equals(questPath, "ep1/quests/main_quest/q304_deal") {
    return "后续任务 / 结局条件";
  };
  return "";
}

public func QOHResolveExactObjectiveLabel(objectivePath: String) -> String {
  if Equals(objectivePath, "quests/side_quest/sq018_jackie/02_storage/05a_optional_talk_misty") {
    return "值得留意";
  };
  if Equals(objectivePath, "quests/meta/02_sickness/q115/02_meet_hanako") {
    return "关键节点 · 建议存档";
  };
  if Equals(objectivePath, "ep1/quests/main_quest/q304_deal/06b_lab/05_decide") {
    return "关键节点 · 建议存档";
  };
  return "";
}

public func QOHResolveQuestFallbackLabel(questPath: String) -> String {
  return "";
}
