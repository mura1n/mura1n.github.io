# 修改和隐藏内容

## 1. 个人信息

编辑 `_config.yml`：

```yaml
first_name: Yulong
last_name: Chen
email: 72405526@cityu-dg.edu.cn
github_username: mura1n
scholar_userid: WAzerzwAAAAJ
linkedin_username:
orcid_id:
```

社交字段留空即可隐藏对应图标，不要填写 `TODO`、`None` 或假链接。
留空 Scholar/GitHub 后，首页对应的资源卡也自动隐藏。
RefineEdit 资源卡在 `_pages/about.md` 中，可直接删除整个对应的
`<a class="resource-card ...">...</a>` 块。

简介位于 `_pages/about.md` 的第二个 `---` 之后。
暂时不想公布的经历直接删除，不要用 HTML 注释保留私密内容。

## 2. 照片

当前使用你提供的 `yulong-2026.jpg` 原图。
换图时把文件放入 `assets/img/`，并修改
`_pages/about.md`：

```yaml
profile:
  align: right
  image: yulong-2026.jpg
  image_circular: false
```

完全隐藏照片可将整个 `profile:` 配置改为 `profile: false`。
不必调整 CSS，原模板已包含桌面和移动端布局。

## 3. 添加论文和效果图片

把图片存入 `assets/img/publication_preview/`。
在 `_bibliography/papers.bib` 中添加条目，例如：

```bibtex
@article{unique_key_2026,
  title={Your Paper Title},
  author={Chen, Yulong and Lastname, Firstname},
  journal={arXiv preprint},
  year={2026},
  html={https://example.com/paper},
  code={https://github.com/your-account/your-project},
  preview={your-paper.png},
  selected={true}
}
```

- `selected={true}`：在首页 Selected Publications 中显示。
- 改为 `selected={false}` 或删除该字段：只在 Publications 页面显示。
- 要从网站完全移除，删除整个条目，或移至仓库外单独保存。
- 没有图：删除 `preview` 字段；可用 `abbr={Venue}` 显示会议标记。
- 没有链接：删除对应字段，不会显示无效按钮。
- `html`、`pdf`、`code`、`website`、`video` 可按需添加。
- 点击论文缩略图可查看大图。版式采用原模板，未做另一套卡片布局。
- 有图的论文：图片占约三分之一栏宽，文字占三分之二；手机端上下排列。
- 共同作者标记放在姓后，例如 `Chen*, Yulong`、`Chen†, Yulong`，
  这样模板仍能识别并强调自己的名字。
- 只写已确认的作者、年份和录用状态。已有 RefineEdit 图片，
  但请先补齐并确认其公开论文信息再添加条目。

## 4. 添加 News

News 已显示在首页 Selected Publications 上方。目前不显示任何示例动态，
为空时显示原模板的 “No news so far...” 提示。

复制 `_news/announcement-template.md`，例如另存为 `_news/2026-09-25-update.md`，
替换正文和日期，并将 `published: false` 改为 `published: true`：

```markdown
---
layout: page
title: A short news title
date: 2026-09-25
inline: true
published: true
related_posts: false
---

在这里填写你的真实动态，可以使用 **粗体** 和 [链接](https://example.com)。
```

按日期从新到旧排列。每条动态一个文件，保留模板的 `published: false`，
就不会把模板本身显示到网站上。暂时不想展示某条动态也可设为 `published: false`。
默认最多显示七条，可修改 `_config.yml` 中的 `announcements.limit`。
添加后重新构建；使用 Jekyll 预览服务时会自动更新。

## 5. 隐藏整个栏目

首页论文区：`_pages/about.md` 中设 `selected_papers: false`。
首页 News：同一个文件中设 `news: false`。

CV 或 Talks 完全隐藏：对应 `_pages/*.md` 的头部设置：

```yaml
nav: false
published: false
```

以后恢复时设 `nav: true` 并删除 `published: false`。
仅设 `nav: false` 只隐藏导航，不会让已有页面不可访问。
Talks 当前未发布，内容来自 `_data/talks.yml`，填好后再开放。

CV 数据在 `_data/cv.yml`。没有的章节可删除整个章节项。
若没有 PDF 简历，保持 `_pages/cv.md` 的 `cv_pdf:` 为空。
有 PDF 后放到 `assets/pdf/`，再填文件名即可显示下载按钮。

Blog 没有导入，也没有博客入口、文章页或 RSS。

## 6. 保持与参考站的外观一致

不要修改 `_sass/`、`assets/css/main.scss`、`_includes/header.html`
或 `_layouts/about.html`，除非确实想改变外观。
这些文件基于参考站原模板，只对论文图片宽度和 News 标题做了必要调整；
平时只编辑上面的内容文件即可。

该版本保留参考站的 Google Fonts 和 CDN 依赖。字体需能正常联网加载；
暗色模式还会记住浏览器此前的选择，用右上角按钮可以切换。
