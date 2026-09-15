module SpoilerFreeQuestHints

@wrapMethod(SimpleQuestListItemController)
protected cb func OnDataChanged(value: Variant) -> Bool {
  let result: Bool = wrappedMethod(value);

  if !IsDefined(this.m_data) || Equals(this.m_data.m_questType, QuestListItemType.Finished) {
    return result;
  };

  let impactText: String = "影响：关系 / 后续任务 / 结局条件";
  let currentTitle: String = inkTextRef.GetText(this.m_title);

  inkTextRef.SetText(this.m_title, currentTitle + "  " + impactText);
  inkTextRef.SetVisible(this.m_description, true);

  return result;
}
