# 下载和重导中文 PDF

[GitHub Releases](https://github.com/cacayue/Context-Engineering-ZH/releases) 提供单文件合订本和六册 ZIP。要使用分册间的跳转，解压后请将六份 PDF 放在同一目录并保留文件名。

## 更新译文后重导

在仓库根目录运行：

```bash
uv run zh/tools/export_pdf.py
```

需要 **uv、Pandoc、Google Chrome、curl、Fontconfig、Poppler（pdftotext）以及 Noto CJK 简体中文字体**。Python 依赖由 uv 按脚本内版本准备；正文从本地读取，原文的外链插图按需获取。

导出目录是 `zh/dist/pdf/`，包含 `01.pdf` 至 `06.pdf`、`Context-Engineering-ZH-Complete.pdf`、分册 ZIP、下载目录及 `export-report.json`。这些成品不进入 Git。命令根据 `zh/manifest.json` 编排章节，拒绝未完成或缺失的译文；新增章节时请先按中文化流程更新清单。无法取得的外链图片会保留原图链接，并记录在报告中。

## 发布新 Release

将新版源文件提交到 `zh/main` 并同步至 `origin` 后，用有发布权限的 GitHub CLI 登录运行：

```bash
uv run zh/tools/export_pdf.py --release zh-pdf-YYYY.MM.DD
```

把日期替换成实际版本日期；同日第二次发布可用 `.2` 后缀。命令按当前提交重导并校验，上传到新草稿，核对八个附件后再发布。它不会自动提交、推送分支或覆盖已有 Release。若上传中断，请在 GitHub 检查该标签的草稿；本地已校验的 PDF 仍可使用。

排版与分册顺序在 `zh/tools/pdf_export/`，入口为 `zh/tools/export_pdf.py`。
