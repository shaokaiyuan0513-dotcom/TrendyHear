# Submit skystream.trendyhear 0.3.3

> 草稿，尚未提交；公开代码、标签及完整提交号确定后提交。本版本是 2026-10-05 快照，不冒充此前版本。

队伍：SkyStream；成员：Leah、FruitShow。
应用：听见 · 新闻简报，OctoSense 原生新闻订阅与按需摘要应用。

- Public repository: https://github.com/shaokaiyuan0513-dotcom/TrendyHear  （待确认）
- Tag: v0.3.3（上传后创建）
- Full commit SHA: 待公开仓库最终提交
- Bundle path: bundle/
- Publisher ID: skystream（已签名）
- Publisher public key: `196afc83f7ab4d724e322b7928838a5ebfd2f0abc839774020188d1ea7950114`
- Bundle blake3: `57cd4621551e551634d19b5385fe37957aa24b5f1d3e1bc4474a3ed651af84e4`
- Host: OctoSense 127ae4bd5a5476f0b813179868e61f80748a044e；App Hub 0d5b47a2ae9eb98020feca26b7c895a3cf797dc1
- Verified platform: Apple Silicon macOS；独立原型为 macOS 13+

功能边界（0.3.3）：
- 应用侧：手动更新中新网 RSS（每天最多 8 条）、阅读与偏好、「同步偏好给顾问」按钮（octos.turn.start 把已选兴趣/重点/用途推给 Agent，减少追问）、「生成今日简报」由 octos.turn.start 发起并用 octos.session.history 定时回读对话、把结构化简报填回界面，形成闭环。
- 数据路径已落在账户目录 `accounts/device/`（state.json / agent-context.json），听见顾问可直接读取。
- Ask 面板（系统）基于已采集新闻生成综述，不自行联网抓取；若会话后续挂载 news/web 工具可按需补充并标注来源。
- 无语音播报、后台定时推送、自动修改长期订阅。

附件：build/hub-check.txt、build/review.json、build/REVIEW-ANSWERS.md（待按最终源码核对）；演示视频、截图、来源与限制、操作结果与成员名单另附。

提交方式：在 OctoSense-org/OctoSense-App-Hub 开 Issue，标题即本文标题。不要修改该仓库 catalog.json、index/ 或 artifacts/。最终 catalog 发布需维护者用 Hub anchor 写入（同 0.3.1/0.3.2）。

官方契约：https://github.com/OctoSense-org/OctoSense-App-Hub/blob/main/docs/PUBLISHING.md#submitting
