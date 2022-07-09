# Git 활용 심화편

---

작성 22.07.09 /

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

  

### git 설정 파일 (config)

- 사용자 정보 (commit author) ◀ 커밋을 하기 위해서 반드시 필요

  ```bash
  $ git config --global user.name "username"
  $ git config --global user.email "my@email.com"
  # github 에서 설정한 username / email 로 설정
  # 이때 대소문자에 의해 오류가 날 수 있어, 
  # 편의를 위해 되도록 소문자만 사용하는 걸 권장
  ```

- 설정 확인 

  ```bash
  $ git config -l
  # 전체 설정 확인
  
  $ git config --global -l
  # global (대외) 설정 확인
  
  $ git config user.name
  $ git config user.email
  # 특정 값 개별적으로 확인 가능
  ```



- `.gitkeep`

  - why?

    ▶ git 환경에서는 기본적으로 빈 폴더는 status 에 나타나지 않음

  - so

    1. 일반적으로 `.gitkeep` 이라고 하는 파일을 만든다

    2. `.gitkeep` 는 관용적으로 쓰이며, 다른 단어를 사용해도 상관 없음

       

- git 에서 에러 발생 하면 
  1. `Q`를 사용해서 탈출
  2. `ctrl` + `C` 를 사용해서 탈출
  3. gitbash 창을 껐다 다시 킴

---

## 원격관리 시작하기

- **git** → 분산버전관리시스템(DVCS)
- ***git*** 은 버전(커밋)을 관리한다. ◀▶ ***Github 도*** 버전(커밋)을 관리한다.
- 