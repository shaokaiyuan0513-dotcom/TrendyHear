# 0.4.0 官方 Shell 适配：审核回答

1. 功能：connect/consider_history/proposal_from_text 将 Ask 里的偏好清单转换为待确认草稿；stage_proposal 发布卡片；consume_confirmation/accept 在点击后保存并执行。select_news/complete 生成和替换新闻结果。真实 Shell 效果待验收。
2. 分类 news，平台保留历史已验证的 macos；当前新版界面未运行，现有截图是旧版。
3. 权限：storage 为应用自身保存、net 只访问 www.chinanews.com.cn RSS、model 语义整理、glance 确认/结果卡片、octos.session.open/history/turn.start 连接及读取本应用对话。所有权限有对应执行路径；Agent 仅 ask_user_question、read-only。
4. 无仿冒系统登录或授权界面。卡片清楚展示应用偏好和具体操作；Ask 由宿主提供，无自建聊天。
5. 指令文本是本应用向自己的 Agent 发送的偏好整理任务，以及向 model.complete 发送的有界整理任务。RSS/偏好通过数据参数传入；模型不编写可执行卡片代码。
6. 无攻击私人个体或辱骂文字，新闻仅基于来源摘要。
7. Agent 不写入或调用 storage.read/write。所有持久修改与抓取由用户点击确认后的应用函数执行。无自定义 shareable 工具或跨应用访问；卡片仅操作发布应用的账户。草稿关联 ID、顺序号与有效期防止旧确认覆盖新偏好。取消不执行。
8. human-review：准入和模拟检查通过，正式提交仍需真实 Shell 演示、新截图与发布者签名。本版不再依赖宿主扩展；不能把接口适配等同真实演示成功。
