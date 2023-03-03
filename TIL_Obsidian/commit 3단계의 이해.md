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
4. Stash [^git-stash]
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