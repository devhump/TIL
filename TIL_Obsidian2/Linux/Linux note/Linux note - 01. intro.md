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



#### 여러 가지 쉘

| 이름            | 쉘                                                                                                                                                                                             |
| :---------------: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| sh <br>(에스에이치) | 가장 기본적인 명령어 처리 능력을 가지고 있는 쉘로, b쉘 이라고 부른다.<br>동작은 빠르지만, 기능 면에서는 다른 쉘에 비해 빈약하기 때문에 주로 쉘 스크립트의 실행 환경 등에 사용되는 경우가 많다. |
| bash <br>(배쉬)     | b쉘을 확장한 쉘로, 현재는 이것을 b쉘이라 부르는 경우도 있다.<br>Linux에서는 표준 쉘로 채택되어 있으며, 가장 널리 알려진 쉘이라 할 수 있다.                                                     |
| ksh <br>(k쉘)       | b쉘을 확장한 쉘로, AT&T사가 개발했으며, 상용 UNIX로 사용되고 있다.                                                                                                                             |
| csh <br>(c쉘)       | 주로 BSD계열에서 채택되고 있는 쉘로, c쉘이라고 부른다. <br>C언어적 명령어 구문을 가지고 있는 것이 특징이다.                                                                                    |
| tcsh <br>(tc쉘)     | c쉘을 확장한 쉘로 현재의 BSD 계열 OS에서는 표준 쉘이다.<br> bash와 함께 많이 사용하는 쉘이다.                                                                                                  |
| zsh <br>(z쉘)       | b쉘을 확장한 쉘이지만, tcsh 기능도 갖고 있다. <br>b쉘 계열과 c쉘의 두 기능을 모두 사용할 수 있지만, 대신 동작이 느린 단점이 있다.                                                                  |

![|600](assets/linux_dir.jpg)
#### 주요 디렉터리

| 디렉터리 | 역할                                                                                          |
| :--------: | --------------------------------------------------------------------------------------------- |
| bin      | 바이너리 형식의 실행 파일이나 명령이 보관되어 있다.                                           |
| dev      | 디바이스 관련 파일이 보관되어 있다.                                                           |
| etc      | 각종 설정 파일 등 다양한 파일이 보관되어 있다.                                                |
| root     | 루트 디렉터리와는 별도로 준비된 시스템 관리자용인 홈 디렉터리이다.                            |
| sbin     | 관리자용 시스템 표준 명령이 보관되어 있다.                                                    |
| usr      | 각 사용자의 데이터나 애플리케이션이 보관되어 있는 장소이다.                                   |
| home     | 이 디렉터리 아래에 사용자별 디렉터리가 만들어지고, <br>거기가 각 사용자의 홈 디렉터리가 된다. |
| var      | 애플리케이션의 기록(로그) 파일이나 메일 데이터 등이 보관되어 있는 장소이다.                   |

#### 파일 시스템의 종류
- Linux에서 사용되는 주요 파일 시스템에 대해 알아본다.

| 파일 시스템 | 특징                                                                                                                                                            |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ext4        | Linux의 표준 파일 시스템으로 채택된 ext(EXTended file system)의 후속이다.<br>현재도 많은 Linux 디스트리뷰션의 디폴트 파일 시스템으로 되어 있다.                 |
| JFS         | IBM이 개발한 파일 시스템이 기반이며, Linux에서는 커널 2.6이 표준으로 채택되었다.<br>기존의 파일 시스템에 비해 신뢰성이 높으며 접속 속도가 빠르다는 특징이 있다. |
| XFS         | SGI사가 개발한 파일 시스템을 이식한 것으로, 병렬 입출력 조작이 뛰어나다.                                                                                        |

- 가상 파일 시스템 
	- 파일이 많은 경우 하드 디스크나 SSD에 저장되지만, 메모리 일부를 파일 시스템으로 사용한 것을 **가상 파일 시스템**이라고 한다. 가상 파일 시스템의 예로는 tmpfs나 devtmpfs와 같은 것들이 있다. 

##### 파일의 압축과 풀기 in Linux
- Linux에서는 크기를 작게 압축하여, 여러 개의 파일로 정리하는 것을 아카이브라고 하여 구별한다. 
- 이때, **아카이브**된 파일을 원래대로 되돌리는 것을 **해제**라고 한다. 
- 그러나, windows에서는 푸는 것을 해제라고 부르고 있어 용어가 혼용되는 경우가 있다. 

- window에서는 ZIP이라는 압축형식이 유명하지만, Linux의 경우는 종류가 많고, 표준 압축 방식에 대해서는 이에 대응한 명령이 준비되어 있다. 

| 주요 명령어   | 기능                                                 |
| :------------: | :--------------------------------------------------: |
| gzip / gunzip | 압축 / 해제                                          |
| zip / unzip   | 압축 / 해제                                          |
| tar           | 아카이브, 생성, 압축, 해제<br>(하나의 명령으로 대응) |

- tar 압축 파일의 경우, 아카이브만 하면 확장자가 `.tar` 인 파일이 만들어지고, 옵션을 사용한 압축까지 한 경우 `.tar.gz`와 같이 두 개의 확장자가 나란히 있는 파일이 만들어진다.

#### 절대경로와 상대경로 
##### 절대경로
- **루트 디렉터리**를 기점으로 지정하는 방법이다. 이 표시 방법은 **커런트 디렉터리**(현재 표시하고 있는 디렉터리)가 어디에 있든 상관없이 확실하게 목적한 파일을 지정할 수 있다. 
	- `/` (root dir)
		- `/`는 경로의 맨 처음이나 단독으로 사용하는 경우 **루트 디렉터리**를 나타낸다. 
```shell
/home/beginner/sample.txt
```

##### 상대경로 
- 커런트 디렉터리를 기점으로 지정하는 방법이다. 아래 그림에서 커런트 디렉터리를 beginner 디렉터리로 했을 경우를 살펴보자.
	- `./..`
		- `'..'`은 하나 위의 디렉터리(부모 디렉터리)를 나타낸다.
	- `.`
		- `'.'`는 커런트 디렉터리를 나타낸다. 
		- 커런트 디렉터리의 상대경로 `'./'`는 생략할 수 있다. 
```shell
# 현재 beginner 라는 폴더에 위치하고, 내부에 sample.txt 라는 파일이 있다.
./sample.txt 
또는 
sample.txt

# home 폴더 아래에 picture과 beginner 라는 이름의 폴더가 있다. 
# 커런트 폴더 -> beginner
./.. => home 폴더
./../picture
```

- 홈 디렉터리를 표시할 때 `'~'` (tilde)로 나타내기도 한다.