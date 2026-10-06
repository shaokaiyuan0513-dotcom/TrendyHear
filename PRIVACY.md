# 隐私处理说明

发布者：SkyStream。适用版本：0.4.1。更新日期：2026-10-06。

TrendyHear 在本机自己的 accounts/device 目录保存阅读偏好、确认草稿、新闻摘要、阅读历史、减少推荐反馈和处理记录。确认卡片只在用户点击确认后保存订阅；临时查询不会替换长期订阅。

应用打开时读取本应用的 Ask 会话，将新的用户请求、最近六段相关对话和已保存偏好交给 OctoSense 配置的模型服务，整理确认草稿。新闻整理时发送最多约 25KB 的来源候选及偏好、减少推荐反馈；简报生成只发送选中的新闻标题、主题和摘要。应用不读取其他应用的对话，不接触模型密钥。

应用访问 www.chinanews.com.cn、www.ithome.com、www.ifanr.com、www.solidot.org 的公开新闻订阅源。打开原文由系统处理。模型服务商的数据处理与保留政策由用户选择的服务商决定。应用不提供云同步。

支持与隐私问题：https://github.com/shaokaiyuan0513-dotcom/TrendyHear/issues。请勿在公开 Issue 中附上密钥、个人新闻历史或其他敏感信息。
