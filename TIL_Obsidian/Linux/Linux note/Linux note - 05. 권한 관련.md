---
tags:
  - Linux/Linux_note
---

#### 관련 문서
```dataview
list from #Linux and !#Linux/Linux_note
SORT file.cday DESC
```

##### Linux note
```dataview
list from #Linux/Linux_note
SORT file.name ASC
```


### 권한
- 권한이란 파일이나 디렉터리에 때해 사용자나 그룹이 가지는 권리를 말한다. 
- **보호 모드, 허가속성, 액세스 권한**이라고 한다. 
- 세가지 속성
	- 권한에는 읽기, 쓰기, 실행(디렉터리의 이동이나 검색 등도 포함)의 세 가지 속성이 있다. 
- 세가지 사용자 범주
	- User : 파일 소유자(일반적으로는 작성자)
	- Group : User와 같은 그룹의 사용자
	- Other : 그 외의 다른 사용자 

### 권한의 확인
- `ls -1` 또는 `ls -l`
![](assets/Linux%20note-8.png)

![](assets/Linux%20note-9.png)

| 파일 종류 | 의미                   |
| --------- | ---------------------- |
| -         | 일반 파일              |
| d         | 디렉터리               |
| l         | 심볼릭 링크            |
| c         | 캐릭터형 디바이스 파일 |
| b         | 블록형 디바이스 파일   |

- 디바이스 파일?
	- 주변기기에 접속하기 위한 파일이며, 데이터를 다루는 방법에 따라 두 종류로 나뉜다.

| 권한 | 의미                  |
| ---- | --------------------- |
| r    | 읽기 가능 (Readable)  |
| w    | 쓰기 가능 (Writable)  |
| x    | 실행가능 (eXecutable) |
| -    | 불가능 (각 항목 공통) |


#### 권한의 설정
- 모든 파일과 디렉터리에는 초기 상태로 권한이 설정되어 있다. 
- chmod 명령을 사용하면 사용자가 독자적으로 권한을 변경할 수 있다.
```shell
chmod o+w sample.txt
```
![|500](assets/Linux%20note-10.png)

#### 수치를 사용한 권한 설정

| 권한              | 수치 |
| ----------------- | ---- |
| r (읽기 허가)     | 4    |
| w (쓰기 허가)     | 2    |
| x (실행 허가)     | 1    |
| - (허가하지 않음) | 0    |

![](assets/Linux%20note-11.png)

#### 쉘 스크립트
- 쉘에 대한 명령(명령어)를 미리 텍스트 파일에 저장한 것이다.
- 여러 명령을 조합한 일련의 조작을 모아서 실행할 수 있다. 

##### 권한 설정
- 쉘 스크립트 자체로는 명령어들이 모여진 텍스트 파일일 뿐이며, 이를 쉘 스크립트로 기능하기 위해서는 실행 권한을 부여해야 한다. 

```shell
chmod u+x test.sh
```

- 쉘 스크립트 예시
```shell
#! /bin/sh
ls /home
# Ask your name
echo Input your name:
read name
echo "Hello $name"
```