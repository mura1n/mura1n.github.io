# Yulong Chen's homepage

This is Songlin Yang's customized **al-folio / Jekyll template**, with
Yulong's content, no Blog, and image previews for publications.
The original fonts, spacing, 800px layout, colors, navigation, dark mode,
and fixed footer are retained. See [template provenance](TEMPLATE_ORIGIN.md).

## 本机预览

当前源码目录：`/Users/mercury/Projects/mura1n-homepage`

首次安装依赖需要 Ruby 和 Bundler。已在这台 Mac 的独立缓存中准备运行环境，
不会修改系统 Ruby。运行：

```bash
cd /Users/mercury/Projects/mura1n-homepage
bash scripts/preview.sh
```

打开 http://127.0.0.1:8000/ 。修改页面或论文后通常自动更新；
修改 `_config.yml` 后按 Ctrl+C 并重新运行。若端口已被当前预览占用，
可用 `PORT=8001 bash scripts/preview.sh`。

在另一台已有 Ruby 3.3 的电脑上：

```bash
gem install bundler -v 2.4.22
bundle install
bundle exec jekyll serve --host 127.0.0.1 --port 8000
```

只构建、不启动服务：

```bash
bash scripts/build.sh
python3 tests/check_site.py
```

## 在哪里修改个人信息

| 内容 | 文件 |
| --- | --- |
| 姓名、邮箱、Scholar/GitHub、网站地址 | `_config.yml` |
| 首页简介、研究兴趣、三个资源入口 | `_pages/about.md` |
| News 动态（位于首页论文列表上方） | `_news/` 中的 Markdown 文件 |
| 照片 | `assets/img/yulong-2026.jpg`，文件名在 `_pages/about.md` 中配置 |
| 论文列表、链接和预览图文件名 | `_bibliography/papers.bib` |
| 论文图片 | `assets/img/publication_preview/` |
| CV 中的教育、经历、奖项 | `_data/cv.yml` |
| CV 的导航和 PDF 下载按钮 | `_pages/cv.md` |

具体增删、隐藏方法见 [EDITING.md](EDITING.md)。
旧版的 `site.json` 和 `build.py` 已不再使用。

## 上传并替换现有 GitHub Pages

本次只改了本机文件，没有向 GitHub 提交或发布。确认预览后再进行以下步骤。
新的工作流使用 Jekyll 构建，不要沿用旧版 Python 工作流。

1. 打开 `mura1n/mura1n.github.io` 的 **Settings → Pages**，
   将 **Build and deployment → Source** 设为 **GitHub Actions**。
2. 在一个新的本地目录克隆现有仓库，保留仓库历史：

```bash
cd /Users/mercury/Projects
git clone https://github.com/mura1n/mura1n.github.io.git mura1n-pages-upload
cd /Users/mercury/Projects/mura1n-pages-upload
git branch backup-before-alfolio
```

如果 `mura1n-pages-upload` 已存在，不要覆盖其中未提交的修改；
先查看 `git status`，或选择一个新的目录名。

3. **以下同步会删除上传副本中旧模板的文件**，但保留 `.git` 和提交历史。
   先预览，再执行。两个路径不要换成主目录或 Projects 根目录。

```bash
rsync -av --dry-run --delete \
  --exclude='.git/' --exclude='_site/' --exclude='.bundle/' \
  --exclude='.jekyll-cache/' --exclude='.jekyll-metadata' \
  --exclude='.sass-cache/' --exclude='vendor/' --exclude='.DS_Store' \
  /Users/mercury/Projects/mura1n-homepage/ \
  /Users/mercury/Projects/mura1n-pages-upload/
```

确认列出的增删符合预期后，去掉上面命令中的 `--dry-run` 再运行一次。

4. 检查并上传：

```bash
cd /Users/mercury/Projects/mura1n-pages-upload
git status --short
git add -A
git diff --cached --stat
git commit -m "Use original al-folio template with publication previews"
git push origin HEAD
```

此命令不会强制推送。工作流同时支持 `master` 和 `main`，
无需为了建站重命名现有分支。等待仓库 **Actions** 中
“Build and deploy homepage” 成功后访问 https://mura1n.github.io/。

GitHub Pages 配置依据：
https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages

## 模板和隐私

- 保留原模板的 MIT LICENSE，来源见 `TEMPLATE_ORIGIN.md`。
- 原作者的个人资料、照片、论文和社交账号没有迁入。
- 未启用统计、广告、Blog 或评论。
- 网站源代码公开时，写在源码里的内容也会公开。
  “不显示在网页上”不等于“保密”，不要把私密信息写进源码或 Git 历史。
