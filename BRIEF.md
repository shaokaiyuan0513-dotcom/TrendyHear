# TrendyHear 0.4.4：官方 Shell 混合式 Agent

主要目标：用户点击“听见顾问”后，由 TrendyHear 自己的 Agent 在一个 `octos.turn.start` 回合内使用 `ask_user_question` 渐进收集阅读偏好。Agent 负责理解和澄清；应用负责 AppCard、校验、持久化、RSS 与新闻任务。

必填信息为操作类型、1–3 个有序主题，以及长期订阅的每日上海时间或按需阅读。用途和细分范围选填。Agent 每次只问一个缺失项，复述理解后必须再次通过 `ask_user_question` 获得明确确认。应用随后用 `model.complete` 整理严格结构；只有 `confirmed=true` 才发布偏好 AppCard。

用户点击 AppCard 的“确认保存”后，应用自身才把长期偏好写入 `accounts/device/state.json` 并立即执行新闻任务。单次查询只写本次运行偏好，不替换长期订阅。暂停和恢复保留原配置。确认前不改变持久偏好，也不发起 RSS 请求。

应用并行抓取 IT之家、爱范儿、Solidot 与中新网四类主机上的七个 RSS 源，保留最近七天候选并轮询合并。模型根据主题语义、优先级、新闻重要性和减少推荐反馈选择最多八条；候选不足时如实少于八条。列表先显示，随后生成 100–200 字简报并填入顶部。

“快速设置”保留为模型不可用时的固定 AppCard 备用流程。每日运行、15/30 分钟延后提醒仅在应用保持打开时执行，没有后台唤醒。

官方 Shell 的独立 “Ask <app>” 面板使用 `shell-ask` instance，应用无法通过自己的 `octos.session.history` 可靠读取该面板。因此 0.4.4 从应用内“听见顾问”按钮发起 Agent 回合，仍完全使用官方 Shell 和系统问题界面，不自建聊天 UI，也不修改 Shell。

权限：`storage`、`net`、`model`、`glance`、`octos.session.open`、`octos.turn.start`。Agent profile 为 `read-only`，唯一工具为 `ask_user_question`。

验证：Splash 语法、确认边界与 AppCard 写回测试通过；真实 MiniMax-M3 Agent 对话完成渐进提问和最终工具确认；真实结构化模型调用通过；App Hub 检查结果为 `skystream.trendyhear 0.4.4 — PASSED`，当前仅等待发布者重新签名并安装后做最终 Shell 界面验收。
