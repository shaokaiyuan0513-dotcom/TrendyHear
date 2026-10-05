# Hub 扫描问题回答 — news.tingjian-native 0.3.0

1. **名称和功能是否相符？** main.splash 的 today/history/settings/status 四页提供兴趣、新闻订阅、阅读状态、偏好、历史及按需摘要。名称“听见”是品牌，不表示已有语音。无后台自动运行或自主 Agent 工具。原始 AI 生成已在 0.2.0-validation 验证；0.3.0 的新提示词未付费复测。
2. **平台与分类是否相符？** news 分类合理。只声明 macos；已在 Apple 芯片 Mac 上检查原生界面与独立路径启动，Intel、其他操作系统未验证。
3. **权限与网络目标是否必要？** storage 写入 state.json 和 model-receipt.json；net 读取 www.chinanews.com.cn 的四个 HTTPS RSS；model 由明确按钮调用 model.complete，最多一次每日逻辑请求、每次两条。没有 llm、octos、microphone、web 等额外权限；应用不执行自身 Agent 工具。
4. **是否有欺骗性界面？** 没有仿系统授权、付款或登录表单，也没有收集凭据。数据源与 AI 标识清楚；公开订阅内容不包装成自采报道。listing 发布者为 SkyStream，支持为仓库 Issues，隐私说明为 PRIVACY.md。
5. **是否含面向助手的指令？** model.complete 的 task 是此摘要功能的固定指令；用户用途与 RSS 内容作为数据，schema 限制输出字段。没有 AGENT.md、可执行工具或后台指令，模型无网络和工具调用权限。仍需考虑恶意来源文本的影响，不声称完全防止提示注入。
6. **是否含辱骂或针对私人个体？** 应用固定文案没有。新闻文本归属公开来源，不以应用自身观点攻击个人；动态订阅内容未预先人工审阅。
7. **建议路线？** HUMAN-REVIEW，首次 unsigned 提交。已有包检查与实际原生运行证据、公开源码与隐私说明；维护者需审核，尚未上架。此回答是作者侧的书面自查，不声称获维护者审核通过。
