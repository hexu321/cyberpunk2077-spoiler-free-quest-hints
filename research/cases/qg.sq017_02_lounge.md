# qg.sq017_02_lounge — Off the Leash

## 当前判断

- 状态：`journal-located`
- 候选影响：`relationship` / `ending`
- 置信度：高（任务级）；中（精确 objective 映射）

## Journal 定位

`party` phase 中：

- `party/find_kerry` — Talk to Kerry.
- `party/follow_kerry` — Follow Kerry.
- `party/enjoy` — Talk to Kerry.

根据 Journal 顺序和攻略流程，`party/enjoy` 最可能对应跟随 Kerry 到露台后的关键对话。

## 外部交叉验证

PowerPyx 将露台对话明确标成 Kerry 关系线的第一个直接 romance 选择，并说明下一任务 Boat Drinks 仍会继续该路线。

## 阶段提示候选

- `party/enjoy` → `important`，目前中置信度。

## 下一步

必须从 scene/questphase 确认 `party/enjoy` 是否确实是露台选择所在 objective；确认后再升级置信度。
