---
aliases:
  - 삼바
tags:
  - HomeServer
---
```dataview
list from #HomeServer
```

#### 1. 삼바 설치
```shell
sudo apt-get -y install samba # 우분투 삼바 설치
```

#### 2. 삼바 계정 등록하기
```shell
sudo smbpasswd -a [사용자명]

sudo pdbedit -L # 삼바 서버에 등록된 유저를 확인 
sudo pdbedit -L -v
```

| 옵션 | 설명                                                                                                          |
| :----: | ------------------------------------------------------------------------------------------------------------- |
| -a   | 삼바 사용자를 추가할 때 사용.<br>삼바 사용자는 리눅스 시스템에 존재하는 계정이어야 한다.                      |
| -x   | 삼바 사용자를 제거할 때 사용                                                                                  |
| -d   | 삼바 사용자를 일시적으로 비활성화할 때 사용                                                                   |
| -e   | 삼바 사용자를 활성화할 때 사용                                                                                |
| -n   | 패스워드 없이 로그인이 가능하도록 할 때 사용. <br>smb.conf에 'null passwords = yes'라고 추가로 설정해야 한다. |

```shell
smbpasswd -a inpa # → jhnyang를 삼바 사용자에 추가하면서 패스워드를 부여. jeff는 리눅스에 생성된 계정이어야 함.

smbpasswd inpa # → 삼바 패스워드를 변경

smbpasswd -x inpa # → 삼바 사용자를 제거

smbpasswd -d inpa # → 삼바 사용자를 비활성화
```

#### 3. 공유 디렉터리 생성
- 윈도우에서 리눅스로 접근할 수 있는, 즉 삼바로 공유될 디렉터리를 하나 생성해 준다.
```shell
mkdir /smbdir

chmod 777 /smbdir # 권한 열기
```

#### 4. 삼바 환경 설정
```shell
vi /etc/samba/smb.conf

```

```shell
[share] # [] 대괄호는 섹션을 정의, 윈도우에서 접근할 때 폴더 이름이 세션안의 문자열로 보인다. 보이고 싶은 이름을 적으면 된다.
comment = samba shared directory # 간단한 공유 폴더 설명
path = /smbdir # 공유 디렉토리 경로
read only = no # 읽기 전용
writable = yes # 쓰기 전용 
guest ok = no # 다른 사용자들도 이용할 수 있도록 설정
valid user = user1 # 공유 디렉토리를 이용할 수 있는 사용자를 설정
create mask = 0777 # 파일 허가권
directory mask = 0777 # 디렉토리 허가권
```

```shell
[share]
comment = samba shared directory
path = /smbdir
read only = no
writable = yes
guest ok = no
valid user = user1
create mask = 0777
directory mask = 0777
```

| 옵션                       | value               | 설명                |
|--------------------------|---------------------|-------------------|
| comment                  | (text)              | 공유 폴더에 대한 설명      |
| path                     | (text)              | 공유 폴더 경로          |
| read only                | yes/no              | 공유 폴더를 읽기 전용으로 설정 |
| writable, write ok       | yes/no              | 공유 폴더를 쓰기 가능으로 설정 |
| valid users              | (id, id, ...)       | 공유 폴더 접근 가능 유저 목록 |
| write list               | (id, id, ...)       | 공유 폴더 쓰기 가능 유저 목록 |
| public, guest ok         | yes/no              | 게스트 이용 가능 여부      |
| browsable                | yes/no              | 파일 목록을 보여줄 것인지 여부 |
| printable                | yes/no              | 프린터 스풀 파일 지정      |
| create mask, create mode | (0644 / 0777 / ...) | 생성 권한             |
| force group              | (group, group, ...) | 접근 가능 그룹 지정       |
| directory mask           | (0644 / 0777 / ...) | 공유 폴더 권한          |


```ad-note
[global]

workgroup = [작업 그룹명]
server string = [Windows Network에서 보여줄 Samba 서버에 대한 설명.]
wins support = [Samba서버에서 nmbd 데몬이 wins 서버의 역할을 할 수 있는지 여부를 지정 ( yes | no )]
wins server = [wins 서버의 IP를 지정하는 옵션]
dns proxy = [nmbd 데몬이 wins 서버 역할을 하고 등록되지 않은 Net BIOS 이름을 찾아줄 때 DNS 서버를 사용하여 NetBIOS 이름을 찾아줄 것인지의 여부 ( yes | no )].
interfaces = [바인딩할 특정 인터페이스/네트워크, 인터페이스 이름 또는 IP주소/넷마스크]
Samba 서버 서비스를 네트워크 인터페이스별 제공할 때 사용. 지정하지 않으면 모든 인터페이스. ( ex:  lo eth0 192.168.12.1/24 )
bind interfaces only = ['interfaces' 옵션을 사용 유무 ( yes | no )]
interfaces 옵션의 네트워크에 대해서 바인딩. Samba가 방화벽으로 보호되지 않거나 방화벽 자체인 경우 사용하도록 설정하는 것이 좋으나 동적, 비 브로드캐스트 인터페이스의 경우 정확하게 동작하지 않을 수 있음.
log file = [Samba 각 시스템에 대해 별도의 로그 파일을 사용]
max log size = [개별 로그 파일의 크기 제한(KB)]
syslog only = [syslog를 통해서 로그를 기록 유무 (yes | no)]
syslog = [syslog에 기록하는 로그 레벨]
syslog로 삼바 로그를 저장하기를 원한다면 다음 매개 변수를 높은 값으로 설정.
server role = [서버 모드]
"standalone server", "member server", "classic primary domain controller", "classic backup domain controller", "active directory domain controller". 대부분 "standalone sever"나 "member server"로 사용.  
"Active Directory 도메인 컨트롤러"로 실행하려면 데이터베이스를 지우고 새 도메인을 만들려면 먼저 "samba-tool 도메인 프로비저닝"을 실행해야 한다.
 
```


#### 5. 삼바 데몬 smbd 재시작 및 연결 상태 확인 
```shell
service smbd restart
```

```shell
smbstatus # 삼바 서버와 클라이언트의 연결상태 보기
```



#### 출처
- [🐧 삼바(SAMBA) 설치 & 설정 방법 [리눅스 ↔ 윈도우]](https://inpa.tistory.com/entry/LINUX-%F0%9F%93%9A-%EC%82%BC%EB%B0%94SAMBA-%EC%84%A4%EC%B9%98-%EC%84%A4%EC%A0%95-%E2%80%BB-%EC%B4%9D%EC%A0%95%EB%A6%AC)