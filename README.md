# TrendyHear · 听见 0.4.3

现有 OctoSense 官方 Shell 接口版，独立 App Hub 应用，ID `skystream.trendyhear`。阅读偏好由三步系统卡片收集，选完由应用保存并立即执行。

保持应用打开，点「听见顾问」即开始：应用依次推送三张固定模板卡片——① 兴趣主题（最多三个，顺序即优先级）② 阅读目的（若干选项，可跳过）③ 推送时间（若干时点或按需阅读）。三步选完，应用把偏好写入 `accounts/device/state.json`，并立即从 RSS 抓取、语义筛选最多八条、生成 100–200 字简报，按主题优先级与重要性排序。支持临时查询不改订阅、减少推荐反馈、主题标签、通知和阅读历史。每日运行及延后提醒只在应用保持打开时执行。

偏好收集不经过 Ask 面板：Shell 的「Ask <app>」面板使用 instance `shell-ask`，而应用 `octos.session.open` 使用 `card.<app id>-gN`；`octos.session.history` 只合并调用方自身 instance 的人这一侧 lane（crates/app-peers/src/broker.rs:3144-3145），应用读不到面板里的自由输入，因此改为应用主导的卡片流程。卡片由应用使用 `glance.publish` 发布，选择结果写回 `accounts/device/pref-answer.json`，应用校验后推进下一步，并以自身 `fs.write` 落盘。Agent 为 read-only，仅保留 `ask_user_question`；不依赖 `storage.read/write` 宿主扩展或 Shell 加载 AGENT.md，也不自建聊天界面。

源码为 `bundle/main.splash`（Makepad Script / Splash）；`bundle/AGENT.md` 记录同一份顾问指令。需求见 `BRIEF.md`，检查与实际验收步骤见 `build/VERIFICATION-0.4.0.md`。

已通过包准入及非图形脚本流程检查；并已在真实 Shell 中完成卡片交互与模型效果验收（三步卡片 → 保存偏好 → 抓取新闻 → 生成简报）。已由发布者签名、发布到本机 App Hub 目录并在 Shell 中安装运行。`bundle/screenshots` 为本版真实截图。

发布者 SkyStream，代码 Apache-2.0。新闻归原来源所有；隐私说明见 PRIVACY.md。宿主能力扩展单独存为贡献候选，参赛应用无需使用上轮编译的新 Shell。
