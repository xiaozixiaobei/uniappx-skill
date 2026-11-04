---
name: uniappx-build
description: Use when configuring or producing uni-app X Android, iOS or HarmonyOS App builds, release signing, certificates, application identifiers, native configuration, cloud packaging or build artifact verification. 适用于打包、签名与产物核验。
---

# uni-app X 分平台打包

以实际平台工具链和应用身份构建可追溯产物。构建成功不等于测试通过或已经满足商店上架要求。

## 使用流程

1. 读取 manifest、平台原生资源、已有构建说明和目标分发方式，记录源码版本、模式、工具链、应用版本及身份。确认工具和签名文件的存在与用途，日志不输出密码或私钥。
2. 按 [分平台构建](references/platform-builds.md) 选择 Android/iOS 云打包或经核验的本地方案；鸿蒙按项目文档所述 DevEco 本地链路处理，不能假设有同一云打包命令。
3. 检查应用标识、版本、最低系统、target/编译 SDK、能力/权限、SDK 签名绑定与证书关系。平台能力和商店提交要求分开核对。
4. 通过已确认的菜单或 CLI 执行构建，保留退出结果与产物位置；出错按首个有效错误定位，不能用降低安全校验或伪造签名解决。
5. 检查产物身份、签名、版本、构建类型和哈希，再加载 [uniappx-quality](../uniappx-quality/SKILL.md) 验证安装、运行、升级。已注册时可按名调用，否则读取相对路径；文件缺失则报告受影响的依赖与验证。依据用户已有授权使用云服务；私钥材料上传或商店上传须有覆盖该材料、目的地和动作的授权，先完成可审阅配置，不重复询问已授权事项。

## 交付

输出适用条件、构建步骤/命令、产物与证据、问题和下一步。结果为**通过／阻塞／不适用**；缺必需工具/证书、签名不匹配或构建失败，相关阶段为阻塞。标准基座、自定义调试基座和正式包分别标识。

区分官方要求、团队基线和建议。结论绑定源码／平台／模式／工具链／版本／签名身份；变更后重查受影响项。CLI 未取得适用版本的正文与本机帮助时不发明命令；商店易变门槛交给发布流程重新核验。

## 按需资料

- [分平台构建](references/platform-builds.md)：云端/本地选择、签名和验收步骤。
- [官方来源记录](references/sources.json)：工具链及平台范围，特别注意普通 uni-app 鸿蒙文档的适用边界。
