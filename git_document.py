git init                        把命令变成git可以管理的仓库
git add                       添加到仓库
git commit -m “”        提交(引号注释)
git status                   查看状态结果
git diff                        查看修改内容
git log                        查看历史记录操作
git log --pretty=oneline        查看历史记录操作
git reset --hard HEAD^        回滚上一个版本(HEAD~100回滚第100个版本)
git reset --hard (commin id) 回滚到指定commit id的版本
git reflog                     记录每次操作命令
git checkout -- file_name      丢弃工作区修改
git reset HEAD file_name     修改文件内容提交到暂存区,可撤回
git rm → git commit              适用于删除文件后,在git上确认删除
git checkout -- file_name      误删文件可以在git恢复
github创建新的仓库-->git remote add origin git@github.com:username/pro_name.git
git push -u origin master        初次推送到远程仓库
git push origin master             再次推送可简化
git clone git@github.com:username/pro_filename.git
git checkout -b dev         创建并切换dev分支相当于 git branch dev-->git checkout dev
git branch                        查看当前分支
git checkout mester         切换mester分支
git merge dev                   分支成果合并到mester分支
git branch -d dev              删除dev分支
git merge --no-ff -m “” dev        删除分支保留分支信息
git stash                            暂时退出当前工作
git stash list                       查看
git stash pop                     恢复暂停的工作区并删除stash内容
git stash apply-->git stash drop        恢复后需要手动删除
git branch -D <name>        强行删除一个分支
git remote                           查看远程仓库信息,-v可查看更详细信息



