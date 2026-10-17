# 来源与致谢

## 上游项目

- 名称：AirCard — Apple Wallet Card Skinner
- 仓库：https://github.com/Mak5er/AirCard
- 作者：Maksym Reva（[@mak5er](https://github.com/Mak5er)）、[@Lumid-Off](https://github.com/Lumid-Off)
- 版本：v1.2.6
- 许可证：MIT（Copyright (c) 2026 Johnny Franks，见 `LICENSE`）

## 本仓库

- 性质：**非官方简体中文汉化版**
- 基础：官方 v1.2.6 源码
- 新增内容：
  - `Localization/zh-Hans.lproj/Localizable.strings`（249 条中文文案）
  - `AirCardApp.swift` 中的 `tr()` 本地化辅助函数与动态文本包裹
  - `Sources/WalletDiagnosticsView.swift` 中的动态文本包裹
  - `build_zh.sh` 构建脚本（本地化资源打包、SDK 自动匹配）
  - `tools/gen_strings.py` 文案生成器
- 汉化方式：由 **DeepSeek** 协助完成翻译、源码定位、构建适配与逐页截图验证

## 声明

本仓库与原作者、Apple Inc. 均无隶属关系，也未获得其官方背书。
原项目全部核心代码与素材版权归原作者所有；本仓库仅新增中文界面文案与构建适配，并同样以 MIT 许可证发布。
