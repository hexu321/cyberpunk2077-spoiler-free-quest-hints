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

  let label: String = QOHResolveLabel(journalManager, objective);
  if Equals(label, "") {
    return;
  };

  let currentText: String = inkTextRef.GetText(this.m_objectiveName);
  inkTextRef.SetText(this.m_objectiveName, currentText + "  [" + label + "]");
}
