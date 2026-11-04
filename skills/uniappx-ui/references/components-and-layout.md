# 组件与布局

## 组件选择

组件/属性/事件的支持分别查 [组件概述](https://doc.dcloud.net.cn/uni-app-x/component/) 及对应组件正文。页面默认使用 uni-app X 的 `view`、`text`、`image`、`input` 等，不把 Web 的 `div`、DOM 库或浏览器事件实现直接当成 App 方案。复用项目已有且兼容的组件。

第三方库按目标平台 + Vapor/VDOM + HBuilderX/插件版本核验；先尝试最小页面，再引入业务。未确认兼容时不要替用户安装大型组件库。原生 UI 扩展还要核对 `native-view` 与 UTS 标准模式支持。

## Vapor 样式约束

依据 [Vapor 开发注意](https://doc.dcloud.net.cn/uni-app-x/app-vapor.html)、[选择器](https://doc.dcloud.net.cn/uni-app-x/css/common/selector.html) 和 [样式隔离](https://doc.dcloud.net.cn/uni-app-x/css/common/style-isolation.html)，核验日 2026-11-04：

- Vapor 运行时只支持简单 class 与分组选择器。将层级选择器 `.panel .title` 改成显式类名 `.panel__title`；SCSS 是编译期工具，但编译后的选择器仍需符合运行时约束。
- Vapor 只使用样式隔离 2.0。组件默认 `isolated`，外部同名 class 不会自然覆盖组件；需要外部影响时，按文档用 `defineOptions` 的 `styleIsolation` 选择 `app` 或 `app-and-page`，同时评估作用范围。
- App CSS 是 Web CSS 的子集。布局属性、单位、文字换行、定位、层叠与安全区按具体文档及目标设备验证，不以浏览器效果推导支持。不把所有 VDOM 的 CSS 一律按 Vapor 限制处理。
- 若干滚动/轮播组件的布尔默认值在模式间有变化，需要的行为显式设定，并查对应属性文档；不要把某一个组件的默认值变化扩展成所有布尔属性规则。

保持项目已有的样式方案；不为单页引入主题系统。组件内外的样式影响、暗黑/大字体等以产品需求和实际支持为准。

## 长列表

普通滚动先看 `scroll-view`；大量重复数据先评估 [list-view](https://doc.dcloud.net.cn/uni-app-x/component/list-view.html)。Vapor 的具体复用条件以 [Vapor 文档](https://doc.dcloud.net.cn/uni-app-x/app-vapor.html) 为准：

1. `list-item` 上的 `v-for` 必须有稳定 `:key`。
2. 一个 `list-view` 中，仅第一组符合条件的 `list-item v-for` 参与该复用机制；后续独立循环不能默认复用。
3. `list-item` 与 `list-view` 必须位于同一 `.uvue` 文件，不能把 `list-item` 根节点包装进另一个组件来期望相同复用。

最小结构示例：Vapor 工程中沿用可转换的 UTS 脚本；具体组件支持仍需按工具版本与目标平台确认。此片段在本技能包中未进行 App 编译，不是已验证的生产页面。

```vue
<template>
  <view class="page">
    <list-view class="list">
      <list-item v-for="row in rows" :key="row.id" class="row">
        <text>{{ row.title }}</text>
      </list-item>
    </list-view>
  </view>
</template>

<script setup lang="uts">
import { ref } from 'vue'
type Row = { id: string, title: string }
const rows = ref<Row[]>([
  { id: 'first', title: '第一项' },
  { id: 'second', title: '第二项' }
])
</script>

<style>
.page { flex: 1; }
.list { flex: 1; }
.row { padding: 16px; }
</style>
```

分页和虚拟复用解决不同问题。数据大时依实际 API 分页；不要为证明复用有效额外引入通用虚拟列表库。复用项中的选择、侧滑、输入和媒体状态按数据 ID 管理，测试滚回旧项时是否串状态。

## 布局与交互验收

| 场景 | 检查内容 |
|---|---|
| 页面与滚动 | 容器高度、唯一主要滚动区、嵌套滚动、触底去重、刷新与返回位置 |
| 表单与键盘 | 输入类型、焦点/失焦、键盘遮挡、提交去重、错误反馈及禁用状态 |
| 安全区与导航 | 状态栏、刘海/底部手势区、导航栏和 tabBar 的实际占位，避免重复补偿 |
| 图片与文本 | 加载失败、长文本、多语言、大字体；按产品要求检查暗黑模式 |
| 列表与媒体 | 真机快滑、分页错误、复用状态、内存、离页释放和重新进入 |
| 可访问性 | 重要图标有可理解文本，状态不只靠颜色，按组件能力验证辅助技术操作 |

验收记录包含设备/系统、应用版本、模式、构建类型和复现步骤。UI 外观检查与功能检查分别留证；性能测试使用正式或适用 release 构建，不能由 debug/Web 数据推出 App 性能结论。
