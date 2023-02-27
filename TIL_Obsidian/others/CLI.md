### CLI
- Command-Line Interface
- 명령어 인터페이스라고도 하며, 가상 터미널 또는 텍스트 터미널을 통해 사용자와 컴퓨터가 상호 작용하는 방식을 뜻한다. 
	- ex) git-bash, dos, cmd, terminal
		- ↔ GUi (Graphic User Interface)
- 작업 명령은 사용자가 툴바 키보드 등을 통해 문자열의 형태로 입력하며, 컴퓨터로부터의 출력 역시 문자열의 형태로 주어진다. 
- 이같은 인터페이스를 제공하는 프로그램을 명형 줄 해석기 또는 셸이라고 부른다.
	- 유닉스 셸(sh, ksh, csh, tcsh, bash 등)과 CP/, 도스의 command.com("명령 프롬프트") 등이 있다.

#### 명령어 기본 구조
- 특정 프로그램을 어떠한 인자와 함께 호출하도록 명령
```bash
	$ git push
	$ python test.py
	
	$ echo 'hello world'
	hello world
	
	$ which echo
	/usr/bin/echo
```

---

### 디렉토리 관련

-   `pwd`(print working directory): 현재 디렉토리(폴더 내지는 파일) 출력.
-   `cd` (change directory) : 디렉토리 이동
	- `cd .` : 현재 디렉토리
	- `cd . .` : 상위 디렉토리 이동, 띄어쓰기
-   `ls` (list) : 현 디렉토리 내 모든 파일 출력
	- `ls -a` : (list up all) 숨김파일/폴더도 전부 표시
	- `ls -l` : 파일 포맷 출력
	- `ls -la` 또는 `ls -al` 도 가능 (결과 둘다 동일)
-   `mkdir` (make directory) : 디렉토리 생성

---

### 파일관련
-   `touch <file_name>` : 파일 생성
-   `rm` (remove) : 삭제
	-   `rm file_name`
	-   `rm -r` (recursive) : 디렉토리(폴더) 삭제
	- `rm -r file_name`

---

### 기타
-   ==git bash 에서 복사/붙여넣기: `shift + insert`==
	- (`ctrl + c`, `ctrl + v` 아님!)
-   명령어 자동 완성 : `tap` 활용
-   터미널 창 클리어
	- `cls` : windows_cmd 환경
	- `ctrl +ㅣ` 또는 `clear` 도 가능