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

---
### git branch 이동
```shell
# 만들고서 이동
git branch 브랜치이름
git switch 브랜치이름

# 만들면서 이동
git checkout -b 브랜치이름

```

### git merge
- branch를 따서 각각 다른 파일을 작업하면 이후 병합 과정(merge)에서 문제가 없으나,<br>==동일한 파일을 수정할 경우 conflict(충돌)이 발생한다.==

![](assets/Git%20basic%20-%20merge.png)

![](assets/Git%20basic%20-%20merge-1.png)

![](assets/Git%20basic%20-%20merge-2.png)

- 👉 충돌사항을 확인하고 정리한뒤, merge 한 결과이다. 이때, **'HEAD'** 는 자신의 현재 위치를 가르킨다. 

### 3-way merge
![](assets/Git%20basic%20-%20merge-3.png)
- main(master) branch와 새로운 branch에 각각 새로운 커밋이 존재하고, 이를 하나로 merge하는 방식을 `3-way merge`라고 부른다. 

### fast-forward merge
![](assets/Git%20basic%20-%20merge-4.png)
- 새로운 branch에는 새로운 커밋이 존재하고, main(master) branch에는 새로운 내용이 없는 경우, 새로운 branch의 마지막 커밋이 main(mater) 브랜치가 된다. 이 방식이 `fast-forward merge` 이다. ==(`git merge 브랜치명` 입력시 자동으로 이뤄짐)==

![](assets/Git%20basic%20-%20merge-17.png)

![](assets/Git%20basic%20-%20merge-18.png)

```shell
# fast-forward merge가 싫을 경우
git merge --no-ff 브랜치명
# 이 경우 강제로 3-way merge를 발생시킨다.
```

### 브랜치의 삭제
```shell
# 병합이 완료된 브랜치 삭제시
git branch -d 브랜치 이름

# 병합이 완료되지 않은 브랜치 삭제시
git branch -D 브랜치 이름
```

### rebase and merge

![](assets/Git%20basic%20-%20merge-5.png)

#### rebase 
- 브랜치의 시작점을 다른 commit으로 옮겨주는 행위
	1. rebase를 이용해서 신규브랜치의 시작점을 main 브랜치 최근 commit으로 옮긴 다음 
	2. fast-forward merge하는 것
- _rebase 사용하는 이유?_
		- 👉 3-way merge 말고 강제로 fast-forward 하고 싶을 때

#### rebase and merge 하는 방법
1. 새로운 브랜치로 먼저 이동해서
2. git rebase main 하면 됩니다. 
3. 그럼 브랜치가 main 브랜치 끝으로 이동하는데 그걸 fast-forward merge 하면 됩니다.

```shell
git switch 새로운브랜치
git rebase main

git switch main
git merge 새로운브랜치
```
- 👉 rebase & merge를 한 줄로 쉽게 비유하자면 **강제 fast-forward merge**입니다. 단점은, branch 끼리의 차이가 많이 나는 경우, 많은 충돌이 발생할 수 있으니 주의할 것 

### squash and merge

![](assets/Git%20basic%20-%20merge-6.png)

- 위의 예시처럼, 모든 브랜치가 3-way merge를 할 경우, git log가 굉장히 복잡해 진다. 
	1. 3-way merge 된 것들은 매우 복잡해보임 
	2. main 브랜치 git log 출력해보면 3-way merge된 브랜치들의 commit 내역도 다 같이 출력되어서 한눈에 알아보기 어려움.

![](assets/Git%20basic%20-%20merge-7.png)

- 브랜치에서 만들어놨던 많은 commit 을 다 합쳐서 하나의 commit으로 main 브랜치에 생성해준다.

```shell
git switch main
git merge --squash 새브랜치명
git commit -m '메세지'
```

![](assets/Git%20basic%20-%20merge-8.png)

- 위의 예시처럼 git log graph가 이어지지 않고 떨어져 있다. 

- 현업에서는 회사별로 가이드 라인이 있으니 이를 실무에 적용하면 된다. 

### 참고


```shell
git log --oneline --graph
```

![](assets/Git%20basic%20-%20merge-20.png)

```shell
git log --oneline --all --graph
```

![](assets/Git%20basic%20-%20merge-19.png)