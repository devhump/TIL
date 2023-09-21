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


```ad-note
- [[#유사한 문서|유사한 문서]]
- [[#intro|intro]]
- [[#1. 원격저장소에 업로드 하기|1. 원격저장소에 업로드 하기]]
- [[#2. 원격저장소 그대로 내려받기|2. 원격저장소 그대로 내려받기]]
- [[#3. 원격저장소 변동사항 불러오기|3. 원격저장소 변동사항 불러오기]]
	- [[#3. 원격저장소 변동사항 불러오기#git pull의 이해|git pull의 이해]]
- [[#4. branch 만드는 방법 & 업로드|4. branch 만드는 방법 & 업로드]]
	- [[#4. branch 만드는 방법 & 업로드#로컬 브랜치 원격저장소에 올리기|로컬 브랜치 원격저장소에 올리기]]
- [[#5. Pull request|5. Pull request]]
- [[#6. git flow / trunk-based 브랜치 전략|6. git flow / trunk-based 브랜치 전략]]
	- [[#6. git flow / trunk-based 브랜치 전략#안정적인 운영이 필요하면 git flow|안정적인 운영이 필요하면 git flow]]
	- [[#6. git flow / trunk-based 브랜치 전략#Trunk-based 전략|Trunk-based 전략]]
		- [[#Trunk-based 전략#trunk-based 전략 적용 예시|trunk-based 전략 적용 예시]]
		- [[#Trunk-based 전략#trunk-based 전략의 특징|trunk-based 전략의 특징]]
	- [[#6. git flow / trunk-based 브랜치 전략#프로젝트에서 어떤 전략을 사용하는게 유리할까|프로젝트에서 어떤 전략을 사용하는게 유리할까]]
```

#### intro
- repository : 저장소 
	- local: `.git` 폴더
	- online(원격저장소) : 대표적으로 github

- 원격 저장소를 사용하는 이유
	1. 로컬 저장소의 내용 백업
	2. 협업을 위해 

- main branch 이름 변경(master → main)
```shell
git branch -M main
```


### 1. 원격저장소에 업로드 하기
```shell
git push -u 원격저장소주소 main

# 깃헙저장소 변수에 넣어 사용하기
git remote add origin http://github.com/dev/TIL.git
# 이후 아래와 같은 축약된 명령어 사용가능
git push -u origin main

# -u 옵션을 사용한 이후에는 더 축약된 명령어 사용가능
git push
```
- 👉 `-u` 옵션은 방금 입력한 주소를 기억하라는 의미
- 👉 `git remote -v` : 해당 저장소의 변수목록 확

### 2. 원격저장소 그대로 내려받기
```shell
git clone http://github.com/dev/TIL.git
```
- 👉 필요할 땐 특정 브랜치 1개만 clone 하는 것도 가능


### 3. 원격저장소 변동사항 불러오기
```shell
git pull 원격저장소주소

# 특정브랜치만 가져오기
git pull 원격저장소주소 특정브랜치명

# git push 단계에서 `-u` 옵션을 사용한 경우
# 짧은 단축 명령어로 사용 가능
git pull
```

#### git pull의 이해
- `git fetch` + `git merge` 의 의미
	- `git fetch` : 원격저장소에 있는 commit 중에서 로컬에 없는 신규 commit 내용을 가져와라- 라는 의미
	- `git merge` : commit 내역들을 merge 하라

### 4. branch 만드는 방법 & 업로드
1. github 에서 직접 branch 생성하기
2. 로컬에서 branch 생성하기

```shell
git branch 새브랜치명
git switch 새브랜치명

# 또는

git checkout -b 새브랜치
```

#### 로컬 브랜치 원격저장소에 올리기
```shell
# 특정 로컬저장소 브랜치 → 원격저장소
git push 원격저장소주소 로컬브랜치명

# 모든 로컬저장소 브랜치 → 원격저장
git push 원격저장소주소 
```


### 5. Pull request
- 개인 프로젝트의 경우 로컬에서 merge 후 push 해도 가능하나, <br>협업의 경우 merge 이전 코드 리뷰/ 검토의 과정을 거침. 이 때 사용하는 것이 _pull request_이다.
	- 👉 PR 과정에서 merge 방식 선택도 가능하다. (3-way merge, squash and merge, rebase and merge)


### 6. git flow / trunk-based 브랜치 전략
- 여러명이서 협업을 할 때에, 브랜치를 마음가는 대로 만들다 보면 개발과정이 복잡해지고, 코드의 추적이 어려울 수 있다. 이를 위해 git branch를 깔끔하게 관리할 수 있게 도와주는 방법론들이 있는데, git flow, github flow, gitlab flow, trunk-based 등 여러가지가 있다.

- 이러한 방법론의 장점으로는 
1. 브랜치관리가 쉬워지고 
2. 팀원이 아무리 많아도 개발절차가 매끄러워진다. 
- 👉 프로젝트 리드하는 입장에서 도움이 된다.

#### 안정적인 운영이 필요하면 git flow

| branch 명 | 역할                                                     |
| --------- | -------------------------------------------------------- |
| main      | 주 브랜치                                                |
| develope  | 개발용                                                   |
| feature   | develop에 기능 추가용                                    |
| hotfix    | main 브랜치 버그 해결용                                  |
| release   | develop 브랜치를 main 브랜치에 합치기 전에 최종 테스트용 |

- 👉 필요에 따라 더하거나 빼면서 사용할 것 (단, 선택과 적용에 대한 합당한 근거가 필요)
![](assets/Git%20basic%20-%20Github%20manual.png)^출처: [코딩애플 - git 강의](https://codingapple.com/wp-content/uploads/2022/07/%EA%B7%B8%EB%A6%BC6.png)

#### Trunk-based 전략
- 규모가 적거나, 조금씩 소소한 기능들만 업데이트를 하는 경우, 주요 코드는 main 브랜치에 유지하면서, feature 브랜치만 운영하는 경우를 가리킨다. 

![](assets/Git%20basic%20-%20Github%20manual-1.png)^출처: [코딩애플 - git 강의](https://codingapple.com/wp-content/uploads/2022/07/%EA%B7%B8%EB%A6%BC7.png)

##### trunk-based 전략 적용 예시
1. 기능추가, 버그픽스가 필요하면 main 브랜치에서 새로운 브랜치를 하나 만들어서 코드짭니다. (브랜치마다 작명 잘하는게 중요) 
2. 기능이 완성되었으면 main 브랜치에 합칩니다. (합친 브랜치 쓸데없으니 삭제)
3. main 브랜치에 있는 코드를 필요할 때 마다 유저들에게 배포합니다.

##### trunk-based 전략의 특징
- trunk-based 개발의 장점은 **코드를 한 브랜치에서만 관리하기 때문에 편리**합니다. 
- 크게 개발해서 한 번에 merge 하는 것 보다 작은 단위로 merge 하는 것이 더 안전합니다. 
- 하지만 main 브랜치에 있는 코드가 오류가 나면 큰일나기 때문에 테스트나 코드리뷰를 자주해야합니다.
	- 그래서 테스트를 자주하고 자동화해놓는 곳들이 제대로 사용가능합니다.


#### 프로젝트에서 어떤 전략을 사용하는게 유리할까
- 이미 어느정도 개발이 진척이 되었거나 프로 코딩전사들로 가득한 팀이면 trunk-based 이런거 쓰는게 훨씬 편리합니다.
- 최근 유행한 CI/CD 이런 식으로 개발하는 곳들도 trunk-based 개발방식을 적용합니다.  
- 출시된 버전의 안정성이 중요한 프로그램들, 아직 뼈대가 확실하지 않아 연구식으로 개발하는 프로그램들은 git flow가 적절할 수 있습니다.

```ad-tip
- **Q. merge 할 때 어떤 방법 쓰는게 좋은가요?**
	- 기록을 남겨야하는 중요한 브랜치를 merge할 땐 3-way merge
	- 기록을 남길 필요없는 쓸데없는 브랜치를 merge할 땐 squash, rebase 쓰면 됩니다. 

- **취향일 뿐이고 필요에 따라 적절한 방법을 사용하면 된다.**
```


