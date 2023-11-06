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


#### Linux의 태스크 처리
- Linux는 여러 태스크(시스템이 수행하는 작업)를 동시에 진행 할 수 있는 **멀티 태스크**를 지원한다. 
- 이때, 하나하나의 태스크를 **프로세스**라고도 하며, Linux환경에서는 OS가 관리하는 단위로 프로세스가 사용되고 있다. 

##### 잡(jobs)
- 파이프로 명령어끼리 연결한 경우 등 하나 이상의 명령(프로세스) 모임을 **잡** 이라고 한다. 잡과 푸로세스는 각각의 고유한 번호를 가지고 있다. 

#### PS
- ps(Process Status) 명령은 현재 가동 중인 프로세스를 ID번호를 붙여 목록으로 표시한다. 
```shell
ps
```

![](assets/Linux%20note-12.png)

#### jobs 명령 
- jobs 명령은 현재 가동 중인 작업을 번호를 붙여 목록으로 표시한다. 

#### kill 명령어 
- 어떤 이유로든 종료하지 못하고 남아 있는 프로세스 또는 잡을 종료하려면 **kill** 명령을 사용한다. 
	- 일반 사용자는 자신이 실행한 프로세스만을 종료할 수 있다. 
```shell
kill 2444 # 프로세스 ID 또는 잡 번호
kill -9 프로세스 ID # 강제 종료시
```


#### 잡 중단과 재개 
- 실행 중인 잡을 일시 중단, 재개 할 수 있다. 중단하려면 `ctrl+z` 를 누른다,
- Vim에서 diary.txt 를 편집하는 도중에 `ctrl+z`를 누르면 잡이 중단되는데, 
- 이때 재개하여면 **fg**(fore ground) 명령으로 잡 번호를 지정하여 실행한다.
	- 잡 번호를 지정하지 않으면 가장 새로운 잡을 재개한다. 


#### 온라인 매뉴얼 참조
- man(MANual) + 명령어
- 해당 명령어의 매뉴얼이 출력된다(기본 less 옵션)
- space로 다음 페이지로 전환, q로 중도에 종료할 수 있다. 
```shell
man ls
```