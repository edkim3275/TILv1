# Git

## 작업과정

- frontend에서 local 브랜치를 하나 만들어주기

  `git checkout -b <branch_name> <상위 branch_name>`

  ex) `git checkout -b fe/feature/#2 frontend`

- 새로운 브랜치에서 작업하면서 지속적으로 add, commit 하기

  `git add .`

  `git commit -m 'commit message'`

- merge하기 전에 상위 브랜치로 이동하기

  `git checkout frontend`

- 기록을 남기면서 merge하기

  `git merge --no-ff <branch_name>`

- 작업을 했던 브랜치 삭제하기

  `git branch -d <branch_name>`

- 'frontend' 브랜치를 원격 중앙 저장소에 올린다.

  `git push origin frontend`

