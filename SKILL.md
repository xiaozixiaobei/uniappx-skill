---
name: uniappx-skill
description: Use when working on uni-app X projects across engineering, Vapor/VDOM, APIs, UI, privacy, testing, App packaging, signing, Chinese store release or review rejection. 适用于开发规范、API 与组件、隐私权限、测试验收、Android/iOS/鸿蒙打包及中国主要商店上架的兼容入口。
---

# uni-app X 兼容入口

此入口保留原有技能名称 `uniappx-skill`，供按仓库根目录接入的工具使用。

先读取并执行本仓库的 [uniappx-workflow](skills/uniappx-workflow/SKILL.md)，再按当前任务只读取它路由到的流程技能。不预加载整个目录，不另建代理或线程。

正式技能共八个，均在 `skills/` 下；可作为同级目录一起安装，之后使用 `$uniappx-workflow` 或直接使用某个阶段技能。若只复制本文件而未保留 `skills/`，报告缺少总控与流程文件，不能退回未经核验的旧规则。

以当前工程及官方文档为准，做最小且可验证的改动；保留用户已有修改。具体规则、证据和交付约定由正式技能定义。
