---
tags: [git, syntax]
alias: 
- Git의 기초 - 되돌리기
---

- 전반적인 git 내용은 👉 [[Git]]

- `git add, git commit, git add` 취소하기 등 이전 내용으로 되돌리고 싶다면?
	- 👉 [[Git basic - rollback]]
- `git merge`에 관한 자세한 내용은?
	- 👉 [[Git basic - merge]]

- 그 외 git 관련 문서
	👉 [git_cheat_sheet](git_cheat_sheet.pdf)
	👉 [Git Manual Book (official)](https://git-scm.com/book/ko/v2)

---



```ad-note
- [[#1.  완료된 커밋을 (살짝) 수정해야할 때|1.  완료된 커밋을 (살짝) 수정해야할 때]]
- [[#2. git add 취소하기 (파일 상태를 Unstage로 변경하기)|2. git add 취소하기 (파일 상태를 Unstage로 변경하기)]]
- [[#3.  git commit 취소하기|3.  git commit 취소하기]]
- [[#4.  Modified 파일 되돌리기|4.  Modified 파일 되돌리기]]
- [[#5. git push 취소하기|5. git push 취소하기]]
	- [[#1. 워킹 디렉터리에서 commit을 되돌린다.|1. 워킹 디렉터리에서 commit을 되돌린다.]]
	- [[#2. 되돌려진 상태에서 다시 commit을 한다.|2. 되돌려진 상태에서 다시 commit을 한다.]]
	- [[#3. 원격 저장소에 강제로 push한다.|3. 원격 저장소에 강제로 push한다.]]
- [[#6. untracked 파일 삭제하기|6. untracked 파일 삭제하기]]
- [[#참고|참고]]
```


### 1.  완료된 커밋을 (살짝) 수정해야할 때
- 너무 일찍 커밋을 했다
- 어떤 파일을 뺴먹었을 때
- 커밋 메시지를 잘못 적었을 때 

```shell
git commit --amend
```

- 만약 마지막 커밋 이후 수정한 것이 없다면 -커밋 직후 바로 위 명령어를 실행할 경우-, 조금 전 한 커밋과 모든 것이 동일하다. 
	- **이때는 커밋 메시지만 수정한다.** 
	- 이때 편집기가 실행되면 이전 커밋 메시지가 자동으로 포함되고, 메시지 수정 없이 커밋해도 기존의 커밋을 덮어쓴다. 
- *커밋을 했는데, stage 하는 것을 깜빡하고, 빠뜨린 파일이 있으면 아래와 같이 고칠 수 있다.*
```shell
git commit -m 'initial commit'
git add forgotten_file
git commit --amend
```

- `--amend` 옵션으로 커밋을 수정하면, 기존 커밋은 사라지고, 수정한 커밋만 남는다. 
	- 로그에 수정된 하나의 히스토리만 존재한다.
	- `--amend` 옵션으로 수정하는 건, '앗차, 빠진 파일 넣었음.', '이전 커밋에서 오타 살짝 고침' 같은 추가 커밋없이, 기존 커밋 내용을 수정하는 개념이다. 



### 2. git add 취소하기 (파일 상태를 Unstage로 변경하기)
- 가령, 두 개의 파일을 따로 커밋하려고 했으나, 실수로 `git add *` 명령어를 사용했다고 하자. 이 파일들은 staging area에 있는데, 이를 working directory로 돌리는 방법이다. 
```shell
git add *
git status
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

    renamed:    README.md -> README
    modified:   CONTRIBUTING.md
```

- git reset HEAD `[file]`
	- 이때 파일명이 없으면 add한 파일 전체를 취소한다.  

```shell
git reset HEAD CONTRIBUTING.md
Unstaged changes after reset:
M	CONTRIBUTING.md

git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

    renamed:    README.md -> README

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

    modified:   CONTRIBUTING.md

```

- 📌 `git reset ` 명령어는 매우 위험하다. 특히 `--hard` 옵션과 함께 사용 하면 더욱!



### 3.  git commit 취소하기 
```
git reset HEAD^
```
- ***직전에 commit한 내용을 취소한다.***

```shell
// [방법 1] commit을 취소하고 해당 파일들은 staged 상태로 워킹 디렉터리에 보존
git reset --soft HEAD^

// [방법 2] commit을 취소하고 해당 파일들은 unstaged 상태로 워킹 디렉터리에 보존
git reset --mixed HEAD^ // 기본 옵션
git reset HEAD^ // 위와 동일
git reset HEAD~2 // 마지막 2개의 commit을 취소

// [방법 3] commit을 취소하고 해당 파일들은 unstaged 상태로 워킹 디렉터리에서 삭제
git reset --hard HEAD^
```

-  옵션에 따른 구분 

| 옵션      | index 구분 | add / staged 상태              | 워킹 디렉터리 |
| :---------: | :----------: | ------------------------------ | ------------- |
| `--soft`  | index 보존 | add한 상태, staged 상태        | 파일 보존     |
| `--mixed` <br> (***기본 옵션***) | index 취소 | add하기 전 상태, unstaged 상태 | 파일 보존     |
| `--hard`  | index 취소 | add하기 전 상태, unstaged 상태 | 파일 삭제    |

- 워킹 디렉터리를 원격 저장소의 마지막 commit 상태로 돌리고 싶다면
	- 📌==주의! 마지막 커밋 이후 수정한 모든 내용이 사라진다 ! ==
```
git reset --hard HEAD
```



### 4.  Modified 파일 되돌리기
파일을 수정 후 이전 버전으로 돌리는 방법이다. 최근 커밋 또는 특정 시점으로 파일의 내용을 복구하고 싶을 때 쓴다. 

```console
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

    modified:   CONTRIBUTING.md
```

```shell
git checkout -- CONTRIBUTING.md
git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

    renamed:    README.md -> README
```

- 📌 `git checkout --<file>` 명령어는 꽤 위험하다.  특정 커밋 이후 수정된 내용이 전부 사라져 버린다. ***단, 커밋하지 않은 내용을 복구하는 건 절대 불가능 하다!***



### 5. git push 취소하기
```ad-caution
- 📌이 명령은 원격 저장소(remote repo)의 내용을 ***자신의 로컬(local) 내용으로 강제 덮어쓰기는 하는 것***이기 때문에 ==매우 주의== 해야 한다.  
	- <u>되돌아간 commit 이후 모든 commit 정보가 사라지기 때문에 주의해야한다!</u>
	- 특히, 협업 프로젝트 간 동기화 문제가 발생할 수 있어, 팀원들과 상의 후 진행하는 것이 좋다!

```

##### 1. 워킹 디렉터리에서 commit을 되돌린다. 
- 방법 1) 가장 최근의 commit을 취소하고 워킹 디렉터리를 되돌린다. 
```shell
	git reset HEAD^
```

- 방법 2) 원하는 시점으로 워킹 디렉터리를 되돌린다. 
```shell
// Reflog(브랜치와 HEAD가 지난 몇 달 동안에 가리켰었던 커밋) 목록 확인
git reflog
또는
git log -g

// 원하는 시점의 워킹 디렉터리로 되돌린다.
git reset HEAD@{number}
또는
git reset [commit id]
```

```ad-example 
title: ##### reflog 예시

- 기존 `git log` 예시
	- ![](assets/Git의%20기초%20-%20되돌리기-img-%20(2).png)

- `git reflog` 예시
	- ![](assets/Git의%20기초%20-%20되돌리기-img-%20(1).png)

- `git log -g` 예시
	- ![](assets/Git의%20기초%20-%20되돌리기-img-%20(3).png)
```

^c92f46

##### 2. 되돌려진 상태에서 다시 commit을 한다.
```shell
git commit -m "commit-message" 
```

##### 3. 원격 저장소에 강제로 push한다. 
```shell
git push origin [branch_name] -f
또는
git push origin +[branch_name]
// ex) git push origin +master
```
- 👉 `-f` (force) 옵션이나 `+[branch_name]` 둘다 <u>경고를 무시하고 강제로 push 한다.</u>



### 6. untracked 파일 삭제하기
- `git clean` 명령어는 추적중이지 않은 파일만 지우는 게 기본 동작이다. 
	- **이때, `.gitignore`에 포함되어 무시되는 파일은 지우지 않는다 !**
```shell
git clean -f // 디렉터리를 제외한 파일들만 삭제
git clean -f -d // 디렉터리까지 삭제
git clean -f -d -x // 무시된 파일까지 삭제
```

| 옵션  | 기능                                                                   |
|:-----:|:---------------------------------------------------------------------- |
| `-d ` | 디렉터리까지 지운다                                                    |
| `-x`  | 무시된 파일까지 전부 삭제(`.DS_Store` 또는 `.gitignore`에 포함된 것들) |
| `-n`  | 가상으로 실행 후 명령어 실행 후 지워질 파일들 보여줌                   |



### 참고
- 유사한 내용 링크
	- [Github에 잘못 올라간 파일 삭제하기](https://gmlwjd9405.github.io/2018/05/17/git-delete-incorrect-files.html)
- 참고한 문서
	- [git add 취소하기, git commit 취소하기, git push 취소하기](https://gmlwjd9405.github.io/2018/05/25/git-add-cancle.html)
	- [2.4 Git의 기초 - 되돌리기](https://git-scm.com/book/ko/v2/Git%EC%9D%98-%EA%B8%B0%EC%B4%88-%EB%90%98%EB%8F%8C%EB%A6%AC%EA%B8%B0)