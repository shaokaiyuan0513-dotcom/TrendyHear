# 隐私处理说明

发布者：SkyStream。适用版本：0.4.4。更新日期：2026-10-06。

TrendyHear 在本应用的 `accounts/device` 目录保存阅读偏好、确认草稿、新闻摘要、阅读历史、减少推荐反馈和任务记录。只有用户点击偏好 AppCard 中的“确认保存”后，长期订阅才会写入；单次查询不会替换长期订阅。

用户点击“听见顾问”后，OctoSense 的 Octos Agent 会通过用户已配置的模型服务理解回答并提出问题。应用收到 Agent 的最终复述后，会把这段结果和已有偏好交给 OctoSense 的 `model.complete` 服务做结构化校验。应用不会读取其他应用的会话，也不会接触模型 API 密钥。Agent 对话的处理和保留由 OctoSense 及用户选择的模型服务商决定。

新闻整理时，应用会把主题偏好、减少推荐反馈以及公开 RSS 候选的标题、来源主题和摘要发送给 OctoSense 配置的模型服务，用于选择新闻。简报生成只发送已选新闻的标题、主题和摘要。

应用访问 `www.chinanews.com.cn`、`www.ithome.com`、`www.ifanr.com`、`www.solidot.org` 的公开新闻订阅源。打开原文由系统处理。应用不提供云同步。

支持与隐私问题：https://github.com/shaokaiyuan0513-dotcom/TrendyHear/issues。请勿在公开 Issue 中附上密钥、个人新闻历史或其他敏感信息。
