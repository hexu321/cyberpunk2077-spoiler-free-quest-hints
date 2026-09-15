module SpoilerFreeQuestHints

@wrapMethod(SimpleQuestListItemController)
protected cb func OnDataChanged(value: Variant) -> Bool {
  let result: Bool = wrappedMethod(value);

  if !IsDefined(this.m_data) || Equals(this.m_data.m_questType, QuestListItemType.Finished) {
    return result;
  };

  let impactText: String = QOHResolveImpact(
    this.m_data.m_journalManager,
    this.m_data.m_questData
  );
  if Equals(impactText, "") {
    return result;
  };

  let currentTitle: String = inkTextRef.GetText(this.m_title);
  inkTextRef.SetText(this.m_title, currentTitle + "  影响：" + impactText);

  return result;
}
