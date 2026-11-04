---
name: uniappx-api
description: Use when integrating or debugging uni-app X APIs, uni.request, HTTP services, uploads, storage, files, media, location, device capabilities, UTS plugins or native SDKs, including platform-specific failures. 适用于 API 调用与原生能力接入。
---

# uni-app X API 与原生能力

基于项目实际模式和平台选择能力，先确认契约再实现调用。业务 HTTP 接入属于本流程，服务端功能开发和完整云服务建设不在本流程范围。

## 使用流程

1. 读目标调用点、已有封装、接口说明及配置；记录项目版本、目标平台、Vapor/VDOM、HBuilderX 和插件版本。未知项先从工程查找，仅对影响实现且不可发现的信息提问。
2. 按 [调用与异常处理](references/api-patterns.md) 查官方 API 的具体参数、返回、权限、版本和模式兼容性；官方内置 API 满足需求时优先使用。未支持项明确替代路径和验证成本，不能靠名称相似推断支持。
3. 复用已有最小封装，区分传输失败、HTTP 状态和业务状态。结合生命周期处理重复触发、取消、迟到响应、监听和资源释放。
4. 涉及个人信息、权限或 SDK 数据行为时加载 [uniappx-privacy](../uniappx-privacy/SKILL.md) 的相关部分。已注册时可按技能名调用，否则直接读取此相对路径；文件缺失则报告依赖及受影响验证，不能静默跳过。Vapor 页面需要原生能力时，通过已核验兼容的 UTS 插件边界实现。
5. 按调用类型验证适用的成功、失败、取消和平台差异，网络请求再补超时与鉴权失效等场景；使用真实接口或明确标注的测试替身。示例不是实机通过证据。

## 交付

输出适用条件、调用/改动方案、验证证据、问题和下一步。阶段结果为**通过／阻塞／不适用**；必需检查未完成属于阻塞原因。平台不支持、接口契约冲突或权限方案不成立时阻止该调用方案通过，继续独立工作。

明确区分官方要求、团队约定和推荐实践。资料不可访问或版本未确认时标为待核验，不发明签名、参数或支持范围。结论绑定项目版本／平台／模式／工具版本，相关条件改变时重查。

## 按需资料

- [调用与异常处理](references/api-patterns.md)：接口选型、网络示例、原生插件及验证场景。
- [官方来源记录](references/sources.json)：精确来源与核验状态。
