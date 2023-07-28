---
title : 
aliases : 
tags : [syntax, IT_SC_basic]
---

## CLI (Command Line Interface)

#### 목차
```ad-note
- [[#CLI|CLI]]
	- [[#CLI#명령어 기본 구조|명령어 기본 구조]]
- [[#디렉토리 관련|디렉토리 관련]]
- [[#파일관련|파일관련]]
- [[#기타|기타]]
- [[#windows cmd 환경|windows cmd 환경]]
```


### CLI
- **Command-Line Interface**
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


### 디렉토리 관련

-   `pwd`(print working directory): 현재 디렉토리(폴더 내지는 파일) 출력.
-   `cd` (change directory) : 디렉토리 이동
	- 디렉토리 이름 쓰면서 `tab`을 치면 자동완성이 가능 하다.
	- `cd` : <u>단독으로 쓰면  home 폴더로 이동 가능 하다</u>
	- `cd .` : 현재 디렉토리
	- `cd ..` : 상위 디렉토리 이동, 띄어쓰기

-   `ls` (list) : 현 디렉토리 내 모든 파일 출력
	- `ls -a` : (list up all) 숨김파일/폴더도 전부 표시
		- 숨겨진 파일은 이름 앞에 `.` 존재한다.
	- `ls -l` : 파일 포맷 출력 
		- 리스트 유형으로
	- `ls -la` 또는 `ls -al` 도 가능 (결과 둘다 동일)
-   `mkdir` (make directory) : 디렉토리 생성


### 파일관련
-   `touch <file_name>` : 파일 생성
-   `rm` (remove) : 삭제
	-   `rm file_name`
	-   `rm -r` (recursive) : 디렉토리(폴더) 삭제
	- `rm -r file_name`


### 기타
-   ==git bash 에서 복사/붙여넣기: `shift + insert`==
	- (`ctrl + c`, `ctrl + v` 아님!)
-   명령어 자동 완성 : `tap` 활용
-   터미널 창 클리어
	- `cls` : windows_cmd 환경
	- `ctrl +ㅣ` 또는 `clear` 도 가능

### windows cmd 환경
| 명령어        | 기능                                                                           |
| :-------------: | ------------------------------------------------------------------------------ |
| `DIR`         | `ls`와 동일한 기능을 한다.                                                     |
| `TREE`        | 해당 폴더 하위 폴더 까지의 모든 디렉토리가 <br> 트리 그래프 형식으로 나타난다. |
| `CLS`         | 화면을 지웁니다.                                                               |
| `DEL`           | 하나 이상의 파일을 지웁니다.                                                   |
| `HELP`          | Windows 명령에 대한 도움말 정보를 제공합니다.                                  |
| `HELP` + `명령어` | 해당 명령어에 대한 더 자세한 설명을 제공합니다                                 |
| `REPLACE`     | 파일을 바꿉니다.                                                               |
| `RMDIR`         | 디렉터리를 제거합니다.                                                         |
| `RENAME`       | 파일 이름을 바꿉니다. (`REN` 과 동일)                                          |
| `PATH`          | 실행 파일의 찾기 경로를 표시하거나 설정합니다.                                 |
| `MOVE`         | 하나 이상의 파일을 한 디렉터리에서 다른 디렉터리로 이동합니다.                 |
