module SpoilerFreeQuestHints

@wrapMethod(QuestDetailsObjectiveController)
public final func Setup(
  objective: wref<JournalQuestObjective>,
  journalManager: wref<JournalManager>,
  currentCounter: Int32,
  totalCounter: Int32,
  opt isTracked: Bool
) -> Void {
  wrappedMethod(objective, journalManager, currentCounter, totalCounter, isTracked);

  if NotEquals(journalManager.GetEntryState(objective), gameJournalEntryState.Active) {
    return;
  };

  let currentText: String = inkTextRef.GetText(this.m_objectiveName);
  inkTextRef.SetText(this.m_objectiveName, currentText + "  [测试] 重要阶段");
}
