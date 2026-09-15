module SpoilerFreeQuestHints

public func QOHBuildEntryPath(journalManager: wref<JournalManager>, entry: wref<JournalEntry>) -> String {
  if !IsDefined(journalManager) || !IsDefined(entry) {
    return "";
  };

  let path: String = entry.GetId();
  let parent: wref<JournalEntry> = journalManager.GetParentEntry(entry);
  let guard: Int32 = 0;

  while IsDefined(parent) && guard < 24 {
    path = parent.GetId() + "/" + path;
    parent = journalManager.GetParentEntry(parent);
    guard += 1;
  };

  return path;
}

public func QOHFindQuestPath(journalManager: wref<JournalManager>, entry: wref<JournalEntry>) -> String {
  if !IsDefined(journalManager) || !IsDefined(entry) {
    return "";
  };

  let current: wref<JournalEntry> = entry;
  let guard: Int32 = 0;

  while IsDefined(current) && guard < 24 {
    let quest: wref<JournalQuest> = current as JournalQuest;
    if IsDefined(quest) {
      return QOHBuildEntryPath(journalManager, quest);
    };

    current = journalManager.GetParentEntry(current);
    guard += 1;
  };

  return "";
}
