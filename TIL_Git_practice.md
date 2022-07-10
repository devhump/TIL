- ![image-20220710155230812](../1)

- git 사용시 항상 경로 확인 !
- 특정 폴더에만 git 이 적용되고 있는지 확인 (master 유무)

![image-20220710155407996](../2)

- vs 코드 좌측 하단에서도 현재 브랜치 상태 확인 가능
- commit message는 각 파일, 폴더별 설정이라기 보다는 이번의 작업에 대한 전반적인 설명을 함축(요약)해야 한다.  = **행위에 대한 기록**

- bash 에서 `ctrl`+`L` 로 터미널 창 지울 수 있음

- 이전 버전 확인하기

```bash
git checkout <해쉬값>
#해당 버전 확인 가능
```

- 원격저장소 조작 금지 ▶ 수정사항이 생기면 로컬에서 작업하고, push 하는 것을 원칙으로!
- **러버덕 디버깅** 
  - 왜맞틀 = ''왜 맞았는데 틀렸대??'
  - ▶어?? 하지말고 오리랑대화 ㅋㅋㅋ
- 마크다운 이미지 경로 이슈
  - 이미지가 저장된 폴더나 파일을 이동시키면 ▶ ***안 보임, 경로 재설정 필요***



- 원격저장소 다운로드 방법

  1. 📌repository 주소를 복사해서 `clone` ! ▶ `clone` 하면 동일한 이름의 폴더 생성

  2. github GUI 프로그램 이용
  3. ZIP 파일로 다운 

  ![image-20220710160209444](../3)

  

  - Zip 버전 다운 vs `clone` 

    - 전자는 단순히 최신 버전의 파일/폴더를 가져옴 
    - ✔후자는 git 저장소를 복사하는 것 ▶ 진정한 의미의 분산버전 관리라 할 수 있음!

  - 원격저장소의 활용

    ```bash
    $ git pull 
    # 변경된 커밋(업데이트) 받아옴
    
    $ git clone
    # 저장소를 복사해옴
    ```

- 지금까지 배운 git 명령어 정리

  ```bash
  
  # 로컬 (local)
  $ git init
  $ git add .
  $ git commit -m 'commit_message'
  $ git status
  $ git log
  
  # 원격 (repository)
  $ git push origin master
  $ git pull origin master
  $ git remote add origin <repo_address>
  $ git clone <repo_address>
  
  ```

