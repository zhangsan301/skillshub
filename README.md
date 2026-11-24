# SkillHub

个人常用 Skill 的分类管理站点（单文件 HTML，数据存浏览器 localStorage，支持 GitHub Gist 多端同步）。

- 应用入口：`index.html`（已由 GitHub Pages 部署）
- 站点技能库：`skills/index.json`（清单）+ `skills/<name>/SKILL.md`（正文）
- 把仓库链接粘贴进页面「从 GitHub 链接导入」（形如 `https://github.com/zhangsan301/skillshub/tree/main/skills`）即可把 8 个技能装回本机记录

## 收录的 8 个 Skill

| Skill | 分类 | 用途 |
|---|---|---|
| ffmpeg-skill | 影视剪辑 | 本地 FFmpeg 剪视频，素材不出本机 |
| last30days | 调研 | 近 30 天多信源话题调研 |
| modern-web-guidance | 编程 | 现代 Web 写法检索小抄 |
| open-code-review | 编程 | OCR 原生代码审查 |
| open-code-review-delegate | 编程 | 复用宿主模型的代码审查 |
| plannotator-review | 编程 | diff 划词批注，意见一次回给 Agent |
| stitch-generate-design | 设计与创意 | 调 Stitch 出 UI 设计稿 |
| stitch-react-components | 编程 | Stitch 设计稿转 React 组件 |

## 自动同步

`.github/workflows/sync-skills.yml` 会在 `skills/index.json` 变更或手动触发时，按每个条目的 `upstream` 地址抓取上游最新 `SKILL.md` 提交到 `skills/<name>/SKILL.md`。

## 说明

本仓库只存 `SKILL.md` 正文与清单；脚本依赖见 `skills/index.json` 的 `note` 字段，按需自行安装。
