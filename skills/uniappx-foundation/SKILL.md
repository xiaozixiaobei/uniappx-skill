---
name: uniappx-foundation
description: Use when creating, configuring, reviewing, or modifying a uni-app X project, choosing Vapor or VDOM, checking HBuilderX compatibility, or handling .uvue, UTS, manifest.json, pages.json and conditional compilation. 适用于工程初始化、开发规范和模式识别。
---

# uni-app X 工程与开发规范

先确认工程事实，再做最小修改。支持 Android、iOS、HarmonyOS App；Web/小程序只补查任务涉及的兼容性。

## 使用流程

1. 读取项目约定、工作区改动、`manifest.json`、`pages.json`、入口、目标页面和依赖；记录项目版本或 Git 提交、目标平台、渲染模式、HBuilderX 版本。`.uvue` 或 `lang="uts"` 单独不能证明使用 VDOM。
2. 新项目依据 [工程与模式选择](references/project-and-modes.md) 核对所有目标平台的 OS、工具链、插件支持条件，满足条件时优先 Vapor。已有项目遵循实际模式；模式迁移单独确认范围并验证。
3. 对变更涉及的 API、组件、样式按版本检查官方支持，保持现有结构和代码风格。只补充任务需要的配置、类型及条件编译。
4. 从项目已有脚本、已安装工具帮助及对应官方文档确定命令。不存在的 `package.json` 脚本、普通 uni-app 的 npm 模板、通用 TypeScript 检查不能冒充 uni-app X App 工具链。
5. 编译受影响的平台并验证行为；环境不足时列出具体待验证项。

## 交付约定

输出：适用条件（项目版本／平台／模式／工具版本）、修改与理由、验证证据、问题及下一步。阶段结果为**通过／阻塞／不适用**；必需验证未完成归为阻塞原因，不影响继续处理独立任务。只有存在适用范围及证据的不适用项才能排除。

将明确的官方要求、项目/团队约定、推荐实践分别标识。当前版本不明或官方资料不可访问时，不把推断写成支持结论。保存检查记录只在任务需要时进行；上下文改变后重查受影响项。

## 按需资料

- [工程与模式选择](references/project-and-modes.md)：新建工程、版本矩阵、代码规范及迁移边界。
- [官方来源记录](references/sources.json)：逐条记录来源、2026-11-04 核验状态与适用范围；快照不能证明未来版本。

后续可单独调用 `uniappx-api`、`uniappx-ui`、`uniappx-quality`；本流程不强制加载其他阶段。
