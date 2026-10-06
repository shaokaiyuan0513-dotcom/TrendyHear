# TrendyHear 0.4.0：官方 Shell 接口版

本说明替代此前要求使用新 Shell 的 0.4.0 验收说明。

## 使用流程

1. 在现有 OctoSense 中更新安装重新签名的 0.4.0，保持 TrendyHear 打开，点击“连接听见顾问”。首次使用仍由系统询问 Agent 授权；授权后可重新连接。
2. 在系统 Ask TrendyHear 输入：“以后优先关注人工智能对设计工作的影响，其次财经，每天 08:30 整理。”顾问通过 ask_user_question 逐项询问缺失信息，整理主题顺序、时间和对需求的理解。
3. 应用读取当前连接之后的顾问答复，发布“确认阅读偏好”AppCard。核对后点击“确认保存”。卡片发布失败时，应用内会提供同一份确认内容。
4. 点击之前，长期偏好不会改变，也不会抓取。点击后，由应用自身把偏好写入 accounts/device/state.json，并立即抓取及语义筛选最多八条，生成 100–200 字简报。临时查询只影响本次任务。
5. 取消、过期、过时或重复确认不会覆盖新偏好或重复启动。修改清单后需确认新卡片。连接监听约十分钟，过期后重新连接即可。

## 官方接口与边界

- octos.session.open：打开应用自己的会话。
- octos.turn.start：把偏好整理说明传入与 Ask 共用的用户通道；无需 Shell 自动安装 AGENT.md。
- octos.session.history：读取带 role/lane 标记的记录，只处理本次初始化消息之后的用户通道答复；旧记录、用户自己发送的清单、系统 Agent 通道均不触发卡片。
- glance.publish：应用发布固定 Splash 模板，模型只提供偏好内容，不编写卡片代码。
- 卡片“确认保存”由应用的 Splash 处理函数写入 confirmed-action.json；应用校验草稿 ID、序号和有效期后，通过自身 fs.write 保存并执行。Agent 没有写文件工具。
- agent.profile 已改回 read-only，agent.tools 仅 ask_user_question。应用自身 storage 权限保留，用于用户确认后的数据保存。
- model.complete 执行后续语义筛选与简报；新闻标签、切换主题重新选取及去掉重复“参考判断”的修复保留。
- 每日运行和延后提醒仅在应用保持打开时生效。没有新增后台唤醒承诺。

接口依据为本地 OctoScript-App-Design-Flow/docs/AI-SERVICES.zh-CN.md 的用户对话、会话服务和 glance 章节，以及 OctoSense crates/app-peers/src/broker.rs 的 merged_history。AppCard 内部只读写本应用账户，不请求宿主弹出额外确认。

## 已验证

- 实际 Makepad Script VM：应用整体语法、确认卡片语法通过。
- 使用网络/模型/UI 替身验证核心流程；运行了卡片实际确认处理函数。覆盖确认前不修改数据、确认后立即抓取、取消、过期、旧回执、用户纠正、重复点击、临时查询隔离，以及此前的个性化列表替换测试。
- App Hub 检查：skystream.trendyhear 0.4.0 — PASSED，仅 unsigned 警告；scan 包和八项问题回答已更新。
- 本轮没有修改或编译 OctoSense；工作区差异与开始时相同。上轮宿主扩展已单独保存为贡献候选，应用包不再调用这些工具。

## 仍待实际验收

本轮按要求不跑图形界面、不发起真实模型调用。现有官方 Shell 中的真实 Ask→清单→AppCard→点击→保存→简报仍需按上述流程验证，不能把模拟检查或包准入当成已完成演示。原截图仍属于 0.3.x。

应用源码位置：<工程目录>/bundle。
没有签名、更新本地 App Hub 目录或替换已安装版本；发布者完成签名和安装后再验证。无需使用上轮编译的新 Shell。

宿主贡献候选位于 outputs/TrendyHear-宿主贡献候选，包含差异快照、新文件与说明。历史 OS 源码修改没有被清理或部署；它们不属于本参赛应用的依赖，也未被认定为官方贡献。
