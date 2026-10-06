# TrendyHear 0.4.3：现有官方 Shell

主要目标：以三步系统卡片收集阅读偏好，保存后由应用立即精选新闻。

交互：点「听见顾问」后，应用依次推送三张固定模板卡片——① 兴趣主题（最多三个，顺序即优先级）② 阅读目的（若干选项，可跳过）③ 推送时间（若干时点或按需阅读）。每张卡片的按钮把选择写回 accounts/device/pref-answer.json，应用校验后进入下一步；三步选完即写入 accounts/device/state.json 并立即抓取新闻。卡片由应用自己发布并校验，不依赖面板自由输入的自动识别。

关于官方会话：Shell 的「Ask <app>」面板使用 instance `shell-ask`，而应用 octos.session.open 使用 `card.<app id>-gN`；octos.session.history 只合并调用方自身 instance 的人这一侧 lane（crates/app-peers/src/broker.rs:3144-3145），应用读不到面板里的自由输入。因此偏好收集改为应用主导的卡片流程，不依赖该通道。

保存订阅后立即抓取四个既有中新网 RSS，近七十二小时最多四十个候选，再通过一次 model.complete 语义筛选最多八条、生成 100–200 字简报，按主题优先级及重要性排序。本次列表由新结果替换；历史保留。临时查询不改订阅。减少推荐记录内容语义特征并可撤销。

glance 用于偏好卡片与结果通知；每日运行、十五/三十分钟延后和今日不再通知仅在应用打开时执行。无后台唤醒。立即查看沿用 Shell 的卡片应用入口。

权限：storage 用于应用自身账户数据；net 仅 www.chinanews.com.cn；model 用于语义整理；glance 用于卡片。agent.profile=read-only，tools 仅 ask_user_question；当前版本偏好收集不经过该 agent（声明保留以备后续自然语言入口）。AGENT.md 不要求宿主加载。

不修改系统 News，不增加 OS 权限，不依赖本地宿主扩展，不自建聊天 UI。本轮不修改 OctoSense Shell：宿主改动仅作为独立贡献候选，参赛应用不依赖它。card-host 无头运行已通过（gate PASSED、首帧绘制、运行日志无错误）；真实 Shell 与模型效果由用户验收。截图为本版真实截图，不用旧版截图冒充。
