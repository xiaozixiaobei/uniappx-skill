---
name: uniappx-store-publish
description: Use when preparing, checking or submitting a uni-app X App for Apple China, Huawei, Xiaomi, OPPO, vivo or Tencent MyApp, or resolving review rejection, policy freshness, store metadata and channel differences. 适用于中国主要商店上架规范。
---

# uni-app X 商店发布规范

用共用准备项减少重复，逐渠道核验差异；不存在可替代所有商店当前规则的一份固定通用标准。

## 使用流程

1. 确认目标商店/地区/平台、应用主体/类别/功能、候选包身份与哈希、源码版本、模式、工具链和测试结果。进入“发布阶段”不等于已授权对外提交。
2. 先读 [共用发布检查](references/release-checklist.md)，再仅加载 [渠道差异](references/channels.md) 中目标商店的条目。需要补证据时加载 [uniappx-build](../uniappx-build/SKILL.md)、[uniappx-quality](../uniappx-quality/SKILL.md) 或 [uniappx-privacy](../uniappx-privacy/SKILL.md)；已注册可按名调用，否则读取相对路径，缺文件则报告具体依赖。避免重做已有效完成的独立检查。
3. **每次实际发布前**重新读取目标商店官方正文、适用公告及当前后台表单，记录生效日期、核验日期和适用范围。入口可访问、页面标题存在、HTTP 200 或旧报告不能证明具体条款已核实。
4. 先完成可审阅的材料与缺项表；已确认的必要条件不满足或必需条款仍未核验时，该渠道不能报准备通过。其他已满足条件的渠道可继续独立准备。
5. 按用户已有授权执行具体渠道的上传/提交；需要的授权应覆盖应用、版本、目的地和动作。实际提审、付费、协议接受和线上版本操作遵守工具权限边界，不从泛泛“同意项目”推导授权，也不对已明确授权事项重复索要确认。
6. 记录真实回执和状态。被拒时按原文、条款、包版本和复现步骤定位，针对性修改并重验；上传成功不等于审核通过，审核通过不等于已上线。

## 交付

输出适用条件、共用准备结果、目标渠道差异、验证与官方依据、缺项、下一步。结果为**通过／阻塞／不适用**，注明是“准备”“上传”“审核”还是“上线”的结果；待核验/待验证是阻塞原因。

区分官方要求、团队准备基线和建议。报告绑定项目／包哈希／平台／模式／工具与签名／渠道／核验日期；换包、换 SDK、加固、重签名或规则变化时重查受影响项。

## 按需资料

- [共用发布检查](references/release-checklist.md)：候选包、材料、条件触发与回执。
- [渠道差异](references/channels.md)：Apple 中国区、华为、小米、OPPO、vivo、应用宝。
- [官方来源记录](references/sources.json)：`verified` 是已读相应正文，`entry-only` 仅证明入口；两者不能互换。
