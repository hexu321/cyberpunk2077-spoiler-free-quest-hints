# Research workspace

这个目录用于维护“可能影响剧情的任务/阶段”的研究过程，不直接驱动游戏运行时。

## 目录职责

```text
research/
├─ candidates.jsonl                  # 一行一个候选研究任务；机器可读的研究队列
├─ cases/                            # 单个候选的详细调查记录
│  └─ TEMPLATE.md
└─ sources/
   └─ questguide-1.5.0-seed.json     # 从本地 QuestGuide 1.5.0 归一化出的种子集合
```

正式进入游戏的规则仍然只来自：

```text
data/hints.json
```

研究队列中的候选在完成核验前，不得自动进入 `data/hints.json`。

## 候选状态

按下面的顺序推进：

```text
candidate
  -> journal-located
  -> logic-verified
  -> in-game-verified
  -> ready
  -> shipped
```

含义：

- `candidate`：已有可信来源认为值得调查，但尚未定位到具体 Journal 阶段。
- `journal-located`：已经确认 questPath / phase / objectivePath。
- `logic-verified`：已经从游戏逻辑、quest fact、scene / questphase 或等价证据确认存在后续影响。
- `in-game-verified`：已通过真实存档/游戏内行为确认提示时机正确。
- `ready`：证据足够，可进入 `data/hints.json`。
- `shipped`：已经随正式规则发布。

## 数据源优先级

1. **游戏真实资源**：`.quest` / `.questphase` / `.scene` / Quest Facts。用于确认因果链。
2. **CDPR / REDmodding Journal 数据**：用于定位稳定的 quest / phase / objective 内部路径。
3. **本地 QuestGuide 1.5.0**：作为人工筛过的高价值候选种子，不作为最终唯一事实来源。
4. **成熟 Wiki / Walkthrough**：用于发现候选和交叉验证。
5. **游戏内 A/B 存档测试**：最终验收，尤其是 `critical` 规则。

## QuestGuide 使用边界

本地参考源码位于被 Git 忽略的：

```text
references/QuestGuide-1.5.0/
```

只允许用它来识别“哪些任务值得调查”和理解公开可观察的分类思路；不要复制其实现、源码块、资产或 UI 文本到本项目。

当前 `sources/questguide-1.5.0-seed.json` 只保存我们自己归一化后的任务 ID、候选影响类型和来源位置，不保存 QuestGuide 的实现代码。

## 候选记录原则

- `suspectedImpacts` 只是“待验证影响类型”，不是正式结论。
- 不在研究队列中记录推荐选项、角色命运、结局名称等玩家可见剧透字段。
- 能定位到具体 objective 时，优先把阶段提示缩窄到 objective，而不是整条 quest fallback。
- 如果后续证据推翻候选，保留调查记录并标记为 `rejected` / 在 notes 中说明，而不是悄悄删除研究历史。
