# TrendyHear · 听见新闻简报应用

OctoSense 原生新闻阅读与摘要应用，版本 0.3.0，ID `news.tingjian-native`。

## 文件

`bundle/main.splash` 为产品源码，`manifest.json` 声明权限，`listing.json` 为应用资料，`assets/` 为图标，`screenshots/` 为真实界面截图。仅 bundle 是 Hub 应用包；运行环境与说明独立交付。

## 在官方开发环境运行

使用 OctoScript-App-Design-Flow，按其 QUICKSTART 配置 hub 与 card-host，然后：

```sh
tools/octo run /absolute/path/to/bundle --port 8141 --hidden --detach
tools/octo shot 8141 /tmp/tingjian.png
tools/octo check /absolute/path/to/bundle
curl -s http://127.0.0.1:8141/quit
```

独立 card-host 不提供模型服务，AI 整理必须在真实 OctoSense 宿主中验证。同行交付的 Mac 应用包含本机签名目录；正式发布按 App Hub PUBLISHING.md 操作，不能提交本地签名密钥冒充正式身份。

当前已验证：Apple 芯片 macOS 下真实原生界面、网络更新、存储与已有模型结果展示。未验证：其他平台、独立安装包在另一台实体 Mac 上的模型付费生成、最新提示词的真实输出。

新闻内容归原来源所有；代码采用 Apache 2.0，见 LICENSE。发布者 SkyStream；支持渠道为本仓库 Issues；隐私说明见 [PRIVACY.md](PRIVACY.md)。首次提交使用 unsigned，等待 App Hub 人工审核。

依赖：OctoSense 源码提交 `127ae4bd5a5476f0b813179868e61f80748a044e`；App Hub `0d5b47a2ae9eb98020feca26b7c895a3cf797dc1`。精确本机运行制品校验见交付说明。

公开仓库：[TrendyHear](https://github.com/shaokaiyuan0513-dotcom/TrendyHear)。
本次提交版本：v0.3.0 

## 演示和证据

[真实操作视频](submission/演示视频/听见新闻-实际操作演示.mp4)、[需求说明](submission/需求说明/需求说明.md)、[数据来源与限制](submission/数据来源与限制/数据来源与限制.md)、[成员名单](submission/成员名单/已报名成员名单.md)。真实截图位于 bundle/screenshots/。验证记录在 submission/操作与结果证据/。

队伍：SkyStream
成员：Leah、FruitShow
