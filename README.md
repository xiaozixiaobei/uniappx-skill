# uniappx-skill

面向 AI 编程助手的中文 uni-app X 全流程技能包：一个总控按需调用七个阶段技能，各阶段也可独立使用。App 优先，覆盖 Android、iOS、HarmonyOS；Web/小程序只检查任务涉及的兼容性。

## 技能

| 技能 | 用途 |
|---|---|
| [uniappx-workflow](skills/uniappx-workflow/SKILL.md) | 总控、阶段选择、证据交接 |
| [uniappx-foundation](skills/uniappx-foundation/SKILL.md) | 初始化、工程规范、Vapor/VDOM 和版本识别 |
| [uniappx-api](skills/uniappx-api/SKILL.md) | 官方 API、业务 HTTP、SDK 与原生能力 |
| [uniappx-ui](skills/uniappx-ui/SKILL.md) | 组件、样式、交互、长列表与跨端适配 |
| [uniappx-privacy](skills/uniappx-privacy/SKILL.md) | 隐私同意、系统权限、数据/SDK 清单 |
| [uniappx-quality](skills/uniappx-quality/SKILL.md) | 功能回归、真机、性能及验收证据 |
| [uniappx-build](skills/uniappx-build/SKILL.md) | Android/iOS/鸿蒙分平台构建、签名和产物 |
| [uniappx-store-publish](skills/uniappx-store-publish/SKILL.md) | Apple 中国区、华为、小米、OPPO、vivo、应用宝 |

根目录 [SKILL.md](SKILL.md) 保留 `uniappx-skill` 名称作为旧安装方式的兼容入口，指向正式总控；它不是新增的第九个阶段。

## 接入与使用

推荐把 `skills/` 下八个技能目录**作为一个安装单元，保持同级**放入工具的技能目录。Codex 默认使用 `~/.codex/skills/`；设置了 `CODEX_HOME` 时使用其 `skills/` 子目录。安装前检查同名目录，已有内容先比较或备份，不直接覆盖。其他支持 `SKILL.md` 的助手按其机制接入，必要时显式读取技能文件。

若工具按整个仓库根目录接入，保留完整 `skills/` 子目录，根兼容入口才能继续路由。不要只复制根 `SKILL.md`。

调用总控时无需声明阶段，例如：

```text
使用 $uniappx-workflow 为当前 uni-app X 项目实现订单列表，检查 Android/iOS 兼容性。
使用 $uniappx-workflow 检查现有 VDOM 工程的 API 超时问题，保持当前渲染模式。
使用 $uniappx-workflow 为本次版本准备小米和 Apple 中国区上架材料，列出缺项。
```

也可直接调用流程：

```text
使用 $uniappx-ui 修复 Vapor list-view 项目复用后的状态错乱。
使用 $uniappx-privacy 检查统计 SDK 的同意前初始化和撤回路径。
使用 $uniappx-build 核验 Android/iOS 的应用标识、签名与正式产物。
```

首次需要项目/平台/模式/工具版本时先从工程读取；仅对无法发现且影响方案的信息提问。当前任务只加载需要的阶段和参考资料。流程调用不要求 agent、联网服务或额外运行时；涉及当前技术支持和商店条款时仍需要访问官方来源。

每个结论包含适用条件、执行内容、证据、结果/问题及下一步。结果为**通过／阻塞／不适用**；必要检查尚未验证时列为阻塞原因，其他独立工作可继续。技能提供流程指引，不是自动强制执行的 CI 或应用商店认证。

## 资料状态与维护

官方来源核验日期：**2026-11-04**。每个技能自己的 `references/sources.json` 记录 URL、读取状态、正文哈希、日期与适用范围。`verified` 表示已取得对应主题的正文，不代表已核实全部当前公告；`entry-only` 表示只确认入口，具体条款仍待核验；`pending` 表示尚未成功获取。

- DCloud 已取得工程、Vapor、请求、组件/样式、隐私、打包及测试等相关正文。
- Apple 已取得审核、隐私及提交准备正文；当前 SDK 门槛及生效日需在每次发布前重新核对，不从历史或未来公告直接推导。
- 小米已取得开发者生态政策和权限申请正文，避免把门户自身隐私政策误作应用审核细则。
- 华为、OPPO、vivo、应用宝目前只确认官方入口，详细审核条款待任务执行时取得，不据此报告这些渠道准备通过。
- 官方 CLI 入口本轮只返回页面壳；本包不编造创建/发行命令，使用时核对对应版本正文和本机帮助。

新增或更新规则时区分官方要求、团队约定和建议，记录平台、模式、版本与来源；商店规则在实际发布前重新核验。新项目满足官方支持条件时优先 Vapor；既有项目不因小修改被自动迁移。发布动作按具体任务授权执行，阅读技能本身不授权对外上传或提审。

## 验证

本包是技能文档，不是 App 源码，不包含任何真实应用的打包或上架通过声明。

在仓库根目录运行：

```sh
python3 -m unittest discover -s tests -v
```

自动检查八技能完整性、元数据/来源记录、本地引用和总控路由；[行为场景](tests/scenarios.md) 用于人工或独立 agent 验收。若环境提供 `skill-creator`，还可逐个运行其 `quick_validate.py`。自动结构检查不能证明流程判断、示例编译或真实商店审核一定正确。

## 贡献

欢迎提交可复现的问题和有官方依据的修订。仅修改相关阶段及其来源记录，并重跑结构检查与受影响行为场景；不要复制整站手册或把某次经验推广成所有平台的固定规则。
