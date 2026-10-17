#!/usr/bin/env python3
# 生成 zh-Hans.lproj/Localizable.strings
# 键 = AirCard 界面中的英文原文（含 SwiftUI 插值格式符），值 = 简体中文

T = {}

def add(en, zh):
    T[en] = zh

# ---------- 通用 / 工具栏 ----------
add("AirCard", "AirCard")
add("v1.2.6", "v1.2.6")
add("Wallet Cards & Passcode Themes", "钱包卡片与密码键盘主题")
add("Refresh Device List", "刷新设备列表")
add("Refresh device connection", "刷新设备连接")
add("Click to select an active device", "点击以选择当前设备")
add("Select Device", "选择设备")
add("No iPhone (USB)", "未连接 iPhone（USB）")
add("Scan Cards", "扫描卡片")
add("Stop Scanning", "停止扫描")
add("Start Scanning", "开始扫描")
add("Save IDs", "保存 ID")
add("Save IDs for Matching", "保存 ID 用于匹配")
add("Save Card IDs for Matching", "保存卡片 ID 用于匹配")
add("Set Skin for All...", "为全部卡片设置皮肤…")
add("Assign one skin to all selected cards", "为所有选中的卡片指定同一张皮肤")
add("Select All", "全选")
add("Deselect All", "取消全选")
add("Clear All", "全部清除")
add("Done", "完成")
add("Cancel", "取消")
add("OK", "确定")
add("Close", "关闭")
add("Remove", "移除")
add("Reset", "重置")
add("Clear", "清除")
add("Copy", "复制")
add("Copied!", "已复制！")
add("Copy full hash", "复制完整哈希")
add("Export", "导出")
add("Credits", "致谢")
add("Credits & Donate", "致谢与捐赠")
add("Category", "分类")
add("Log", "日志")
add("Activity Log", "活动日志")
add("Ready", "就绪")
add("Target:", "目标：")

# ---------- 钱包卡片 ----------
add("Apple Wallet", "苹果钱包")
add("No Cards Detected Yet", "尚未检测到卡片")
add("Click **Scan Cards** in the toolbar above.", "点击上方工具栏中的「扫描卡片」。")
add("On your iPhone, **double-click the Side button** (Apple Pay), authenticate with **Face ID**, and **tap your card**.",
    "在 iPhone 上，**双击侧边按钮**（Apple Pay），通过 **Face ID** 验证，然后**轻点你的卡片**。")
add("Your card will be detected immediately!", "你的卡片将被立即检测到！")
add("Detected cards will appear here as the iPhone reports them.", "检测到的卡片会在此显示，以 iPhone 报告为准。")
add("Live Scanner Active", "实时扫描已开启")
add("Double-click Side button (Apple Pay), pass Face ID, then tap your card.",
    "双击侧边按钮（Apple Pay），通过 Face ID 验证，然后轻点你的卡片。")
add("Double-click Side button", "双击侧边按钮")
add("Double-click Side button, pass Face ID, then tap your card...",
    "双击侧边按钮，通过 Face ID 验证，然后轻点你的卡片…")
add("Scanner is active. Open Wallet on your iPhone.", "扫描器已激活。请在 iPhone 上打开钱包。")
add("Scanning for Cards…", "正在扫描卡片…")
add("Check missing cards", "检查缺失的卡片")
add("Not verified", "未验证")
add("Unidentified card", "未识别的卡片")
add("Matched to this iPhone in current scan", "本次扫描中与此 iPhone 匹配")
add("Saved on this iPhone", "已保存在此 iPhone 上")
add("Manually added · Ready to flash", "手动添加 · 可刷写")
add("Skin already on iPhone", "皮肤已在 iPhone 上")
add("Skin changed, will be flashed", "皮肤已更改，将被刷写")
add("Skin file unavailable. Choose the image again.", "皮肤文件不可用。请重新选择图片。")
add("Remove skin", "移除皮肤")
add("Change Skin", "更换皮肤")
add("Include in flash", "包含在刷写中")
add("Remove from list", "从列表移除")
add("Assign Card Skin", "指定卡片皮肤")
add("Click to browse or drag image", "点击浏览或拖入图片")
add("Drop image here", "将图片拖到此处")
add("Paste one or more card IDs. Saved IDs remain hidden until the connected iPhone exposes them in a scan.",
    "粘贴一个或多个卡片 ID。已保存的 ID 会在连接的 iPhone 于扫描中提供之前保持隐藏。")

# ---------- 密码主题 ----------
add("Passcode (.passthm)", "密码键盘主题 (.passthm)")
add("Apply .passthm", "应用 .passthm")
add("Passcode Theme File", "密码键盘主题文件")
add("Passcode Themes:", "密码键盘主题：")
add("Lock Screen Keypad Preview", "锁屏密码键盘预览")
add("Interactive iPhone Lock Screen Preview", "可交互的 iPhone 锁屏预览")
add("Custom Theme Loaded", "已加载自定义主题")
add("Enter Passcode", "输入密码")
add("Emergency", "紧急")
add("Choose .passthm File...", "选择 .passthm 文件…")
add("Choose File...", "选择文件…")
add("Export .passthm...", "导出 .passthm…")
add("Change...", "更改…")
add("Clear Theme", "清除主题")
add("Drop .passthm file here", "将 .passthm 文件拖到此处")
add("Supports .passthm, .passtheme, or .zip packages from Cowabunga or Nugget",
    "支持来自 Cowabunga 或 Nugget 的 .passthm、.passtheme 或 .zip 压缩包")
add("TelephonyUI-10 (iOS 18+)", "TelephonyUI-10（iOS 18+）")
add("TelephonyUI-9 (iOS 16–17)", "TelephonyUI-9（iOS 16–17）")
add("TelephonyUI-8 (iOS 14–15)", "TelephonyUI-8（iOS 14–15）")
add("Universal (All 8, 9, 10)", "通用（全部 8、9、10）")
add("Edit in Creator", "在创建器中编辑")
add("Drag dialer to pan · Use slider to zoom", "拖动拨号盘平移 · 使用滑块缩放")
add("No .passthm loaded · Select a theme package to flash", "未加载 .passthm · 请选择要刷写的主题包")
add("Passcode theme applied successfully!", "密码主题已成功应用！")
add("Flash & Language Target", "刷写与语言目标")
add("Auto-detect", "自动检测")
add("Reset to iPhone's detected language and font style", "重置为 iPhone 检测到的语言与字体样式")
add("System Language:", "系统语言：")
add("Font Weight / Style:", "字重 / 样式：")
add("Universal mode flashes ~600 files for all languages & Bold text. Selecting a specific language (e.g. Ukrainian) speeds up flashing dramatically.",
    "通用模式会为所有语言与加粗文字刷写约 600 个文件。选择特定语言（例如乌克兰语）可大幅提升刷写速度。")
add("Flash Passcode Theme", "刷写密码主题")
add("Flash to iPhone", "刷写到 iPhone")
add("Flash Skins", "刷写皮肤")
add("Flashing Cards...", "正在刷写卡片…")
add("Flashing Passcode...", "正在刷写密码主题…")

# ---------- 主题创建器 ----------
add("Theme Creator", "主题创建器")
add("Theme Creator reset", "主题创建器已重置")
add("Theme Creator · Import a poster or drop icons onto keys", "主题创建器 · 导入海报或将图标拖到按键上")
add("Poster Artwork", "海报素材")
add("Artwork Loaded", "素材已加载")
add("Drop poster or wallpaper here", "将海报或壁纸拖到此处")
add("Choose Image...", "选择图片…")
add("Change Image...", "更改图片…")
add("Choose Poster...", "选择海报…")
add("Change Poster...", "更换海报…")
add("Choose Poster Image", "选择海报图片")
add("Slicing Style", "切片方式")
add("Seamless Poster", "无缝海报")
add("Circle Buttons", "圆形按钮")
add("Poster Slice (Puzzle)", "海报切片（拼图）")
add("Individual Keys", "单独按键")
add("Artwork is clipped into individual circular button icons.", "素材会被裁切为独立的圆形按钮图标。")
add("Seamless artwork spans across dialer keys without circular cuts (Adobe Dog style).",
    "无缝素材跨拨号键铺开，不做圆形裁切（Adobe Dog 风格）。")
add("Zoom & Framing", "缩放与构图")
add("Reset Position", "重置位置")
add("Reset Position & Zoom", "重置位置与缩放")
add("Zoom", "缩放")
add("Drag anywhere on the dialer preview to reposition", "在拨号预览上任意拖动以重新定位")
add("Click any key on the dialer to select it, pan the image, adjust zoom, or drop files.",
    "点击拨号盘上的任意按键即可选中它、平移图片、调整缩放或拖入文件。")
add("Fill from Poster", "从海报填充")
add("Clear All Keys", "清除全部按键")
add("Poster image loaded · Ready to frame and slice", "海报图片已加载 · 可进行构图与切片")
add("Save Passcode Theme", "保存密码键盘主题")

# ---------- 诊断 / 设备 ----------
add("Read Cache", "读取缓存")
add("Read this Mac's Wallet cache", "读取此 Mac 的钱包缓存")
add("Reading…", "正在读取…")
add("Reconnect", "重新连接")
add("Scanning iPhone Wallet…", "正在扫描 iPhone 钱包…")
add("All cached cards on this Mac have been verified.", "此 Mac 上所有缓存的卡片均已验证。")
add("No cards detected. Tap 'Scan Cards' to begin.", "未检测到卡片。点击「扫描卡片」开始。")
add("No cards detected. Open Wallet and tap a card.", "未检测到卡片。请打开钱包并轻点一张卡片。")
add("Checking iPhone…", "正在检查 iPhone…")
add("Checking connected devices...", "正在检查已连接的设备…")
add("Connecting to the iPhone log stream…", "正在连接 iPhone 日志流…")
add("No iPhone connected.", "未连接 iPhone。")
add("No iPhone found. Please connect via USB.", "未找到 iPhone。请通过 USB 连接。")
add("No iPhone connected. Connect, unlock and trust this Mac, then use Reconnect.",
    "未连接 iPhone。请连接、解锁并信任此 Mac，然后点击「重新连接」。")
add("Open Wallet and scan cards to verify this iPhone's saved entries.",
    "打开钱包并扫描卡片，以验证此 iPhone 上保存的条目。")
add("Could not read Wallet metadata. Scanning still works. Use Read Cache to retry.",
    "无法读取钱包元数据。扫描仍可使用。请点击「读取缓存」重试。")
add("No matching name in the Mac cache. The card ID is preserved.",
    "Mac 缓存中没有匹配的名称。卡片 ID 已保留。")
add("A payment card was activated, but its ID is not available in this Mac's Wallet cache. Use Read Cache and try again.",
    "已激活支付卡，但其 ID 不在此 Mac 的钱包缓存中。请点击「读取缓存」后重试。")
add("Payment card activated. Waiting for Wallet metadata to finish loading…",
    "支付卡已激活，正在等待钱包元数据加载…")
add("Scanner connected. Open Wallet and tap a card; membership cards may need opening in the Wallet app.",
    "扫描器已连接。打开钱包并轻点一张卡片；会员卡可能需要在钱包 App 中打开。")
add("Scanner could not start. Reconnect the iPhone and try again.",
    "扫描器无法启动。请重新连接 iPhone 后重试。")
add("Could not start card scanning.", "无法启动卡片扫描。")
add("Card scanning ended. Check the log and reconnect the iPhone to retry.",
    "卡片扫描已结束。请检查日志并重新连接 iPhone 后重试。")
add("Card scanning failed. Check the log and retry.", "卡片扫描失败。请检查日志后重试。")
add("The log connection failed. Reconnect the iPhone and retry scanning.",
    "日志连接失败。请重新连接 iPhone 并重试扫描。")
add("Device check failed. Reconnect and unlock the iPhone, then retry.",
    "设备检查失败。请重新连接并解锁 iPhone 后重试。")
add("Device detection could not run. See the log.", "无法运行设备检测。请查看日志。")
add("Device tools are missing from this build.", "此版本缺少设备工具。")
add("Device tools are missing. Rebuild or reinstall AirCard, then reconnect.",
    "设备工具缺失。请重新构建或安装 AirCard，然后重新连接。")
add("Developer tools or license agreement required. See log.", "需要开发者工具或接受许可协议。请查看日志。")
add("Command Line Tools required.", "需要命令行工具。")
add("Bundled device_helper not found — cannot scan.", "未找到内置的 device_helper —— 无法扫描。")
add("Bundled device_helper not found — detection cannot run.", "未找到内置的 device_helper —— 无法进行检测。")
add("AirCard could not run its device tools. Check the Activity Console log for details.",
    "AirCard 无法运行设备工具。请查看活动控制台日志了解详情。")
add("AirCard could not read the image you picked for one of the cards. That card was left unchanged.",
    "AirCard 无法读取你为某张卡片选择的图片，该卡片未做更改。")

# ---------- 提示 / 错误 ----------
add("Something went wrong", "出错了")
add("Success!", "成功！")
add("Failed to apply card skins.", "应用卡片皮肤失败。")
add("One or more cards could not be updated. Check the log and try again.",
    "一张或多张卡片无法更新。请查看日志后重试。")
add("Skin application stopped after a card update failed.", "某张卡片更新失败后，皮肤应用已停止。")
add("Complete! All cards updated.", "完成！所有卡片均已更新。")
add("Please assign a skin image to at least one selected card.", "请先为至少一张选中的卡片指定皮肤图片。")
add("Please connect and trust your iPhone first.", "请先连接并信任你的 iPhone。")
add("Please add at least one key icon or import a poster image first.", "请先添加至少一个按键图标或导入一张海报图片。")
add("Please configure at least one key before exporting.", "导出前请至少配置一个按键。")
add("Failed to inspect .passthm file", "无法解析 .passthm 文件")
add("Failed to package theme for flashing.", "打包主题以进行刷写失败。")
add("Cleared all cards.", "已清除全部卡片。")
add("Cleared all custom keys", "已清除全部自定义按键")
add("Created Theme", "已创建主题")
add("Adopted poster slices to individual keys", "已将海报切片应用到各个按键")
add("Starting passcode theme flash...", "正在开始刷写密码主题…")
add("Started scanning device logs for cards...", "已开始扫描设备日志以查找卡片…")

# ---------- 弹窗正文 ----------
add("Passcode theme successfully applied!\n\nLock your iPhone (or restart) to see your new passcode keypad.",
    "密码主题已成功应用！\n\n锁定 iPhone（或重启）即可看到新的密码键盘。")
add("Skins successfully applied to all selected cards!", "皮肤已成功应用到所有选中的卡片！")
add("Skins successfully applied to all selected cards!\n\nPlease force-close the Wallet app on your iPhone (or reboot) to see your new designs.\n\nNote: Apple Card renders dynamically and its face color reflects your spending categories rather than static cached skins.",
    "皮肤已成功应用到所有选中的卡片！\n\n请在 iPhone 上强制关闭「钱包」App（或重启）以查看新样式。\n\n注意：Apple Card 为动态渲染，其卡面颜色会随你的消费分类变化，而非静态缓存的皮肤。")
add("AirCard needs Xcode Command Line Tools to communicate with devices.\n\nPlease open Terminal and run:\nxcode-select --install\n\nor open Xcode to accept the license agreement, then restart AirCard.",
    "AirCard 需要 Xcode 命令行工具才能与设备通信。\n\n请打开终端并运行：\nxcode-select --install\n\n或打开 Xcode 接受许可协议，然后重新启动 AirCard。")

# ---------- 关于 / 捐赠 ----------
add("By", "作者")
add("&", "&")
add("@mak5er", "@mak5er")
add("@Lumid-Off", "@Lumid-Off")
add("@mak5er • Lead Developer", "@mak5er • 首席开发者")
add("Maksym Reva", "Maksym Reva")
add("Apple Wallet Skins & Passcode Themes for iOS 18+", "适用于 iOS 18+ 的 Apple 钱包皮肤与密码键盘主题")
add("Developer:", "开发者：")
add("Core Exploit:", "核心漏洞利用：")
add("airlift (AirTraffic sync escape)", "airlift（AirTraffic 同步逃逸）")
add("Passcode Themes:", "密码键盘主题：")
add(".passthm standard (Cowabunga / Nugget)", ".passthm 标准（Cowabunga / Nugget）")
add("Twitter / X", "Twitter / X")
add("GitHub", "GitHub")
add("DONATE & SUPPORT", "捐赠与支持")
add("Donate with PayPal", "通过 PayPal 捐赠")
add("Recipient: Maksym Reva", "收款人：Maksym Reva")
add("Support @mak5er (Donate ❤️)", "支持 @mak5er（捐赠 ❤️）")
add("Donate ❤️", "捐赠 ❤️")
add("Thank you for supporting AirCard development! ❤️", "感谢你支持 AirCard 的开发！❤️")
add("You can reopen donation options anytime in Credits & Donate ❤️",
    "你可以随时在「致谢与捐赠」中重新打开捐赠选项 ❤️")
add("💎 TON (The Open Network)", "💎 TON（The Open Network）")
add("💵 USDT (TRC20)", "💵 USDT（TRC20）")
add("🪙 BEP20 (BNB / USDT)", "🪙 BEP20（BNB / USDT）")

# ---------- 欢迎弹窗 ----------
add("Welcome to AirCard!", "欢迎使用 AirCard！")
add("Free & Open Source • Developed by @mak5er", "免费开源 • 由 @mak5er 开发")
add("Continue to AirCard", "继续使用 AirCard")
add("Don't show this popup on startup", "启动时不再显示此弹窗")

# ---------- 语言 / 字体选项（rawValue） ----------
add("All Languages (Universal)", "全部语言（通用）")
add("Ukrainian (uk)", "乌克兰语 (uk)")
add("Russian (ru)", "俄语 (ru)")
add("English (en)", "英语 (en)")
add("Other / Fallback", "其他 / 兜底")
add("Spanish (es)", "西班牙语 (es)")
add("German (de)", "德语 (de)")
add("French (fr)", "法语 (fr)")
add("Polish (pl)", "波兰语 (pl)")
add("Italian (it)", "意大利语 (it)")
add("Portuguese (pt)", "葡萄牙语 (pt)")
add("Turkish (tr)", "土耳其语 (tr)")
add("Japanese (ja)", "日语 (ja)")
add("Korean (ko)", "韩语 (ko)")
add("Chinese (zh)", "中文 (zh)")
add("Arabic (ar)", "阿拉伯语 (ar)")
add("Hebrew (he)", "希伯来语 (he)")
add("Universal (Regular + Bold)", "通用（常规 + 加粗）")
add("Bold Text Only (Fast)", "仅加粗文字（快速）")
add("Regular Font Only (Fast)", "仅常规字体（快速）")

# ---------- SwiftUI 插值格式键 ----------
add("%lld artwork assets loaded · Ready to flash to iPhone", "%lld 个素材已加载 · 可刷写到 iPhone")
add("Deselect Key %@", "取消选择按键 %@")
add("Key %@ Framing", "按键 %@ 构图")
add("Drag Key %@ on dialer preview to reposition", "在拨号预览上拖动按键 %@ 以重新定位")
add("Change Key %@...", "更改按键 %@…")
add("Clear Key %@", "清除按键 %@")
add("%lld of 10 keys configured", "已配置 %lld / 10 个按键")
add("Fast mode selected: only targets %@ with %@.", "已选择快速模式：仅针对 %@ 与 %@ 刷写。")
add("Theme Creator · %lld of 10 keys configured · Target: %@", "主题创建器 · 已配置 %lld / 10 个按键 · 目标：%@")
add("%lld source assets loaded · Target: %@", "已加载 %lld 个源素材 · 目标：%@")
add("%lld of %lld cards selected · %lld changed · %lld already on iPhone",
    "已选中 %lld / %lld 张卡片 · %lld 张已更改 · %lld 张已在 iPhone 上")
add("Connected Devices (%lld)", "已连接的设备（%lld）")
add("Cache date: %@", "缓存日期：%@")
add("Pending Payment Cards (%lld):", "待处理的支付卡（%lld）：")
add("Pending Passes / Memberships (%lld):", "待处理的通行证 / 会员卡（%lld）：")
add("#%lld", "#%lld")

def esc(s):
    return s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n").replace("\t", "\\t")

lines = ["/* AirCard 简体中文本地化（v1.2.6）",
         " * 由自动化流程生成：英文原文为键，保持与 SwiftUI LocalizedStringKey 完全一致。",
         " */", ""]
for k, v in T.items():
    lines.append(f'"{esc(k)}" = "{esc(v)}";')
lines.append("")
open("Localization/zh-Hans.lproj/Localizable.strings", "w", encoding="utf-8").write("\n".join(lines))
print("wrote", len(T), "entries")
