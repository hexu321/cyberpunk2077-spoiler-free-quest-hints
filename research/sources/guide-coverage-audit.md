# Guide coverage audit

这份文件记录“剧情影响研究库”已经扫过的攻略来源、纳入边界和明确排除项，用于避免重复全量研究。

## 已系统扫过的来源

- PowerPyx：Story Choices Guide、Endings Guide、四条主要恋爱线指南、相关单任务 walkthrough、Phantom Liberty ending / trophy route guides。
- Game8：All Choices and Effects、本体主线任务页、Phantom Liberty 任务与结局相关页面。
- GamePressure：Important Choices 总表及对应的重要选择页面。
- Cyberpunk Wiki：任务链、结局条件、角色关系和部分隐藏失败条件的交叉验证。
- 其它按需交叉来源：GameSpot、Push Square、PC Gamer、Destructoid、TrueAchievements、GamerGuides。
- CDPR / REDmodding Journal 数据：只用于确认 `questPath`、`phase` 和 `objectivePath`，不单独判断剧情后果。

## 纳入条件

只收至少符合下列一项、且有成熟来源明确说明存在持续影响的选择：

1. `relationship`：持续改变 V 与角色、或重要 NPC 之间的关系/关系状态；包括恋爱、友好/敌对和明确的 NPC 关系结局。
2. `followup`：开启、关闭、提前终止或显著改变后续任务/任务链内容。
3. `ending`：开启、关闭、选择或明显改变正式结局/尾声内容。

只改变当前一句对白、临时战斗方式、钱、装备、单次奖励、进场路线或商店库存，不自动纳入。

## 强度规则

- `critical`：点 of no return、直接关闭重要任务链/结局资格、或真正选择结局/尾声的节点。
- `important`：明确开启/关闭后续任务、决定重要关系状态、或产生较大的持续剧情差异。
- `notice`：持续关系/尾声差异存在，但不会直接锁死主要任务线；或影响可补救。

## 已覆盖的高价值区域

- 本体主线长期选择：The Pickup、The Heist、Automatic Love、Ghost Town、Life During Wartime、I Walk the Line、Gimme Danger、Play It Safe、Search and Destroy、Nocturne Op55N1、Changes、Where Is My Mind?。
- Johnny / Rogue：Chippin' In、Blistering Love 及相关链路。
- Panam：Riders on the Storm、With a Little Help From My Friends、Queen of the Highway，以及早期 Ghost Town / Life During Wartime 关系节点。
- Judy：Talkin' 'bout a Revolution、Pisces、Pyramid Song 等真正有后续/关系影响的节点。
- River：The Hunt、Following the River。
- Kerry / Us Cracks：Holdin' On 到 Boat Drinks 的链路，以及 I Don't Wanna Hear It 对 Every Breath You Take 的影响。
- 其它持续支线：Heroes、Sinnerman 任务链、The Beast in Me、Violence、Raymond Chandler Evening、Dream On。
- Phantom Liberty：Lucretia My Reflection 的退出点、Firestarter 主分岔、Somewhat Damaged / The Killing Moon 二次结局分岔、Who Wants to Live Forever 的 Tower 最终确认点。

## 明确排除或暂不纳入

下面这些已经检查过，除非未来新证据证明会影响三大分类，否则不要重复研究：

- The Space in Between / Fingers：主要是后续商店可用性，不属于当前三类。
- Both Sides, Now、Ex-Factor：攻略明确说明其中普通选择不是 Judy 恋爱硬门槛；不要因为任务属于 Judy 链就给所有阶段加标签。
- I Fought the Law：普通选择不是 River 恋爱决定点。
- A Cool Metal Fire：交互本身没有独立持续后果；保留为 `rejected` 研究记录，真正后果在 Chippin' In。
- Second Conflict 的 Denny/Henry 选择：主要改变演出参与者/对白，不作为独立 stage 警告。
- Spellbound：不同做法主要影响钱与物品；未发现可靠证据证明某个选择是 KOLD MIRAGE 的必要开关。
- Run This Town：主要改变 Mr. Hands 的满意度/局部收尾，未发现 Phantom Liberty 结局资格变化；为避免把每个 fixer approval 都当 `relationship`，暂不收。
- No Easy Way Out、Balls to the Wall、Shot by Both Sides 等 Phantom Liberty 支线：主要是 NPC 命运/奖励差异；没有明确的关系、后续任务链或正式结局影响时不收。
- Happy Together：重要角色命运，但当前 schema 没有 `character_fate` 分类；除非以后增加新分类，否则不强塞进 relationship/followup/ending。
- Full Disclosure：主要是信任/奖励对白差异，未发现明确后续任务或结局门槛。
- Gimme Danger 只按 `notice / relationship` 收录：一起侦察会带来更好的 Takemura 关系与后续额外对白，但不会改变任务进度或结局资格。

## 收尾判断

完成 PowerPyx、Game8、GamePressure 的总表与主关系/结局专题交叉后，发现的大多数新增项已经从“大任务缺失”转为少量软关系或次级支线差异。

因此后续工作默认从“广泛发现”切换为：

1. 游戏内验证标签出现时机；
2. 对高置信研究规则分批晋升到 `data/hints.json`；
3. 只有遇到新资料明确指出现有库遗漏了三大分类的持续后果时，才重新进入候选发现阶段。
