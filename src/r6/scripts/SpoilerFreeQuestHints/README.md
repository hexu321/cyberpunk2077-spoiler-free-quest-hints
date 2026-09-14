# Runtime implementation boundary

This directory is reserved for the tested redscript runtime implementation.

Do not add guessed Journal controller method names here.

The first runtime implementation must provide three isolated responsibilities:

1. `JournalSelectionAdapter`
   - reads the selected quest and current objective from the actual Journal menu;
   - listens to the smallest verified refresh hook;
   - exposes stable Journal paths/identity to the resolver.

2. `HintResolver`
   - exact objective match first;
   - optional quest fallback second;
   - returns only `none`, `notice`, `important`, or `critical` plus the fixed label.

3. `JournalHintView`
   - owns one read-only ink text/badge element;
   - never takes controller focus;
   - hides for `none`;
   - updates/removes itself when selection or objective changes.

The UI adapter must not contain story classifications. The rules database must not contain widget/controller knowledge.
