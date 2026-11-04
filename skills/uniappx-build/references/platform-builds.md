# 分平台构建

## 共同输入和构建身份

记录源码提交或快照、HBuilderX/原生工具版本、Vapor/VDOM、目标 OS、环境配置、插件/SDK、应用版本及签名身份。区分 DCloud `appid`、Android package、iOS Bundle ID、鸿蒙 bundleName，不能相互替换。

保持既有应用身份和签名连续性；更新包与已发布版本比较。版本号满足框架和目标渠道要求，不仅检查名称相同。最低运行系统、编译 SDK、Android target SDK、商店上传最低 SDK 是不同约束，分别记录。

引用 [项目文档](https://doc.dcloud.net.cn/uni-app-x/project.html)、[云打包](https://doc.dcloud.net.cn/uni-app-x/tutorial/app-package.html) 和 [manifest](https://doc.dcloud.net.cn/uni-app-x/collocation/manifest.html)。离线/嵌入原生工程需要 uni-app X 对应 SDK 及原生工程文档；不得改用旧 uni-app 的离线包结构。CLI 入口已确认但正文未核验，按具体版本补查帮助后再自动化，不给出猜测的 npm/build/publish 命令。

## Android

1. 在 `manifest.json` 和平台配置中核对 package、版本、最低系统、target SDK、ABI、权限/模块及 SDK 参数。若插件不兼容新的 target，先核对插件升级及平台/渠道要求；不能为编译过关随意降低 target 并报告可上架。
2. 云打包按 HBuilderX **发行 → App-Android/iOS-云打包** 进入，选择 Android，配置包名、所需证书与格式。云端操作涉及上传的源码/证书按用户授权和工具规则执行，不因读到文档就自动上传私钥。
3. 选择项目既定云证书或自选证书；更新版本时核对签名指纹。自选证书核对路径、别名、有效性及密码是否可用，密码通过已有安全方式提供，不写入仓库或报告。
4. 格式依目标渠道确认。DCloud 支持 APK 和 AAB，不意味着中国各渠道都接受两者；AAB 不按 APK 直接安装测试。自定义渠道号仅是包内标记，不代表已经满足某店审核。
5. 构建后使用本机已有且适用的 Android SDK 工具检查签名、包名、版本、权限和 ABI，并留存日志。工具缺失时明确待验证，不仅从文件名推断。
6. 安装实际候选包，验证启动、核心能力、签名绑定 SDK 和覆盖升级；性能在 release 正式包测量。

## iOS

1. 核对 Bundle ID、Team、版本/build、支持设备、最低系统、所需 capabilities、Info.plist 用途说明和 SDK 配置。
2. 云打包按同一菜单选择 iOS，使用当前分发方式要求的证书/私钥和匹配 Profile。开发、Ad Hoc、TestFlight/App Store 等签名用途分开核验；可在测试手机安装不等于可向 App Store 上传。
3. 本地构建时先确认 uni-app X 原生工程及所需 Xcode/SDK。App Store 提交要求在发布时按 Apple 当前官方说明核查，不以运行最低 iOS 版本代替 SDK 上传门槛。
4. 检查签名身份、Profile、Bundle ID、entitlements、版本和分发类型一致，保留真实构建产物。证书存在不能证明密码正确、证书未撤销或 Profile 能覆盖当前能力。
5. 在实际设备或适用测试分发验证安装、启动、权限、核心流程与升级；没有设备时该验收仍待验证。测试账号、推送/登录/支付等按实际正式环境再核验。

## HarmonyOS

以 [uni-app X 项目文档](https://doc.dcloud.net.cn/uni-app-x/project.html) 为路线依据：调用本地 DevEco 出包。参考 [鸿蒙运行与发行](https://uniapp.dcloud.net.cn/tutorial/harmony/runbuild.html) 的公共工具安装、签名和发行操作；该页普通 uni-app 的兼容性说明、热更新和最低系统门槛不能移植为 uni-app X/Vapor 结论。

1. 确认本机 DevEco、SDK、设备连接工具、HBuilderX 的适配组合；Vapor 的 OS/工具门槛另查 Vapor 文档。发布时核对正式 API/SDK，避免将 Beta 工具链产物默认用作发行包。
2. 按所用 uni-app X 版本识别配置目录；项目文档当前提到 `harmonyConfig`，公共 uni-app 文档中也存在 `harmony-configs`。先检查实际项目与对应 x 文档，不能仅依据普通 uni-app 路径创建/覆盖配置。
3. 核对 bundleName、版本、图标/名称、权限/能力、目标与兼容 API，以及发布证书/Profile 与签名配置。调试自动签名只证明调试环境，不代表正式分发身份。
4. 通过已验证的 HBuilderX/DevEco 发行路径生成候选包，确认当前目标商店实际接受的格式与签名类型；运行用 HAP 不能未经检查当作上架产物。
5. 避免构建中同时触发差量编译。出现编译锁或忍者构建错误时保留首个错误，停止冲突任务后按工具要求重建；不要反复修改权限/签名来碰运气。
6. 验证目标真机的安装、冷启动、权限、原生能力和升级。华为 Android 渠道与鸿蒙渠道分别核验。

## 产物交接

最小交付记录：源码/配置版本、平台与模式、工具链、应用标识、版本号、构建类型、签名主体/公开指纹、产物路径/文件名、SHA-256、构建结果和已完成的安装验证。不要记录私钥或密码。候选包一旦重签名、加固、加入渠道信息或换 SDK，更新哈希并重做受影响验证。

自定义调试基座不能用于上架；云打包正文对此有明确说明。文件生成、安装成功、业务通过、商店审核是不同阶段，分别报告。

热更新属于单独能力：框架支持 WGT 不等于商店允许动态改变功能。涉及热更新时核验对应模式/工具能力及渠道规则；iOS 尤其核对 Apple 审核指南 2.5.2，不默认启用绕过审核的更新路径。
