---
tags: [git]
---

### git restore : 파일 하나 되돌리기
```shell
git restore 파일명
# 최근 커밋된 상태로 현재 파일 수정 내역 되돌림

git restore --source 커밋아이디 파일명
# 입력한 파일이 특정 커밋 시점으로 복구됨

gir restore --staged 파일명
# 특정 파일의 staging 취소
```

### git revert : commit 되돌리기 
```shell
git revert 커밋아이디
# 해당 commit을 취소한 commit을 생성

git revert 커밋아이디1 커밋아이디2
# 여러개의 커밋아이디 입력가능

git revert HEAD
# 가장 최근의 커밋 1개만 취소
```
- merge 명령으로 만들어진 commit도 revert 가능

### git reset : 과거 코드로 회귀하기
```shell
git reset --hard 커밋아이디
# 해당 커밋이 생성되던 시점으로 시간을 돌려줌
```
- ==협업하는 레포지토리에서는 사용 하지 말것 !!==
- 짧은 거리를 돌아갈 때만 사용하기
- untracked 파일들은 (git add 안해놓은 파일들은) 사라지지않고 유지됨
- git clean 명령어 찾아서 쓰면 untracked 파일들도 다 지울 수 있다.

#### git reset 옵션
![](assets/Git%20basic%20-%20git%20revert,%20reset,%20restore.png)

```shell
git reset --hard d874b2b
# 이러면 a, b파일은 남아있고 c 파일이 삭제됩니다. 

git reset --soft d874b2b
# 이러면 a, c파일은 남아있고 b 파일은 staging area에 남아있습니다. 
# 이제 commit 하거나 그럴 수 있습니다. 

git reset --mixed d874b2b
# 이러면 a, c파일은 남아있고 b 파일은 staging 되지 않은 상태가 됩니다. 
# 이제 git add 하고 commit 하거나 그럴 수 있습니다.
```
- 👉 결론은 **reset하면서 파일을 아예 지워버리는게 아니라** 검토하고 다시 commit 하고 싶으면 `--soft / --mixed` 사용해봅시다. 
	- 옵션값 없이 `git reset 커밋아이디` 를 사용하면 `--mixed 옵션이 자동`으로 발동됩니다.
