---
tags:
  - Linux/Linux_note
---

## table of contents
- [종료와 재시작](#%EC%A2%85%EB%A3%8C%EC%99%80%20%EC%9E%AC%EC%8B%9C%EC%9E%91)
- [사용자 환경 설정](#%EC%82%AC%EC%9A%A9%EC%9E%90%20%ED%99%98%EA%B2%BD%20%EC%84%A4%EC%A0%95)
- [경로설정](#%EA%B2%BD%EB%A1%9C%EC%84%A4%EC%A0%95)
- [Linux GUI 환경](#Linux%20GUI%20%ED%99%98%EA%B2%BD)
- [Wayland란](#Wayland%EB%9E%80)
- [통합 데스크톱 환경](#%ED%86%B5%ED%95%A9%20%EB%8D%B0%EC%8A%A4%ED%81%AC%ED%86%B1%20%ED%99%98%EA%B2%BD)
- [기본조작](#%EA%B8%B0%EB%B3%B8%EC%A1%B0%EC%9E%91)
- [고도의 조작](#%EA%B3%A0%EB%8F%84%EC%9D%98%20%EC%A1%B0%EC%9E%91)
- [SSH에 의한 원격 조작](#SSH%EC%97%90%20%EC%9D%98%ED%95%9C%20%EC%9B%90%EA%B2%A9%20%EC%A1%B0%EC%9E%91)
- [dnf](#dnf)
- [부록](#%EB%B6%80%EB%A1%9D)

### table of contents
- [관련 문서](#%EA%B4%80%EB%A0%A8%20%EB%AC%B8%EC%84%9C)
- [리다이렉트](#%EB%A6%AC%EB%8B%A4%EC%9D%B4%EB%A0%89%ED%8A%B8)
- [파이프란?](#%ED%8C%8C%EC%9D%B4%ED%94%84%EB%9E%80?)
- [메모리와 디스크 명령](#%EB%A9%94%EB%AA%A8%EB%A6%AC%EC%99%80%20%EB%94%94%EC%8A%A4%ED%81%AC%20%EB%AA%85%EB%A0%B9)
- [사용자 관련 명령](#%EC%82%AC%EC%9A%A9%EC%9E%90%20%EA%B4%80%EB%A0%A8%20%EB%AA%85%EB%A0%B9)
- [명령 이력 알아보기](#%EB%AA%85%EB%A0%B9%20%EC%9D%B4%EB%A0%A5%20%EC%95%8C%EC%95%84%EB%B3%B4%EA%B8%B0)
- [입력을 보완하는 기능](#%EC%9E%85%EB%A0%A5%EC%9D%84%20%EB%B3%B4%EC%99%84%ED%95%98%EB%8A%94%20%EA%B8%B0%EB%8A%A5)
- [일시설정](#%EC%9D%BC%EC%8B%9C%EC%84%A4%EC%A0%95)
- [사용자의 생성과 삭제](#%EC%82%AC%EC%9A%A9%EC%9E%90%EC%9D%98%20%EC%83%9D%EC%84%B1%EA%B3%BC%20%EC%82%AD%EC%A0%9C)


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



#### 리다이렉트
- 표준 입력, 표준 출력, 표준 오류 출력의 입출력 대상을 변경하는 것을 **리다이렉트**(또는 **리다이렉션**)라고 한다. 

##### 출력 대상 지정
```shell
명령 > sample1.txt # 출력 대상 경로
```
- 이때, `>`는 저장(덮어쓰기), `>>`는 추가저장을 의미한다. 
	- 오류 출력의 경우는 `2>` 또는 `2>>` 을 의미한다. 

##### 입력 대상의 지정
```shell 
명령 < sample2.txt # 입력 대상의 경로
```

##### 예시
```shell
sort < sample1.txt > sample2.txt
# 이때 sample1 → 정렬 대상이 되는 파일(입력)
# sample2 → 저장할 곳의 경로(출력)
```


#### 파이프란? 
- 명령에 의해 얻은 결과를 다른 명령에 넘겨주고 싶을 때 사용한다.
```shell
ls | more
```
- more : 출력 결과를 페이지 단위로 표시하는 명령
- 파이프는 명령이 세개 이상 있어도 연결할 수 있다.

```shell
ls / | grep sr
# 루트 디렉토리를 조사하는데, 이 때 문자열 'sr'이 포함된 결과를 찾아라 
```


#### 메모리와 디스크 명령
- free, df, du 명령은 디폴트로는 결과의 단위가 KB이다. 
- -h 옵션을 붙이면 읽기 쉬운 당위로 표시할 수 있다. 

##### 메모리 사용량 알아보기 
- free 명령을 사용해서 메모리 사용량을 알 수 있고, 스왑(교체) 파일(메모리가 사용하지 않는 부분을 일시적으로 디스크에 옮긴 파일)의 크기도 확인 할 수 있다. 
```shell
free
```

##### 디스크의 사용량 알아보기 
- df 명령을 사용하여 디렉터리와 파일 시스템의 관계와 사용량을 알 수 있다.
```shell
df
``` 

##### 파일 및 디렉터리의 크기 알아보기
- du 명령은 지정한 파일의 크기 및 디렉터리 사용량을 표시하는 명령어 이다.
```shell
du -a diary.txt
# -a → 파일 단위로 크리를 표시
```

- 파일명(또는 디렉터리명)을 지정하지 않은 경우는 커런트 디렉터리 아래의 모든 디렉터리를 조사하여 표시한다. 
```shell
du - a | less

```

![](assets/Linux%20note-6.png)
- 사용량(kb) 와 파일명이 표시된다.

#### 사용자 관련 명령
##### 사용자의 로그인 상황 확인하기
- w 명령은 현재 로그인 중인 사용자와 그 사람이 무엇을 하고 있는지 정보를 표시한다. 
```shell
w
```

- 비슷한 명령어로 who 가 있다. 이는 사용자명과 로그인 일시를 표시한다. 
```shell
who
```

##### 비밀번호 변경하기
- passwd 명령은 사용자 계정의 비밀번호에 관한 성정을 변경하는 명령이다. 
- 일반 사용자는 자신의 계정만 조작할 수 있다. 
```shell
passwd
```

- 관리자는 모든 사용자의 비밀번호를 리셋할 수 있다. 이 경우는 다음과 같이 사용자 계정을 지정한다.
	- 관리자는 특정 사용자 계정의 비활성화 또는 비밀번호 유효기간을 바꿀 수도 있다.
```shell
passwd mario # 비밀번호를 리셋하고 싶은 사용자 계정
```


#### 명령 이력 알아보기 
- history 명령을 사용하면 과거에 입력한 명령을 표시할 수 있다. 
```shell
history 5 # 표시 건수 (history 명령 포함)
```

![](assets/Linux%20note-7.png)

- 이때 '!' 와 이력번호를 이어서 입력하고 'enter' 키를 누르면 해당 번호에 대응하는 명령을 다시 실행 할 수 있다. 
	- 또는 간편하게 화살표(up/down)을 이용하여 최근  사용한 명령어 부터 다시 불러 올 수 있다. 

#### 입력을 보완하는 기능
- bash 에서는 명령 또는 경로 입력 도중에 `TAB` 키를 누르면 입력할 문자열의 나머지 문자를 보완해 준다.
	- 후보가 2개 이상일 경우 `TAB` 키를 두번 누르면 후보 목록이 표시된다.


#### 일시설정
##### 시스템 클락(system clock)
- OS가 내부에 가지고 있는 시계를 **시스템 클락**이라고 한다.
- 파일의 타임스탬프나 사용자의 이용 기록 등을 정확하게 관히하기 위해서라도 시스템 클락의 설정은 중요하다. 
	- 기본적으로는 컴퓨터 본체의 시계(RTC; Real Time Clock 또는 하드웨어 클락)을 기준으로 한다.

##### date 명령
- date 명령은 시스템 클락의 일시를 설정, 관리하는 명령이다. 현재의 일시를 확인하는 방법은 다음과 같다. 
```shell
date # 실행한 순간의 일시가 표시됨
```


##### NTP 서버를 사용한 시간 맞추기
- 네트워크에 연결되어 있는 Linux에서는 NTP(Network Time Protocol) 서버라고 하는 시간 맞춤용 서버를 이용하여 정기적으로 시간을 맞춘다. NTP 서버를 통해 시간을 맞추려면 ntpd라는 데모가 실행되고 있어야 한다. 
	- ntpd는 `/etc/ntp.conf`에 기술된 NTP 서버나 타이밍 정보를 바탕으로 시간을 맞춘다.

##### ntpdate 명령
- ntpdate 명령은 NTP 서버에 문의하여 시간을 동기화한다. 인수에는 다음과 같이 서버명을 지정해야 하며, ntpd가 실행 중인 경우는 사용할 수 없다.
```shell
ntpdate ntp.nict.kr # NTP 서버명
```



#### 사용자의 생성과 삭제 
- 사용자 계정의 생성과 삭제에 대해 알아본다. 
- 이는 모두 관리자에게만 허용된 작업이다. 

##### 사용자 계정 생성
- 먼저 **useradd** 명령을 사용하여 사용자명을 설정한다. 사용자명은 중복해서 설정할 수 없다. 같은 이름의 사용자가 있는 경우에는 이를 알려주는 메시지가 표시된다. **-m** 옵션을 붙여서 사용자용 홈 디렉터리도 함께 작성한다. 

- 그리고 비밀번호는 **passwd** 명령으로 설정한다. 비밀번호를 설정하지 않으면 보안상 문제가 될 뿐만 아니라, 설정에 따라서 비밀번호 없이 로그인할 수 없는 경우도 있다.
```shell
useradd -m testuser # 사용자명

passwd testuser
```

##### 사용자 계정 삭제
- 사용자 계정을 삭제하려면 **userdel** 명령을 사용한다. 
```shell
userdel -r testuser # 사용자명
# -r 옵션 → 계정과 그 홈 디렉터리를 삭제
# 옵션 없음 → 계정만 삭제
```


##### 다중 사용자 모드와 단일 사용자 모드
- Linux에는 여러 명의 사용자가 사용하는 **다중 사용자 모드**와 관리자 한 명만 로그인 할 수 있는 **단일 사용자 모드**가 있다. 단일 사용자 모드는 유지 관리 시 관리자가 안심하고 작업할 수 있도록 준비한 것이다. 


### 종료와 재시작
- 시스템을 종료하고나 재시작하는 방법이다. 
- 원칙적으로는 일반 사용자는 이들 작업을 수행할 수 없다. 

#### '종료한다'는 것
- '시스템을 안전하게 종료하고 전원을 끄는 것'을 **셧다운**(shutdown), '재시작 하는 것'을 **리부팅**(rebooting)이라고 한다. Linux는 항상 가동하는 서버로 사용되기 떄문에 이들 작업을 수행하는 것은 긴급 상황이 발생한 경우 뿐이다. 

#### shutdown 명령
- **shutdown** 명령은 종료나 재시작을 수행하는 명령으로, 실행하면 로그인 중인 모든 사용자에게 메시지가 통지되며, 사용하려면 관리자로 로그인 해야 한다. 
```shell
shutdown -h +5 Shutdown At 10:25 # 사용자에게 통지되는 메시지
# shutdown [옵션] [시간설정] [메시지]
# 옵션 -h는 종료, -r은 리부팅
# 시간설정은 now는 지금바로(종료만) +5는 5분 후를 뜻한다. 
```

#### halt 명령
- **halt** 명령도 시스템을 종료하는 명령이다. 
- 사용자에게는 통지나 시간 설정 권한이 없기 때문에, 가급적 shutdown 명령을 사용하도록 한다. 
- 환경에 따라 사용할 수 없는 경우도 있다. 
```shell
halt
```

#### reboot 명령
- **reboot** 명령은 시스템을 다시 시작하는 명령이다. 
- 사용자에게는 통지나 시간 설정 권한이 없기 때문에, 가급적 shutdown 명령을 사용하도록 한다. 
```shell
reboot
```

```ad-attention
- halt 명령과 reboot 명령은 환경에 따라서는 일반 사용자도 이용할 수 있지만, 여러 사용자가 공유하여 사용하는 경우에는 누가 어떤 작업을 하고 있는지 알 수 가 없다. '마음대로 종료해서는 안 된다' 라는 점을 명심하자.
```


### 사용자 환경 설정
#### 닷파일
- 닷 파일은 대부분 시스템 관리용 환경 설정 파일이다. 닷 파일이 `ls` 명령(옵션 없음)으로 표시되지 않는 것은 부주의하게 조작할 수 있는 위험을 방지하기 위해서다.

##### 닷 파일의 예
- 새로 작성한 홈 디렉터리에서 `ls -a`를 실행하면 닷 파일만 표시된다.
```shell
ls -a
```

#### 주요 환경 설정 파일
- 홈 디텍터리 내의 시스템 환경 설정 파일에는 다음과 같은 것이 있다. (bash의 경우)

| 파일명        | 내용                                                                       |
| ------------- | -------------------------------------------------------------------------- |
| .bash_history | bash로 실행한 명령의 이력                                                  |
| .bash_profile | 로그인시에 실행되는 환경 설정                                              |
| .bash_logout  | 로그아웃 시에 실행되는 환경 설정                                           |
| .bashrc       | .bash_profile로부터의 호출이나 쉘 시작 시에 실행되는 환경 설정             |
| .bash_login   | .bash_profile이 없는 경우에 사용되는 로그인 시의 환경 설정                 |
| .profile      | .bash_profile이나 .bash_login이 없는 경우에 사용되는 로그인 시의 환경 설정 |

- 그 외 vi(vim)의 기록 파일(.viminfo) 등 애플리케이션별로 환경 설정 파일이 저장되어 있는 경우도 있다. 

```python
# pseudocode

## 로그인의 경우
def 로그인:
	do .bash_profile
	if not .bash_profile:
		do .bash_login
		if not .bash_login:
			do profile
	do .bashrc

로그인()

################################

# 로그아웃의 경우
def 로그아웃:
	do .bash_logout

로그아웃()
```


### 경로설정
- 환경 설정의 예로 경로(PATH) 설정 방법에 대해 소개한다. 

#### 경로 지나가기 
- 자주 사용하는 명령이 있는 디렉터리 경로를 미리 설정해 두면 명령 이름을 입력만 해도 사용할 수 있다. 
- 이를 '경로를 지나간다' 라고 한다. 

#### 환경변수
- Linux에는 쉘과 명령에서 공통적으로 참조할 수 있는 내장 변수가 있는데, 이것을 **환경 변수**라고 한다. 
- 환경변수는 **env**(ENVironment) 명령으로 확인할 수 있다. 

##### PATH 지정
- 경로를 통하게 하기 위해서는 **PATH** 변수에 디렉터리 경로를 지정해야 한다. 
- .bash_profile 파일에서 'PATH=경로' 라고 지정해 두면 로그인할 떄 PATH 변수가 설정된다. 
- 여러 개의 경로를 설정하는 경우에는 ':'로 연결한다. 

```shell
# .bash_profile 파일
...
PATH=$PATH:$HOME/bin
# 새로운 PATH 변수는 기존의 것이 '홈디렉터리 경로/bin'을 추가한 것이 된다. 
# $PATH → PATH 변수: 이보다 전에 지정한 PATH정보를 나타낸다. 
# $HOME → 홈 디렉터리 경로를 나타낸다. 
```
- 이미 있는 환경변수를 참조할 때는 맨 앞에 `$`를 붙인다.

- .bash_profile 파일 변경을 활성화하려면 다시 로그인하거나 **source** 명령을 실행하여 닷 파일을 다시 읽어 들이도록 한다. 
```shell
source ~/.bash_profile
```

##### 쉘 변수
- 시스템 변수에는 쉡 스크립트 등에서 이용되는 쉘 변수도 있다. 
- 내용은 **set** 명령으로 확인할 수 있다. 
	- set 명령은 환경 변수와 쉘 변수를 나타낸다. 
- 쉘 변수와 환경 변수의 이름이 동일한 경우, 한쪽이 바뀌면 다른 한쪽에도 반영된다. 
	- PATH 변수도 그러한 예 중 하나이다. 


#### cron
- **cron**(Command Run ON)은 스크립트 파일을 자동으로 실행하는 시스템이다. 
- 이 시스템을 사용하면 정기적으로 실행하고 싶은 프로그램(명령어나 스크립트 파일 포함)을 정해진 타이밍에 자동으로 실행 할 수 있다. 
- cron은 설정파일인 `/etc/crontab`과 설정 내용에 따라 명령을 실행하는 `crond`라는 프로그램으로 구성된다. 
	- crond 맨 끝의 d는 daemon(데몬; 수호신)에서 따왔다. 


### Linux GUI 환경
- window나 mac과 같이 창(윈도우)를 이용해 파일이나 애플리케이션을 조작하는 GUI 관리 기능을 **window system**이라고 한다. 
- LInux에서는 X window system에서 발전한 **GNOME(놈), KDE, Xfce** 같은 **통합 데스크톱 환경**으로 발전해 왔다. 

### Wayland란
- **Wayland**는 Linux에서 GUI를 이용하기 위한 시스템 중 하나이다. 
- 쉘이 커널과 사용자 사이의 중개자 역할을 하고 있는데, Wayland 또한 커널과 사용자를 중개하는 역할을 하고 있다. 

- Wayland는 Wayland 컴포지터(compositor)와 Wayland 클라이언트(client)라는 두 개의 프로그램으로 구성되어 있다. 
- 사용자는 Wayland 클라이언트를 통해 Wayland 컴포지터 기능을 사용한다. 
	- 이 때, Wayland 클라이언트와 Wayland 컴포지터가 통신하는 방식을 **Wayland 프로토콜**이라고 한다. 

### 통합 데스크톱 환경
- 윈도 매니저에 데스크톱용 **유틸리티**(도구)를 모아 놓은 것을 **통합 데스크톱 환경**이라고 한다. 
- Linux에는 **GNOME과 KDE**라는 두 개의 유명한 통합 데스크톱 환경이 있다. 
	- GNOME (GNU Network Object Model Environment)은 가장 많이 사용되는 통합 데스크톱 환경이다. 
		- CentOS, Fedora, Ubuntu 등에서 채택되었다. 
		- GNU (GNU is Not UNIX) : UNIX 호환 시스템을 재배포하기 자유로운 형태로 공개, 구축하는 것을 목표로 하는 프로젝트 이다. 
	- KDE (K Desktop Environment)는 그래픽 그리기 방법으로 GNOME과는 다른 방법을 채택한 데스크톱 환경이다. 


### 기본조작
- 텍스트 모드에서 GNOME 시작과 종료를 실행한다. 

#### 텍스트 모드에서 시작 
```shell
systemctl enable gdm.service # GNOME을 시작
```


### 고도의 조작 
### SSH에 의한 원격 조작
- SSH(Secure SHell)는 네트워크로 연결된 다른 컴퓨터를 원격으로 조작하기 위한 프로그램이다. 통신이 암호화되므로 안전하게 통신할 수 있다. 

#### ssh 명령
- SSH를 사용해 처음 접속하려면 **ssh** 명령을 사용해야 한다. 
- 종료하는 경우는 exit라고 입력한다. 
```shell
ssh testman02@sample2.cyber.co.kr
# ssh 사용자명@호스트명
```
- 현재의 사용자명으로 로그인할 경우, 호스트명만 입력해도 된다. 


#### SFTP
- SFTP(SSH File Transfer Protocol)은 TCP/IP 네트워크로 연결된 다른 컴퓨터와 파일을 전송하기 위한 프로토콜이다. 

##### SFTP 접속
- SFTP 서버에 접속하려면 **sftp** 명령을 사용한다. 
- 종료하려면 quit을 입력한다. 
```shell
sftp user-name@sample2.cyber.co.kr
# sftp 사용자명@호스트명
```

- 다운로드에는 **get**명령, 업로드에는 **put** 명령을 이용한다. (FTP 명령어)


#### 애플리케이션의 설치
```shell
sample-1.0.1a-1.tar.gz
# 프로크램 또는 패키지명.버전.개정.확장자
```
- 해당 프로그램을 다운받은 뒤,  `tar xvzf 파일명`으로 실행한다.

- 배포형식이 바이너리 형식인 경우 컴파일 과정이 필요하다. 
```shell
./configure

make

make install
```

#### 패키지 관리 시스템이란
- 패키지 관리 시스템은 설치에 필요한 파일을 한데 모은 **패키지 파일**을 사용해 설치부터 삭제까지 관리한다. 
	- centOS → RPM 형식
	- Ubuntu → deb 형식
	- 그 외 → tgz 형식

##### RPM
- RPM(Redhat Package Manager)
```shell
# 설치 및 업그레이드
rpm -ivh sample-1.0.1a-1.rpm
# rpm -옵션 패키지의 파일명
# -ivh 신규설치
# 이때, vh는 진행 상황 등 상세 표시를 하는 옵션
# -Uvh 강제적으로 최신 버전으로 업그레이드(없는 것은 신규설치)
# -Fvh 설치 완료된 패키지만 갱신

## 삭제
rpm -e sample

## 설치 상태 확인
rpm -qa | grep sample
# qa 모든 설치가 완료된 패키지(a)를 리스트 업(q)
```


### dnf
- dnf(Dandified Yum)는 네트워크를 통한 RPM용 패키지 파일의 업데이트(갱신) 정보를 섬색하여 필요에 따라 업데이트 하는 시스템이다. 의존 관계가 있는 패키지도 찾아서 한꺼번에 설치한다. 

```shell
# 업데이트 정보 확인 
dnf check-update 

# 업데이트
dnf update sample02 sample03
# 파일명 지정하지 않으면 갱신 가능한 모든 패키지가 대상이 된다.

# 설치
dnf install sample03

# 삭제
dnf remove sample03
```

- Yum(Yellow dog updater, Modified)
	- dnf의 전신인 명령어로 yum이 있다. dnf는 yum과의 호환성을 유지하면서 안정성과 속도를 향상 시켰다. yum 명령 조작은 dnf와 거의 같다. 


#### 로그 관리
- 시스템의 로그 → 정상적으로 작동하고 있음을 나타내는 정보나 오류, 트러블 정보는 로그로 로그파일에 남겨진다. 

- Linux의 대표적인 로그 파일(CentOS 8 기준)

| 로그 파일         | 역할                      |
| ----------------- | ------------------------- |
| /var/log/boot.log | 커널 시작 시의 기록       |
| /var/log/cron     | cron의 처리와 관련된 기록 |
| /var/log/lastlog  | 마지막의 로그인 기록      |
| /var/log/messages | 시스템 전체의 기록        |
| /var/log/secure   | 인증과 관련된 기록        |
| /var/log/wtmp     | 로그인 기록               |

- logrotate는 점점 커지는 로그파일을 정기적으로 파일에 백업하기 위한 프로그램이다. 
	- 백업 시점이나 남겨둘 파일 수를 /etc/logrotate.conf 파일에서 설정할 수 있다. 


### 부록
#### GUI 활성 및 비활성 명령어

- GUI 활성 및 비활성 (centOS)
```shell
# GUI 비활성
sudo systemctl disable gdm

# GUI 재활성
sudo systemctl enable gdm
sudo reboot
```

- GUI 활성 및 비활성 (ubuntu)
```shell
# GUI 비활성
sudo systemctl set-default multi-user.target

# GUI 재활성
sudo systemctl set-default graphical.target
sudo reboot
```


#### 마운트
- 마운트란 HDD, CD-ROM 등의 드라이브를 이용하기 위한 장치이다. 
- LInux 시스템에서는 개별 드라이브라는 개념이 없고, 모두 루트 디렉터리에 접속(마운트)된 디렉터리로 취급한다.

```shell
mount -t iso9660 /dev/cdrom /mnt/cdrom

unmount /mnt/cdrom
```

#### 주요 파일 형식

| BMP        | .bmp       | 바이너리             | 일반적인 비트맵 이미지 파일이다.                                                                                                             |
| ---------- | ---------- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| CSV        | .csv       | 텍스트               | Comma-Seperated Valuese<br>,(콤마) 등의 구분된 문자로 파일을 구분하여 한 줄에 하나의 레코드를 나타내는 데이터 파일이다.                                                 |
| DAT        | .dat       | 텍스트               | 데이터 저장용 파일이다.                                                                                                                      |
| Document   | .doc       | 텍스트               | 문서 저장용 파일이다. MS word도 같은 확장자를 사용하고 있는데, 이것은 서식 데이터를 포함하는 바이너리 데이터로 되어 있다.                    |
| EPS        | .eps       | 텍스트 또는 바이너리 | PostScript에서 사용하는 이미지 파일이다.                                                                                                     |
| Gzip       | .gz        | 바이너리             | 비가역 압축 파일이다.                                                                                                                        |
| JSON       | .json      | 텍스트               | JavaScript Object Notation<br>사람이 읽고 쓰기가 용이하고, 컴퓨터도 이해하기 쉬운 데이터 형식이다.                                                                         |
| LOG        | .log       | 텍스트               | 로그를 저장하기 위한 파일이다.                                                                                                               |
| mp3        | .mp3       | 바이너리             | MPEG-1 Audio Layer-3<br>비가역 압축 사운드 파일이다.                                                                                                                 |
| mp4        | .mp4       | 바이너리             | MPEG-4 Part14<br>다양한 사운드 및 동영상을 기록하기 위한 파일이다.                                                                                            |
| MPEG       | .mpg/.mpeg | 바이너리             | 비가역 압축 동영상 파일이다.                                                                                                                 |
| PDF        | .pdf       | 바이너리             | Adobe Acrobat에서 사용하는 문서 파일이다.                                                                                                    |
| PNG        | .png       | 바이너리             | Portable Network Graphics<br>이미지 파일이다.                                                                                                                             |
| PostScript | .ps        | 텍스트 또는 바이너리 | PostScript에서 사용하는 문서 파일이다.                                                                                                       |
| svg        | .svg       | 텍스트               | Scalable Vector Graphics<br>벡터 형식의 이미지 파일이다.                                                                                                                 |
| S shell    | .sh        | 텍스트               | 쉘 스크립트 파일이다.                                                                                                                        |
| TAR        | .tar       | 바이너리             | TAR에서 사용하는 압축파일이다.<br>`tar svf sample.tar` 명령어로 압축해제 할 수 있다.<br>옵션으로 gzip기능을 쓰면, .tar.gz라는 확장자가 된다. |
| Z 형식     | .z         | 바이너리             | compress 명령에서 사용하는 압축파일이다.<br>`uncompress sample.z`로 압축해제 할 수 있다.                                                     |


#### 주요 디스트리뷰션

| 계열                    | 디스트리뷰션                                                     |
| ----------------------- | ---------------------------------------------------------------- |
| Red hat                 | RHEL(Red Hat Enterprise Linux), CentOS, Fedora, Scientific Linux |
| Debian                  | Ununtu, Debian GUN/Linux, Raspdian                               |
| 그 외                   | openSuSE                                                         |
| BSD (오픈 소스 Unix OS) | FreeBSD, NetBSD, OpenBSD, Darwin                                 |
| Linux에서 파생한 OS     | Android                                                          |


