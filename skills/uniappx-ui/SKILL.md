---
name: uniappx-ui
description: Use when implementing or reviewing uni-app X pages, built-in or custom components, Vapor CSS, list-view recycling, scrolling, forms, keyboard behavior, safe areas, responsive layouts or UI library compatibility. 适用于组件、样式与交互开发。
---

# uni-app X UI 组件与样式

根据平台、模式与工具版本选择组件和样式；界面目标以用户需求和现有设计为准，不额外规定视觉风格或引入 UI 库。

## 使用流程

1. 读取目标页面、相关组件、页面路由、全局样式和依赖，确认项目版本、目标设备、Vapor/VDOM、HBuilderX 版本与已有 UI 约定。
2. 从内置组件和项目已有组件中选择最小方案。按 [组件与布局](references/components-and-layout.md) 核对具体属性、事件、插槽及模式限制。
3. 明确布局/滚动容器、尺寸、键盘与安全区处理，补充加载、空、失败、禁用、重复操作等任务相关状态。按模式处理样式隔离和长列表复用。
4. 引入第三方组件前核对 uni-app X、目标平台、渲染模式和依赖版本，实际运行最小示例。插件市场“支持 Vue3”不等同于支持目标 App 模式。
5. 在受影响 App 平台编译并验证交互；Web/小程序单独检查所用能力。Web 截图或运行结果不替代原生 App 验收。

## 交付

输出适用条件、组件与样式改动、交互验证证据、问题和下一步。结果为**通过／阻塞／不适用**；编译失败或必要设备验证缺失时不报通过。不适用需说明依据，风格优化仅作建议。

区分官方要求、项目约定和推荐实践；结论绑定项目版本／平台／模式／工具版本。相关条件变化后重查；资料缺失时标待核验，不猜属性或跨端效果。

## 按需资料

- [组件与布局](references/components-and-layout.md)：Vapor CSS、隔离、长列表示例与 UI 验收。
- [官方来源记录](references/sources.json)：组件/样式官方文档与核验范围。
