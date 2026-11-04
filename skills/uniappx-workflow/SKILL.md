---
name: uniappx-workflow
description: Use when a uni-app X task spans development stages or needs workflow selection, project-to-release guidance, compatibility assessment or a coordinated readiness review for Android, iOS and HarmonyOS Apps. 适用于 uni-app X 全流程总控及阶段不明确的任务。
---

# uni-app X 全流程总控

按任务调用必要流程，每个阶段可以直接进入。目标为 Android/iOS/鸿蒙 App；Web/小程序做涉及能力的兼容性检查。中国主要商店为 Apple 中国区、华为、小米、OPPO、vivo、应用宝。

## 开始与路由

1. 读取用户目标、项目约定和相关工程事实：源码/应用版本、目标平台、Vapor/VDOM、HBuilderX/插件版本。优先从工程发现；仅对影响方案且无法发现的信息提问。
2. 定义本次成功标准，再从下表选择**最少必要流程**。用户只改 UI 且工程上下文充分时直接进入 UI；不机械重跑初始化和全套上架检查。
3. 宿主有技能调用能力且目标技能已注册时按精确名称加载；未注册或没有调用工具时，读取表中相对链接指向的 `SKILL.md` 并执行其指令。根兼容入口方式不要求子技能注册。调用流程不要求新建 agent、线程或外部任务。仅在当前任务需要时读子技能所链接的参考资料，不预读全部技能。

| 当前任务 | 应加载的正式技能 | 必要关联 |
|---|---|---|
| 新建/工程配置、模式或语言选择、升级迁移 | [uniappx-foundation](../uniappx-foundation/SKILL.md) | 相关 API/UI 变更再加载对应流程 |
| HTTP/官方 API、存储/设备/SDK/原生能力 | [uniappx-api](../uniappx-api/SKILL.md) | 数据/权限/SDK 隐私行为触发 privacy |
| 页面、组件、样式、长列表、UI 库适配 | [uniappx-ui](../uniappx-ui/SKILL.md) | 本任务需要交互验收时触发 quality |
| 同意、权限、SDK 披露、撤回/注销 | [uniappx-privacy](../uniappx-privacy/SKILL.md) | 商店具体条款交 store-publish |
| Bug 重现、回归、真机/性能、验收结论 | [uniappx-quality](../uniappx-quality/SKILL.md) | 根据问题定位回到对应开发流程 |
| Android/iOS/鸿蒙打包、签名与产物 | [uniappx-build](../uniappx-build/SKILL.md) | 候选包验证交 quality；提审交 store-publish |
| 上架材料、渠道差异、提审或审核驳回 | [uniappx-store-publish](../uniappx-store-publish/SKILL.md) | 只补必要的 build/quality/privacy 证据 |

子技能文件缺失时报告精确缺少的技能与受影响任务；不静默套用旧 uni-app 技能。八个目录保持同级，作为一个安装单元；本仓库中均位于 `skills/` 下。

## 共用决策与交接

- 新项目符合官方支持条件时优先 Vapor；已有工程先识别模式，迁移是独立任务。API/组件/参数/插件逐项核对目标平台和工具版本，不能因“支持 Vue3”推导支持原生 App。
- 当前规则按对应官方文档核验。注明官方要求、团队约定或推荐实践，保留来源、适用范围和日期。商店规则在实际发布前重新核验；只有入口或旧快照不证明最新条款。
- 输出依次包含：**适用条件、执行内容、证据、结果与问题、下一步**。结果为**通过／阻塞／不适用**，注明验收范围；必需项待验证是阻塞原因。不适用有依据，其他独立工作继续。
- 每份结论绑定源码/应用版本、目标平台、模式、工具/SDK版本；构建/发布另绑定包哈希与签名身份、渠道/地区。条件变化时只重查受影响项。按需用普通 Markdown 保存交接记录，不建状态服务。
- 编译失败、平台不支持、签名错误、已确认的必要合规缺项阻止相关阶段通过。风格建议不阻塞。缺设备/证书/资料不能伪装为已验证，Web/Mock/标准基座不能替代对应正式 App 证据。
- 根据当前用户已有授权执行工作。先完成可审阅的配置与发布材料；上传、提审、付费、协议接受或线上操作受具体授权及工具规则约束，不推导额外权限、不重复询问已授权动作。

## 资料

- [阶段进入与交接示例](references/routing-and-handoff.md)：跨阶段任务、拒审和证据失效处理。
- [官方来源记录](references/sources.json)：工程/Vapor 依据；各阶段的具体来源在其自身目录内。
