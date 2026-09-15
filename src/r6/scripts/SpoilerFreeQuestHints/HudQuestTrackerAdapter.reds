module SpoilerFreeQuestHints

@wrapMethod(QuestTrackerGameController)
private final func UpdateTrackerData() -> Void {
  wrappedMethod();

  if !IsDefined(this.m_bufferedQuest) || !IsDefined(this.m_journalManager) {
    return;
  };

  let impactText: String = QOHResolveImpact(this.m_journalManager, this.m_bufferedQuest);
  if Equals(impactText, "") {
    return;
  };

  let currentTitle: String = inkTextRef.GetText(this.m_QuestTitle);
  if Equals(currentTitle, "") {
    return;
  };

  inkTextRef.SetText(this.m_QuestTitle, currentTitle + "  影响：" + impactText);
}

@wrapMethod(QuestTrackerObjectiveLogicController)
public final func SetData(
  const objectiveTitle: script_ref<String>,
  isTracked: Bool,
  isOptional: Bool,
  currentCounter: Int32,
  totalCounter: Int32,
  objectiveEntry: wref<JournalQuestObjective>,
  isQuestType: Bool
) -> Void {
  wrappedMethod(
    objectiveTitle,
    isTracked,
    isOptional,
    currentCounter,
    totalCounter,
    objectiveEntry,
    isQuestType
  );

  if !IsDefined(objectiveEntry) {
    return;
  };

  let journalManager: ref<JournalManager> = GameInstance.GetJournalManager(this.GetGame());
  let label: String = QOHResolveLabel(journalManager, objectiveEntry);
  if Equals(label, "") {
    return;
  };

  let currentText: String = inkTextRef.GetText(this.m_objectiveTitle);
  inkTextRef.SetText(this.m_objectiveTitle, currentText + "  [" + label + "]");
}
