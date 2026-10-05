# GitHub 提交操作说明

目标为 OctoSense-org/OctoSense-App-Hub 的 Issue，不修改其 catalog.json、index/ 或 artifacts/。

1. 确认发布者名称、支持联系和真实隐私政策 URL，替换 bundle/listing.json 的占位字段。
2. 重新 stamp、check 和 scan；核对 build/REVIEW-ANSWERS.md 与最终源码相符。
3. 按团队确认的签名方式处理。用户给定流程要求正式发布者本人生成、保管仓库外的长期密钥并签名；本机原型的临时签名不可用于正式提交。官方契约允许首次未签名提交，如决定使用该方式，要在 Issue 中明确写 unsigned，不伪装成已签名。
4. 将本目录源码发布到队伍自己的公开仓库，提交最终字节并打版本 tag。只有最终签名后不会再改动的提交可以作为发布引用。
5. 将「01-可运行原型」和演示视频作为 Release 附件或赛务认可的可访问附件；不要把开发工具链、缓存或模型账号目录提交到仓库。
6. 复制 build/SUBMISSION.md，填写公开仓库、tag、完整 commit SHA、bundle 路径、公钥或 unsigned，并附最终 hub check 输出与七项审核回答，在 App Hub 创建 `Submit news.tingjian-native 0.3.0` Issue。
7. 等维护者在完全相同的字节上审核与发布；Issue 创建、准入通过和上架是不同状态，应分别记录。

当前障碍：本机 GitHub 登录凭据失效，公开仓库未指定，正式发布者、支持方式和隐私政策 URL 未提供。以上状态不能用示例网址或本地提交号替代。

官方契约：https://github.com/OctoSense-org/OctoSense-App-Hub/blob/main/docs/PUBLISHING.md#submitting
