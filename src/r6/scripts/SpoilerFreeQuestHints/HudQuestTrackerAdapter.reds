module SpoilerFreeQuestHints

@wrapMethod(QuestTrackerGameController)
private final func UpdateTrackerData() -> Void {
  wrappedMethod();

  let currentTitle: String = inkTextRef.GetText(this.m_QuestTitle);
  if Equals(currentTitle, "") {
    return;
  };

  inkTextRef.SetText(
    this.m_QuestTitle,
    currentTitle + "  影响：关系 / 后续任务 / 结局条件"
  );
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

  let currentText: String = inkTextRef.GetText(this.m_objectiveTitle);
  inkTextRef.SetText(this.m_objectiveTitle, currentText + "  [测试] 重要阶段");
}
