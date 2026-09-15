module SpoilerFreeQuestHints

@wrapMethod(QuestTrackerGameController)
private final func UpdateTrackerData() -> Void {
  wrappedMethod();

  if !IsDefined(this.m_journalManager) {
    return;
  };

  if IsDefined(this.m_bufferedQuest) {
    let impactText: String = QOHResolveImpact(this.m_journalManager, this.m_bufferedQuest);
    if NotEquals(impactText, "") {
      let currentTitle: String = inkTextRef.GetText(this.m_QuestTitle);
      if NotEquals(currentTitle, "") {
        inkTextRef.SetText(this.m_QuestTitle, currentTitle + "  影响：" + impactText);
      };
    };
  };

  let i: Int32 = 0;
  while i < inkCompoundRef.GetNumChildren(this.m_ObjectiveContainer) {
    let controller: wref<QuestTrackerObjectiveLogicController> =
      inkCompoundRef.GetWidgetByIndex(this.m_ObjectiveContainer, i).GetController() as QuestTrackerObjectiveLogicController;
    if IsDefined(controller) {
      controller.QOHApplyHint(this.m_journalManager);
    };
    i += 1;
  };
}

@addMethod(QuestTrackerObjectiveLogicController)
public final func QOHApplyHint(journalManager: wref<JournalManager>) -> Void {
  let objectiveEntry: wref<JournalQuestObjective> = this.GetObjectiveEntry();
  if !IsDefined(objectiveEntry) {
    return;
  };

  let label: String = QOHResolveLabel(journalManager, objectiveEntry);
  if Equals(label, "") {
    return;
  };

  let currentText: String = inkTextRef.GetText(this.m_objectiveTitle);
  inkTextRef.SetText(this.m_objectiveTitle, currentText + "  [" + label + "]");
}
