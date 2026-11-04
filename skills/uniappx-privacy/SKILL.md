---
name: uniappx-privacy
description: Use when uni-app X work involves privacy consent, runtime permissions, personal data, analytics or advertising SDKs, privacy disclosures, withdrawal, account deletion or store privacy rejection. 适用于隐私、权限和 SDK 数据行为核验。
---

# uni-app X 隐私、权限与 SDK

从真实数据行为检查应用、插件和服务端的配合；框架隐私状态、系统权限与商店声明分别核验。

## 使用流程

1. 确认项目版本、平台、模式、工具/SDK 版本、发行地区及当前功能，盘点调用点、原生自动初始化、权限配置和已有隐私页面。
2. 使用 [隐私与权限流程](references/privacy-and-permissions.md) 建立必要的数据/SDK 清单，识别同意前采集、超范围权限、撤回无效或披露不一致。
3. 按当前官方文档确认隐私 API、按钮机制和平台默认状态；功能触发时申请系统权限，拒绝后按业务提供降级或明确退出该功能。
4. 对照实际渠道当前规则检查隐私文本与后台声明。只有真实触发的登录、广告、支付、儿童/未成年人或特殊行业要求才加入检查，不套用全部行业规则。
5. 验证首次启动、拒绝、同意、冷启动、撤回、协议更新以及 SDK 自动初始化路径；通过代码、原生日志及必要的网络观测证明数据行为。

## 交付

输出适用条件、数据/SDK 清单、已执行改动和验证证据、缺项及下一步。结果为**通过／阻塞／不适用**。已确认的必要合规缺项，或必要数据行为验证尚未完成，阻止相关阶段通过；不妨碍无关开发。

将官方要求、团队基线和建议分别标识。具体法律/商店要求须注明来源、适用条件、核验日期；不能仅凭隐私弹窗出现、平台默认 `agree`、SDK 声称合规或后台勾选完成作出合规通过结论。

结论绑定项目版本／平台／模式／工具及 SDK 版本；采集行为、SDK、地区或渠道变化时重查。来源不可访问时列待核验，不编造法规或审核条文。

## 按需资料

- [隐私与权限流程](references/privacy-and-permissions.md)：框架机制、检查表及异常场景。
- [官方来源记录](references/sources.json)：正文与适用范围。
