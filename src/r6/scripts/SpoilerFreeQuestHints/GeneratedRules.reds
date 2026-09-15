module SpoilerFreeQuestHints

// Generated from data/hints.json. Do not edit by hand.

public func QOHResolveExactObjectiveLabel(objectivePath: String) -> String {
  return "";
}

public func QOHResolveQuestFallbackLabel(questPath: String) -> String {
  if Equals(questPath, "quests/meta/02_sickness") {
    return "关键节点 · 建议存档";
  };
  if Equals(questPath, "ep1/quests/main_quest/q304_deal") {
    return "关键节点 · 建议存档";
  };
  return "";
}
