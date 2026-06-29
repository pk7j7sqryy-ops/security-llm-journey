
#!/bin/bash
# 一键推送 GitHub 脚本
# 用法：把这个文件放到 00-github_share 文件夹里
#   首次给它执行权限（只需一次）：chmod +x push.sh
#   以后每次更新：./push.sh  或  ./push.sh "这次改了啥"

# 如果你给了提交说明就用你的，没给就用日期
if [ -z "$1" ]; then
  MSG="update $(date '+%Y-%m-%d %H:%M')"
else
  MSG="$1"
fi

echo "▶ 添加所有改动..."
git add .

echo "▶ 提交：$MSG"
git commit -m "$MSG"

echo "▶ 推送到 GitHub..."
git push

echo "✅ 完成！去 GitHub 刷新看看吧"