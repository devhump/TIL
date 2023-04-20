---
tags: [git, syntax, KDT]
alias: "Git 기초"
---

👉 [git_cheat_sheet](git_cheat_sheet.pdf)
👉 [Git Manual Book (official)](https://git-scm.com/book/ko/v2)

- `git add, git commit, git add` 취소하기 등 이전 내용으로 되돌리고 싶다면?
	- 👉 [[Git basic - rollback]]

### 목차
```ad-hint
- [[#목차#Git 기초 명령어 (local)|Git 기초 명령어 (local)]]
- [[#목차#원격 저장소 설정 기본 명령어 (remote)|원격 저장소 설정 기본 명령어 (remote)]]
- [[#1. 개요|1. 개요]]
- [[#2. git 초기 설정|2. git 초기 설정]]
	- [[#2. git 초기 설정#2-1. $ git init|2-1. $ git init]]
	- [[#2. git 초기 설정#2-2. $ git add `<file>`|2-2. $ git add `<file>`]]
	- [[#2. git 초기 설정#2-3. $ git commit -m `<커밋메시지>`|2-3. $ git commit -m `<커밋메시지>`]]
		- [[#2-3. $ git commit -m `<커밋메시지>`#commit 이해하기|commit 이해하기]]
		- [[#2-3. $ git commit -m `<커밋메시지>`#commit 3단계의 이해|commit 3단계의 이해]]
	- [[#2. git 초기 설정#2-4. $ git log|2-4. $ git log]]
	- [[#2. git 초기 설정#2-5. $ git status|2-5. $ git status]]
	- [[#2. git 초기 설정#2-6. Git 설정 파일 (config)|2-6. Git 설정 파일 (config)]]
- [[#3. 원격 관리 시작하기|3. 원격 관리 시작하기]]
	- [[#3. 원격 관리 시작하기#$ git push <원격저장소이름> <브랜치 이름>|$ git push <원격저장소이름> <브랜치 이름>]]
		- [[#$ git push <원격저장소이름> <브랜치 이름>#원격저장소 경로 설정|원격저장소 경로 설정]]
		- [[#$ git push <원격저장소이름> <브랜치 이름>#push 실패시|push 실패시]]
	- [[#3. 원격 관리 시작하기#$ git pull <원격저장소이름> <브랜치이름>|$ git pull <원격저장소이름> <브랜치이름>]]
	- [[#3. 원격 관리 시작하기#$ git clone <원격저장소 주소>|$ git clone <원격저장소 주소>]]
- [[#4. Git 사용시 주의 사항|4. Git 사용시 주의 사항]]
	- [[#4. Git 사용시 주의 사항#git 사용시 항상 경로 확인 !|git 사용시 항상 경로 확인 !]]
	- [[#4. Git 사용시 주의 사항#commit에 관하여|commit에 관하여]]
	- [[#4. Git 사용시 주의 사항#원격저장소 조작 금지|원격저장소 조작 금지]]
	- [[#4. Git 사용시 주의 사항#마크다운 이미지 경로 이슈|마크다운 이미지 경로 이슈]]
- [[#5. 기타|5. 기타]]
	- [[#5. 기타#5-1. `.gitkeep`|5-1. `.gitkeep`]]
	- [[#5. 기타#5-2 `.gitignore`|5-2 `.gitignore`]]
	- [[#5. 기타#5-3. 저장소(repository) 관련|5-3. 저장소(repository) 관련]]
		- [[#5-3. 저장소(repository) 관련#1) 저장소 이름 변경|1) 저장소 이름 변경]]
		- [[#5-3. 저장소(repository) 관련#2) 저장소 접근 관리|2) 저장소 접근 관리]]
		- [[#5-3. 저장소(repository) 관련#3) 원격저장소 다운로드 방법|3) 원격저장소 다운로드 방법]]
	- [[#5. 기타#5-4. 그 외|5-4. 그 외]]
	- [[#5. 기타#5-5. 참고|5-5. 참고]]
```


#### Git 기초 명령어 (local)
| 명령어                       | 내용                            |
| ---------------------------- | ------------------------------- |
| git init                     | 로컬 저장소 생성                |
| git add <파일명>             | 특정 파일/ 폴더의 변경사항 추가 |
| git commit -m '<커밋메시지>' | 커밋(버전 기록)                 |
| git status                   | 상태확인                        |
| git log                    |  버전 확인                    |


#### 원격 저장소 설정 기본 명령어 (remote)
| 명령어          | 내용             |
| :--------------- | :----------------: |
| git clone `<url>`                |                원격 저장소 복제                      |
| git remote -v                                    | 원격저장소 정보 확인                |
| git remote add <원격저장소> `<url>`                | 원격저장소 추가 (일반적으로 origin) |
| git remote rm  <원격저장소>                      | 원격저장소 삭제                     |
| git push <원격저장소> <브랜치>                   | 원격저장소에 push                   |
| git pull <원격저장소> <브랜치>                            | 원격저장소로부터 pull               |

👉 [Git_cheat_sheet](assets/Git_cheat_sheet.png)
![Git_cheat_sheet](assets/Git_cheat_sheet.png)


### 1. 개요
- Git 👉 분산 버전 관리 시스템 (형상 관리 시스템)
	- 2005, 리누스 토르발즈가 개발
- **버전(version)이란?**
	- 컴퓨터 소프트웨어의 특정 상태
```md
“최종_마지막_파이널_진짜진짜.hwp”  
 ​  
“최종.hwp”  
 ​  
“최종_레알.hwp”
```
→ 내용 측면에서 차이점 비교 불가

- 컴퓨터 파일변경사항 추적 + 다중 사용자간에 해당 파일 작업 조율
	- 스냅샷 방식을 이용해서, 버전별로 **달라진 부분(diff, 차이)** 과 수정 이유에 대한 메시지를 남길 수 있다. 

- **분산버전관리시스템(DVCS)**
	- 중앙집중식 버전관리 시스템은 중앙에서 버전을 관리하고 파일을 받아서 사용
	- 분산버전 관리시스템은 원격 저장소(remote repository)를 통하여 협업하고, 모든 히스토리를 클라이언트들이 공유

---

### 2. git 초기 설정

#### 2-1. $ git init 
- 초기화 (저장소 생성)
- 특정 폴더를 git 저장소(repository)를 만들어 git으로 관리
	- `.git` 폴더가 생성되며
	- git bash 창에서는 `(master)`라는 표기를 확인할 수 있음
```bash
$ git init
```

- 기본 흐름
	1) 작업하면 
	2) add 하여 Staging area에 모아
	3) Commit으로 버전 기록

![](assets/git-img-%20(1).png)

| Working Directory | 파일의 변경사항                                  |
| ----------------- | ------------------------------------------------ |
| Staging Area      | 버전으로 기록하기 위한 <br> 파일 변경사항의 목록 |
| Repository        | 커밋(버전)들이 기록되는 곳                       |


#### 2-2. $ git add `<file>`
- commit 할 파일 추가
- working directory 상의 변경 내용을 staging area에 추가하기 위해 사용
	- untracked 상태의 파일을 staged로 변경
	- modified 상태의 파일을 staged로 변경

```shell 
 $ git add .   
 #전체 파일 추가  
 ​  
 $ git add <file_name>  
 # 특정 파일 추가  
 # git add A.txt
```

#### 2-3. $ git commit -m `<커밋메시지>`
- staged 상태의 파일들을 커밋을 통해 버전으로 기록
- SHA-1 해시를 사용하여 40자 길이의 체크섬을 생성하고, 이를 통해 고유한 커밋을 표기
- 커밋 메시지는 변경 사항을 나타낼 수 있도록 명확하게 작성해야 함

##### commit 이해하기
- Git은 데이터를 파일 시스템의 스냅샷으로 관리하고 매우 크기가 작음
- 파일이 달라지지 않으면 성능을 위해 파일을 새로 저장하지 않음
- 기존의 델타 기반 버전 관리시스템과  가장 큰 차이를 가짐

- ***Git은 파일을 modified, staged, committed로 관리***
	- **modified** : 파일이 수정된 상태 (add 명령어를 통하여 staging area로)
	- **staged** : 수정한 파일을 곧 커밋할 것이라고 표시한 상태 (commit 명령어로 저장소)
	- **committed** : 커밋된 상태

- 파일 라이프 리사이클
![](assets/git-img-%20(2).png)
```shell
$ git commit -m "커밋 메시지"  
​  
$ git commit  
# 이 경우 커밋메시지 작성을 위한 팝업이 뜸  
# "커밋메시지 길고 자세하게 작성 가능!"  
# 기본은 vim 에디터가 뜨나, 변경가능   
# (수업시간엔 vs code로 변경해서 사용)  
​  
$ git commit <filename> -m "commit_message”  
#특정 파일만 commit
```


##### commit 3단계의 이해
|                         | untracked  |      |
| ----------------------- | ---------- | ---- |
| 1. Working directory    | unmodified | 1통  |
| 🔽`$ git add`            | 🔽          | 🔽    |
| 2. Staging area (Index) | staged     | 2통  |
| 🔽`$ git commit`         | 🔽          | 🔽    |
| 3.Repository            | committed  | 3통  |

1. **Working directory** (작업 영역)
   - <u>실제 프로젝트 디렉터리</u>
   - `.git` 이력과 관련 정보가 저장된 `.git`을 제외한 모든 영역 
   - 실제 코드의 추가, 수정, 삭제 작업이 이루어지는 영역
2. **Staging Area** (Index)
   - <u>working directory 에서 repository로 정보 전송 전 준비 영역</u>
   - 파일 상태를 기록, 스테이징 한다고 표현
   - `.git/index` 파일로 관리
3. **Repository** (저장소)
   - <u>파일, 폴더를 변경 이력별로 저장해 두는 곳</u>
   - .git 디텍토리 내 존재하며 2가지로 나뉨 (local, remote)
4. **Stash 영역** (임시 영역) [^git-stash]
   - 위의 3가지 영역과 다른 별개의 임시 영역
   - 임시적으로 작업사항을 저장해 두고 나중에 꺼내올 수 있음
   - <u>"현재 stage에 있는 파일(add 하기 전 현재 수정된 파일들)을 임시적으로 저장할 수 있다."</u>

- **staging 단계가 있는 이유**
  - 버전으로 기록할 파일을 모으는 '임시공간'
- 특장점
  1. 실질적인 변경 사항을 파악, 저장해 최종 저장 용량을 최소화 가능
  2. 실서비스 사용 전에 *테스트 보드*로서 사용
- untracked/modified → staged → committed
  - 깃은 파일을 스냅샷 방법으로 저장 → 변경 사항만 저장

```bash
$ git commit -m ‘<커밋메시지>’
  
-> nothing to commit, working tree clean
#staging area 가 비어있다.
##현재 작업할 커밋 없음 (모든 파일 커밋 완료)
```

- ***`head -> master`는 해당 커밋이 master 브랜치의 마지막 커밋이라는 뜻***



- **commit message editor vs code 로 설정 하는 법**
```shell
$ git config --global core.editor "code --wait"
```

-   📌참고 `.git` 폴더에는 들어가지 말 것!
```shell
$ cd .git  
 → GIT_DIR!  
 #깃 디렉토리임! 조심!
```


#### 2-4. $ git log
- 현재 저장소에 기록된 커밋을 조회
- 다양한 옵션을 통해 로그를 조작할 수 있음

```shell
$ git log  
#현재 저장소에 기록된 커밋(버전)을 조회(전부 출력)  
​  
$ git log -1  
#최근(직전) 커밋 n건만 출력  
​  
$ git log --oneline  
#커밋 내용 한줄로 요약해서 출력  
​  
$ git log -1 --oneline  
#응용 가능
```


#### 2-5. $ git status
- **Git 저장소에 있는 파일의 상태를 확인하기 위하여 활용**
	- 파일의 상태를 알 수 있음
		- Untracked files
		- Changes not staged for commit
		- Changes to be committed
	- Nothing to commit, working tree clean
- **Status로 확인할 수 있는 파일의 상태**
	- **Untracked** : 버전으로 관리된 적 없는 파일
		- 파일을 새로 만들고 나서 한번도 add 하지 않은 상태
	
	- **Tracked** : 이전부터 버전으로 관리되고 있는 파일
		- 파일이 git에 의해 변동사항이 추적되는 상태 
			- **Unmodified** : git status에 나타나지 않음
				- 현재 파일이 최신 커밋과 비교해서 **바뀐게 없는 상태**
			- **Modified** : Changes not staged for commi
				- 현재 파일이 최신 커밋과 비교해서 **바뀐게 있는 상태**
			- **Staged** : Changes to be committed
				- 파일 수정 후 **staging area**에 올라가 있는 상태
	

```shell
$ git status
```
→ 현 상태 (변경사항) 추적

- 파일생성
  ```bash
  $ touch git.txt
  #지정한 파일형식에 따라 빈 파일 생성
  ```


#### 2-6. Git 설정 파일 (config) 
- *id 설정 없으면* → `author identity unknown`
  ​	~~***“마 니 누군데”***~~

- 사용자 정보(commit author) : 커밋을 하기 위해 반드시 필요
	- 최초 아이디/이메일 설정 (pc당 최초 1회만 실시)
```bash
$ git config --global user.name "username"
$ git config --global user.email "my@email.com"
# Github에서 설정한 username 과 email 입력
```
👉  ***id / e-mail 대소문자 주의! 되도록 소문자로 통일(권장)!***

- 잘못 입력했을 경우 (해제 방법)
    ```bash
    $ git config --unset --global user.name "기존 id"
    $ git config --unset --global user.email "기존 email"
    ```


- 설정 확인 
 ```bash
git config --global --list
# 현재 등록된 id / e-mail 도 확인 가능

git config -l
# 전체 설정 확인

git config --global -l
# global (대외) 설정 확인

git config user.name
git config user.email
# 특정 값 개별적으로 확인 가능

git config --system --unset credential.helper
# git config 초기화
 ```

- `--system`
	- `/etc/gitconfig`
	- 시스템의 모든 사용자와 모든 저장소에 적용 (관리자 권한)
- `--global`
	- `~/.gitconfig`
	- 현재 사용자에게 적용되는 설정
- `--local`
	- `.git/config`
	- 특정 저장소에만 적용되는 설정


### 3. 원격 관리 시작하기
- **git** → 분산버전관리시스템(DVCS)
- ***git*** 은 버전(커밋)을 관리한다. ↔ ***Github 도*** 버전(커밋)을 관리한다.

#### $ git push <원격저장소이름> <브랜치 이름>
- 원격저장소 만들고, ***로컬저장소의 커밋(변경사항)을 push(올림) 한다.***
  (로컬저장소에 원격 저장소 정보는 필수!)
- 로컬 폴더의 파일/폴더가 아닌 저장소의 버전(커밋)이 올라감

 👉 의도를 통해서, 수동으로 작업(조작)해야 한다. 

```bash
git remote add origin <repo_address>
# 원격 주소 등록

git remote add origin https://github.com/github_username/repository.git

git remote add origin https://github.com/hong/test.git
# 원격 주소 예시

git remote -v
# 원격저장소의 정보를 확인함

git push
# (로컬에서) 커밋한 내용을 원격 저장소로 push
```


##### 원격저장소 경로 설정
- 원격 저장소 정보를 로컬 저장소에 추가
- ==로컬 저장소에는 한번만 설정해주면 된다.==

![](assets/git-img-%20(3).png)
```shell
git remote add origin http://github.com/devkid/test.git
```
👉 **“깃아 원격저장소 추가해줘 오리진이라는 이름으로 url을”**
  ***⇒ 깃원츄오유***


- git push <원격저장소이름><브랜치이름>
	- 원격 저장소로 로컬저장소 변경사항(commit)을 올림(push)
	- 로컬 폴더의 파일/폴더가 아닌 **저장소의 버전(커밋)이 올라감**

- push 관련 인증 관련 
	- push 할 때는 인증 정보 필수
	- 윈도우는 팝업창에서 진행 
		- (윈도우도 '자격증명관리자'에서 토큰값으로 설정 가능)
	- 맥은 토큰 값을 받아 비밀번호 활용 **(Github 계정 비밀번호가 아님!)**
		- (키체인 접근)
	- push가 authentication failed 되는 경우 인증정보 확인 

##### push 실패시
- 로컬과 원격 저장소의 커밋 이력이 다른 경우 `push` 가 거부(`![rejected]`)되었다는 에러 메시지가 발생하는데, 이때 
1) 원격저장소의 커밋을 원격저장소로 가져와서(`pull`)
2) 로컬에서 두 커밋을 병합(`merge`) (추가 커밋 발생)
	- 동시에 같은 파일이 수정된 경우 **merge conflict** 발생
3) 다시 Github으로 `push`


#### $ git pull <원격저장소이름> <브랜치이름>
- 원격 저장소로부터 변경된 내역을 받아와서 이력을 병합함
```shell
git pull origin master

git pull
```


#### $ git clone <원격저장소 주소>
- 원격 저장소를 복제하여 모든 버전을 가져옴
```shell
git clone https://github.com/tensorflow/tensorflow.git
```

- clone 과 pull 의 차이?
	- clone : 원격저장소 복제
	- pull : 원격 저장소 커밋 가져오기


### 4. Git 사용시 주의 사항

#### git 사용시 항상 경로 확인 !
![|500](assets/git-img-%20(5).png)

- 특정 폴더에만 git 이 적용되고 있는지 확인 (***master 유무***)
- ***특정 폴더에만 master가 있어야함.*** 
	- 그렇지 않다면, ***너무 상위 폴더에서 "git init" 를 한 경우***
	- 이 경우, `cd .. ` 올라 가면서 `rm -rf .git` 로 지워주기.
- vs 코드 좌측 하단에서도 현재 브랜치 상태 확인 가능
	- ![](assets/git-img-%20(6).png)


#### commit에 관하여
- commit message는 각 파일, 폴더별 설정이라기 보다는 이번의 작업에 대한 전반적인 설명을 함축(요약)해야 한다. = **행위에 대한 기록**


#### 원격저장소 조작 금지
👉 수정사항이 생기면 로컬에서 작업하고, push 하는 것을 원칙으로!

#### 마크다운 이미지 경로 이슈
- 이미지가 저장된 폴더나 파일을 이동시키면
	👉 ***안 보임, 경로 재설정 필요***



### 5. 기타 
#### 5-1. `.gitkeep`
- why?
	👉 git 환경에서는 기본적으로 빈 폴더는 status 에 나타나지 않음
- so
1) 일반적으로 `.gitkeep` 이라고 하는 파일을 만든다
2)  `.gitkeep` 는 관용적으로 쓰이며, 다른 단어를 사용해도 상관 없음

#### 5-2 `.gitignore`
- 일반적인 개발 프로젝트에서 버전 관리를 별도로 하지 않는 파일/ 디렉토리가 발생한다.
- 이때, Git 저장소에(폴더 내)에 `.gitignore` 파일을 생성하고 해당 내용을 관리한다.

>[!caution]
📌주의! 
> 이미 커밋된 파일은 반드시 삭제를 하여야 `.gitignore`로 적용 된다!
> - 따라서, 프로젝트 시작전에 미리 설정해야한다!

```bash
## 특정 파일일 경우
a.txt 
test/a.txt 
#모든 a.txt 또는 test 폴더 내 a.txt


## 특정 디렉토리일 경우
/my_secret

### 특정 확장자를 가진 모든 파일 ( #wild card)
*.exe, *.csv
# = 모든 exe 파일, csv 파일 무시 (제외)

# 예외처리
!b.exe
```
- 📌각 프로젝트 마다 개별 설정해야함!

- `.gitignore`에 포함되는 파일 예시
	- 개발언어
		- 파이썬: `venv/` , JS: `node_modules/` 
	- 개발환경
		- OS (windows, mac, linux)
		- text editor / IDE (vs code 등)
- `.gitignore` 파일 작성 시 참고할 사이트 : [gitignore.io](https://www.toptal.com/developers/gitignore) 

#### 5-3. 저장소(repository) 관련 
##### 1) 저장소 이름 변경
- Settings > General > Repository name
- ==저장소 이름 변경 시 원격저장소 URL이 변경되어 로컬 설정 변경이 필수적이다.== ![](assets/git-img-%20(4).png)

##### 2) 저장소 접근 관리
- Settings > Collaborators
- ==저장소에 push 권한은 collaborator에만 있습니다.==
	- 메일을 통한 초대, 승낙 후 공동 작업 가능!

##### 3) 원격저장소 다운로드 방법
1. 📌repository 주소를 복사해서 `clone` ! 
		👉`clone` 하면 동일한 이름의 폴더 생성
1. github GUI 프로그램 이용
2. ZIP 파일로 다운 
 ![](assets/git-img-%20(7).png)

- Zip 버전 다운 vs `clone` 
	- 전자는 단순히 최신 버전의 파일/폴더를 가져옴 
	- ✔ <u>후자는 git 저장소를 복사하는 것 </u>
		👉 진정한 의미의 분산버전 관리라 할 수 있음!

  - 원격저장소의 활용
```bash
$ git pull 
# 변경된 커밋(업데이트) 받아옴

$ git clone
# 저장소를 복사해옴
```



#### 5-4. 그 외
1) **그래프로 분기(branch) 나타내기**
```bash
$ git log --oneline --graph
# 분기(branch)를 시각적으로 도식화 
```

2) **git 에서 에러 발생 하면**
	1.  `Q`를 사용해서 탈출
	2.  `ctrl` + `C` 를 사용해서 탈출
	3.  gitbash 창을 껐다 다시 킴

3) **bash 에서 `ctrl`+`L` 로 터미널 창 지울 수 있음**
   
4) **이전 버전 확인하기**
```shell
git checkout <해시값>
# 해당 버전 확인 가능
```

5) **러버덕 디버깅** 
	- 왜맞틀 = ''왜 맞았는데 틀렸대??'
	- ***어?? 하지말고 오리랑대화 ㅋㅋㅋ***

6) `git add .` 와 `git add *` 의 차이
	- 전자는 `.gitignore`에 명시된 목록들을 고려해서 파일을 추가하고, <u>후자는 이와 무관하게 전부 추가를 한다.</u>
	- 따라서, `git add .`을 주로 사용하자. 

8) **reflog 목록 확인**
	- reflog 브랜치와 HEAD가 지난 기간 동안에 가리켰었던 커밋
```shell
git reflog
또는
git log -g
```

9) ==파일 제목에 특수문자가 들어가면 오류가 발생할 수 있다!==
	- 백준 제목을 그대로 차용해 파일 이름으로 썼는데, 
	- 맥이랑 백준허브에서는 문제가 없다가, 윈도우 환경에서 pull 받을 때 계속 에러가 발생했다. (`BOJ_2902 KMP는 왜 KMP일까?`)
	- 되도록이면 **파일 제목에는 특수기호는 사용을 자제**하자. 
 

![](../../_others_/Git%20basic%20-%20rollback.md#^c92f46)

#### 5-5. stash 영역
- 참고  [commit 3단계의 이해](#commit%203단계의%20이해)
```shell
git stash // stash에 저장하기 

git stash save '설명 추가' //설명 추가하여 stash 저장하기 

git stash list //stash 목록보기

git stash apply
git stash apply stash@{number}
// 가장 최근의 stash 내용 혹은 지정된 stash가 적용되고, 적용 후에도 stash 리스트에 유지

git stash pop
git stash pop stash@{number}
// 가장 최근의 stash 내용 혹은 지정된 stash가 적용되고, 적용 후에 stash 리스트에서 삭제

git stash drop
git stash drop stash@{number}
// 가장 최근의 stash 내용 혹은 지정된 stash를 삭제

git stash clear
//stash의 모든 기록이 삭제
```


### 6. 참고
- [Git Manual Book (official)](https://git-scm.com/book/ko/v2)
- [github 요약 정리 자료(cheat sheet)](https://velog.io/@palza4dev/TIL-28.-GitGithub-%EC%BB%A4%EB%B0%8B-%EB%A9%94%EC%8B%9C%EC%A7%80-%EC%9E%91%EC%84%B1%EB%B2%95)

![](assets/Git_cheat_sheet.png)

[^git-stash]:  자세한 내용은 해당 문서 [5-5. stash 영역](#5-5.%20stash%20영역) 에서 다룬다.
