# Git 활용 심화편

---

작성 22.07.09 /

---

1. git 설정 파일 (config)
2. push
2. `.gitkeep` & `.gitignore`

- [github 요약 정리 자료(cheat sheet)](https://velog.io/@palza4dev/TIL-28.-GitGithub-%EC%BB%A4%EB%B0%8B-%EB%A9%94%EC%8B%9C%EC%A7%80-%EC%9E%91%EC%84%B1%EB%B2%95)

---



- git 명령어 정리 

  ```bash
  $ git init
  # 로컬 저장소 생성
  
  $git add <file_name>
  # 특정 파일/폴더의 변경사항 추가
  
  $ git commit -m "<commit message>"
  # 커밋 (버전 기록)
  
  $ git status
  # 상태 확인 
  
  $ git log 
  # 버전 확인
  ```

  

- git 에서 에러 발생 하면 

  1. `Q`를 사용해서 탈출

  2. `ctrl` + `C` 를 사용해서 탈출

  3. gitbash 창을 껐다 다시 킴

     

## 1. git 설정 파일 (config)

- 사용자 정보 (commit author) ◀ 커밋을 하기 위해서 반드시 필요

  ```bash
  $ git config --global user.name "username"
  $ git config --global user.email "my@email.com"
  # github 에서 설정한 username / email 로 설정
  # 이때 대소문자에 의해 오류가 날 수 있어, 
  # 편의를 위해 되도록 소문자만 사용하는 걸 권장
  ```

- 설정 확인 +

  ```bash
  $ git config -l
  # 전체 설정 확인
  
  $ git config --global -l
  # global (대외) 설정 확인
  
  $ git config user.name
  $ git config user.email
  # 특정 값 개별적으로 확인 가능
  
  $ git config --system --unset credential.helper
  # git config 초기화
  ```



- `.gitkeep`

  - why?

    ▶ git 환경에서는 기본적으로 빈 폴더는 status 에 나타나지 않음

  - so

    1. 일반적으로 `.gitkeep` 이라고 하는 파일을 만든다

    2. `.gitkeep` 는 관용적으로 쓰이며, 다른 단어를 사용해도 상관 없음

       

---

## 원격관리 시작하기

- **git** → 분산버전관리시스템(DVCS)
- ***git*** 은 버전(커밋)을 관리한다. ◀▶ ***Github 도*** 버전(커밋)을 관리한다.



## 2. `push` 

- 원격저장소 만들고, ***로컬저장소의 커밋을 push 한다.***

  (로컬저장소에 원격 저장소 정보는 필수!)

  ▶ 의도를 통해서, 수동으로 작업(조작)해야 한다. 

  ```bash
  $ git remote add origin <repo_address>
  # 원격 주소 등록
  
  $ git remote add origin https://github.com/github_user_name/repository.git
  $ git remote add origin https://github.com/hong/test.git
  # 원격 주소 예시
  
  $ git remote -v
  # 원격저장소의 정보를 확인함
  
  $ git push
  # (로컬에서) 커밋한 내용을 원격 저장소로 push
  
  ```

- **“깃아 원격저장소 추가해줘 오리진이라는 이름으로 url을”**

  ***⇒ 깃원츄오유***

  

- `git push <원격저장소이름><브랜치이름>`

  - 원격 저장소로 로컬저장소 변경사항(commit)을 올림(push)

  - 로컬 폴더의 파일/폴더가 아닌 저장소의 버전(커밋)이 올라감

    

- push 관련 인증 관련 
  - push 할 때는 인증 정보 필수
  - 맥은 토큰 값을 받아 비밀번호 활용
  - push가 authentication failed 되는 경우 인증정보 확인 



## 3. `.gitkeep` & `.gitignore`

### 3-1) `.gitkeep`

- why?

  ▶ git 환경에서는 기본적으로 빈 폴더는 status 에 나타나지 않음


- so

  1. 일반적으로 `.gitkeep` 이라고 하는 파일을 만든다

  2. `.gitkeep` 는 관용적으로 쓰이며, 다른 단어를 사용해도 상관 없음



### 3-2) `.gitignore`

- 일반적인 개발 프로젝트에서 버전 관리를 별도로 하지 않는 파일/ 디렉토리가 발생한다.

- 이때, Git 저장소에(폴더 내)에 `.gitignore` 파일을 생성하고 해당 내용을 관리한다.

- 이미 기 커밋된 파일은 **반드시** 삭제 후 `.gitignore` 에 등록해야함

- ```bash
  a.txt 
  test/a.txt 
  #모든 a.txt 또는 test 폴더 내 a.txt
  
  /my_secret
  #특정 디렉토리
  
  *.exe, *.csv
  # 특정 확장자를 가진 모든 파일 ( #wild card)
  # = 모든 exe 파일, csv 파일 무시 (제외)
  
  !b.exe
  # 예외처리
  ```

- 📌각 프로젝트 마다 개별 설정해야함!

- `.gitignore` 파일 작성 시 참고할 사이트 : [gitignore.io](https://www.toptal.com/developers/gitignore) 
