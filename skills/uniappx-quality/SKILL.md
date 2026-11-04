---
name: uniappx-quality
description: Use when testing, reproducing regressions, reviewing verification evidence or deciding readiness for a uni-app X change or App release, including real-device, compatibility, performance and missing-environment checks. 适用于开发验收与发布前测试。
---

# uni-app X 测试与验收

按变更风险和实际目标选择必要验证；每个通过结论都对应真实证据，不强制所有小修复跑完整发布矩阵。

## 使用流程

1. 读变更、项目既有检查和测试环境；记录项目版本、目标平台、模式、HBuilderX、设备/系统、构建类型及 SDK 版本。
2. 根据 [测试与证据](references/testing-and-evidence.md) 明确本次验收范围。修复缺陷先重现原行为；可自动化时使用有意义的回归用例，不为静态文案或可逆小改动构造与实现同义的测试。
3. 从仓库脚本、工具帮助和官方文档确认命令，执行适用检查；真实编译/设备测试与测试替身结果分别报告。自动化插件的支持平台按版本确认。
4. 变更影响隐私、权限、SDK 或签名/打包时补相关验证；发布任务检查目标渠道实际候选包，不能用标准调试基座代替。
5. 根据结果定位问题，修复后重跑失败项和受影响检查。已经通过的无关检查不反复扩大执行。

## 交付

输出适用条件、执行命令或手动步骤、结果与证据、未覆盖项和下一步。结果为**通过／阻塞／不适用**；必要项待验证作为阻塞原因，不转成“默认通过”。Web 成功、编辑器无错误、静态检查和过去版本的测试不能替代当前 App 验收。

规则注明官方要求／团队基线／建议。上下文变化时仅重查受影响证据：代码、目标 OS、模式、工具链、依赖、签名或渠道变化都可能使旧结果失效。记录需保存时使用普通 Markdown，无需额外状态系统。

## 按需资料

- [测试与证据](references/testing-and-evidence.md)：风险矩阵、真机和性能验证、报告格式。
- [官方来源记录](references/sources.json)：测试工具和框架事实。
