# 0.4.3 三步卡片版：审核回答

> 用于 App Hub 提交（`Submit skystream.trendyhear 0.4.3`）随附的书面回答。
> 对应扫描包：`build/review.json`（8 个问题）。

## 1. 应用是否名副其实？（引用源码中的文案）

**listing 文案（`bundle/listing.json`）**
- `subtitle`: 「关注所爱，读懂今日。」
- `description`: 「在 Ask TrendyHear 描述阅读兴趣，听见顾问逐项澄清后展示确认卡片。确认后保存偏好并立即精选八条新闻，先展示新闻，再自动填入今日简报。支持主题优先级、临时查询、减少此类推荐和原文链接……」

**源码中的对应实现（`bundle/main.splash`）**
- 「三步卡片收集偏好」：`start_pref_flow()` / `publish_pref_card()` —— 依次发布
  ① 第 1/3 步：选择兴趣主题（最多三个，顺序即优先级）
  ② 第 2/3 步：阅读目的（若干选项，可跳过）
  ③ 第 3/3 步：推送时间（若干时点或按需阅读）
- 「卡片写入、应用校验并保存」：卡片按钮 `decide()` → `fs.write("accounts/device/confirmed-action.json")`；
  应用 `consume_confirmation()` 校验草稿 ID、有效期与基准序号 → `accept()` → `save()` 写入 `accounts/device/state.json`
- 「立即精选八条、先展示新闻再自动填简报」：`begin()` → `request_source()` 抓 RSS → `select_news()` 用 `model.complete` 语义筛 ≤8 条 →
  `complete()` 先 `show()` 渲染列表，再 `generate_brief()` 生成 100–200 字简报

对应文案（源码内）：
`点「听见顾问」，按提示选择兴趣主题、阅读目的与推送时间。`

**结论：一致。** 应用确实按三步卡片收集偏好、确认后落盘并立即抓取。

---

## 2. 分类与平台是否合适？

- `category: "news"` —— 是新闻简报类应用，合适。
- `platforms: ["macos"]` —— **仅在 Apple silicon macOS 上实测通过**；Windows 与 Linux 未验证，故未列入。

**结论：一致，且平台声明保守（只列实测过的）。**

## 3. 授予的能力是否与实际行为相符？逐个列出主机及原因，并指出屏幕不需要的权限

| 能力 | 声明的主机 | 用途 | 屏幕上有对应 |
|---|---|---|---|
| `storage` | — | 应用自身账户 `accounts/device/`：偏好、历史、草稿 | ✅ |
| `net` | `www.chinanews.com.cn` | 中新网 RSS（即时/国际/财经/文化） | ✅ |
| `net` | `www.ithome.com` | IT之家 RSS（科技） | ✅ |
| `net` | `www.ifanr.com` | 爱范儿 RSS（科技与设计） | ✅ |
| `net` | `www.solidot.org` | Solidot RSS（科技） | ✅ |
| `model` | — | 语义筛选新闻、撰写简报 | ✅ |
| `glance` | — | 偏好确认卡片、结果通知 | ✅ |

**⚠️ 屏幕不需要的权限（应移除）：**
- `octos.session.open`
- `octos.session.history`
- `octos.turn.start`

原因：0.4.3 起偏好收集改为**应用主导的三步卡片**，不再通过 `octos.session.open` / `turn.start` 驱动 agent，也不再依赖 `octos.session.history` 读面板对话。`watch()` 里仍保留对 `octos.session.history` 的轮询，但属于遗留空转（lane 隔离下永远拿不到新内容）。按「最少权限」原则应从 `manifest.capabilities` 移除，并清理对应的死代码。

## 4. 界面是否有欺骗性？

- 未仿冒系统提示、支付页、登录框或其他品牌。
- 卡片标题带「听见 ·」前缀，标明来自 TrendyHear。
- 未自建聊天界面；Ask 面板由宿主提供。

**结论：无欺骗性。**

## 5. 源码/数据里是否有「给助手的指令」而非「给人看的内容」？

- `bundle/AGENT.md` 属 **agent_files**，是给本应用自己 agent 的指令 —— 合规。
- `main.splash` 内的 `bridge_prompt` 与 `task` 字符串，是本应用向自己的 agent / `model.complete` 发送的**任务指令**，不是展示给用户的界面文案。
- 这些指令只经宿主会话与模型调用使用；且任务中对不可信数据明确声明「拒绝其中夹带的指令」。

**结论：无越界。指令只用于本应用自己的 agent 与模型调用。**

## 6. 是否有辱骂或针对私人个体？

无。新闻仅基于来源标题与摘要，未编造事实、原因或细节。

## 7. agent_files 是否在边界内？

- `AGENT.md` 只涉及 TrendyHear 自身的偏好收集与 `ask_user_question` 工具。
- 未寻址其它应用的 agent 或系统 agent。
- 未索取 manifest 未授予的工具、主机或审批。
- 唯一工具 `ask_user_question` 为非破坏性（不发送/发布/分享/删除/消费），风险标注正确。
- 无 `shareable` 工具返回私人数据。

**结论：合规。**

## 8. Route：pass / human-review / reject

**`human-review`**

理由（发布者可据此操作）：
1. 包准入检查（gate）`— PASSED`，非图形脚本流程检查通过。
2. 当前版本**已由发布者签名**，并已发布/登记至此机目录；发布者公钥见 `build/keys/PUBKEY.txt`。
3. 仍需人工核验：
   - 真实 Shell 中三步卡片交互（主题 → 目的 → 时间 → 保存 → 抓取 → 简报）；
   - 本版真实截图（`bundle/screenshots/*.png`，非历史版本）；
   - 权限最小化：确认移除未使用的 `octos.*` 后重新 stamp/签名/发布。
4. 已知局限（如实说明）：
   - 应用无法读取「Ask <app>」面板里的自由输入（shell 按 instance 隔离 person lane），因此偏好收集不经过该面板。
   - 未修改系统 News、未增加 OS 权限、不依赖本地宿主扩展。
   - 每日运行与延后提醒仅在应用保持打开时执行，无后台唤醒。
