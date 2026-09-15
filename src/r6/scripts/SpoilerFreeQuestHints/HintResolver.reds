module SpoilerFreeQuestHints

public func QOHResolveLabel(journalManager: wref<JournalManager>, objective: wref<JournalQuestObjective>) -> String {
  if !IsDefined(journalManager) || !IsDefined(objective) {
    return "";
  };

  if NotEquals(journalManager.GetEntryState(objective), gameJournalEntryState.Active) {
    return "";
  };

  let objectivePath: String = QOHBuildEntryPath(journalManager, objective);
  let exactLabel: String = QOHResolveExactObjectiveLabel(objectivePath);
  if NotEquals(exactLabel, "") {
    return exactLabel;
  };

  let questPath: String = QOHFindQuestPath(journalManager, objective);
  return QOHResolveQuestFallbackLabel(questPath);
}
