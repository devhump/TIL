---
tags: [git, CodingApple/git]
---

#### 유사한 문서
``` dataview
list from #git 
sort file.name ASC
```

- 그 외 git 관련 문서
	👉 [git_cheat_sheet](git_cheat_sheet.pdf)
	👉 [Git Manual Book (official)](https://git-scm.com/book/ko/v2)

### git stash (코드 잠깐 보관하기)
```shell
git stash
```
- 현재 코드를 작성 중인 상태에서 위 명령어를 입력하면, ***해당 코드들은 임시 저장 공간에 보관이 되며, 파일들이 최근 commit 상태로 돌아간다.***
	- 추적중인 파일(tracked)은 staging 여부와 관계 없이 이동이된다.
	- _staging이 안 된 새로 만든 파일_ 은 이동하지 않는다. (코드가 삭제된다.)

```shell
# stash 할 때 메모도 입력가능 하다
git stash save "메모 적기"

# 현재 stash 된 코드 목록을 출력한다. 
git stash list
```
- 👉 `stash` 명령어는 여러번 사용 가능하다. 

#### 보관했던 코드 다시 불러오기
```shell
# 가장 최근에 보관했던 코드를 불러온다.
git stash pop

# 특정 순번의 stash 코드를 불러온다
git stash pop 번호
```

![](assets/Git%20basic%20-%20git%20stash.png)

#### stash 관련 여러 명령어들
```shell
# 특정 stash 삭제
git stash drop 삭제할id

# 모든 stash 삭제
git stash clear 

# 일부 코드만 stash 하고 싶을 때 
git stash -p
```

![](assets/Git%20basic%20-%20git%20stash-1.png)

```ad-tip
- **주석 처리하는 게 더 쉽지 않을까?**
	- 주석처리된 코드는 commit 할 때 반영이 된다. 이때 commit 기록을 남기지 않고 싶을 때 `stash` 키워드를 사용하면 된다.
- 또는 유사한 상황에서 브랜치를 새로 만들어 사용하는 경우도 있을 수 있다. 결국 상황에 맞춰, 적절한 방법을 사용하면 된다.
```

