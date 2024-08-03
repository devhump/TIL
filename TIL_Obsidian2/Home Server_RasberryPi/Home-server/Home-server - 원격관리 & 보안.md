---
tags:
  - HomeServer
---
```dataview
list from #HomeServer
```
### tldr

```ad-note
- [SSH (Secure Shell)을 사용한 원격 관리](#SSH%20(Secure%20Shell)%EC%9D%84%20%EC%82%AC%EC%9A%A9%ED%95%9C%20%EC%9B%90%EA%B2%A9%20%EA%B4%80%EB%A6%AC)
	- [openssh-server 수동 설치](#openssh-server%20%EC%88%98%EB%8F%99%20%EC%84%A4%EC%B9%98)
	- [SSH 연결 프로그램](#SSH%20%EC%97%B0%EA%B2%B0%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%A8)
- [기본 보안](#%EA%B8%B0%EB%B3%B8%20%EB%B3%B4%EC%95%88)
	- [자주 업데이트 해줄 것](#%EC%9E%90%EC%A3%BC%20%EC%97%85%EB%8D%B0%EC%9D%B4%ED%8A%B8%20%ED%95%B4%EC%A4%84%20%EA%B2%83)
	- [root 계정](#root%20%EA%B3%84%EC%A0%95)
	- [SSH 계정 제한](#SSH%20%EA%B3%84%EC%A0%95%20%EC%A0%9C%ED%95%9C)
- [방화벽 - iptables](#%EB%B0%A9%ED%99%94%EB%B2%BD%20-%20iptables)
		- [초기화](#%EC%B4%88%EA%B8%B0%ED%99%94)
			- [iptables 옵션](#iptables%20%EC%98%B5%EC%85%98)
		- [기본설정](#%EA%B8%B0%EB%B3%B8%EC%84%A4%EC%A0%95)
			- [설정 확인](#%EC%84%A4%EC%A0%95%20%ED%99%95%EC%9D%B8)
		- [규칙제거](#%EA%B7%9C%EC%B9%99%EC%A0%9C%EA%B1%B0)
		- [저장](#%EC%A0%80%EC%9E%A5)
- [fail2ban - 침입차단](#fail2ban%20-%20%EC%B9%A8%EC%9E%85%EC%B0%A8%EB%8B%A8)
	- [필요성 파악](#%ED%95%84%EC%9A%94%EC%84%B1%20%ED%8C%8C%EC%95%85)
	- [설치](#%EC%84%A4%EC%B9%98)
	- [설정](#%EC%84%A4%EC%A0%95)
	- [적용 및 확인](#%EC%A0%81%EC%9A%A9%20%EB%B0%8F%20%ED%99%95%EC%9D%B8)
	- [차단 풀기](#%EC%B0%A8%EB%8B%A8%20%ED%92%80%EA%B8%B0)
	- [참고자료](#%EC%B0%B8%EA%B3%A0%EC%9E%90%EB%A3%8C)
```

### SSH (Secure Shell)을 사용한 원격 관리

#### openssh-server 수동 설치
- OS 설치 당시 미설치한 경우
```shell
sudo apt update
sudo apt install openssh-server -y
```

#### SSH 연결 프로그램
- 기본 terminal
```shell
ssh userID@xxx.xxx.xxx.xxx
```
- [putty](https://www.putty.org/)
- [MobaXterm](https://mobaxterm.mobatek.net/)


### 기본 보안
#### 자주 업데이트 해줄 것
```shell
sudo apt update && sudo apt upgrade -y
```

#### root 계정
- `su` (Switch user) : 계정 전환
- `sudo` (SuperUser Do) : 권한을 빌려 명령어를 실행
```shell
# 최초 1회 root 계정 비밀번호 생성
sudo passwd

# root 계정으로 로그인 
su
su - 

# 다른 계정으로 로그인
su [userName]

# 현 계정에서 로그아웃 
exit #또는 logout

# 현재 사용자 확인
whoami
```
- `su` 와 `su -`의 차이
	- `su`는 root 계정의 환경 변수를 가져오지 않고, 현재 계정의 환경 변수를 사용하게 되는 차이점이 있습니다.
	- `su -` 하시고 로그인을 하게 되면 기본 /root 디렉토리(directory)로 이동하게 됩니다. (환경 변수를 가져온다는 의미이겠지요.)

#### SSH 계정 제한
- 사용자 계정 외 다른 계정으로 SSH 접속을 하지 못하도록 설정해야 합니다.
- vim 으로 SSH 설정 파일을 열고 아래 내용을 추가하시면 됩니다.
```shell
sudo vim /etc/ssh/sshd_config
```

- 다음 내용 중 `[계정명]` 부분을 자신의 사용자 계정명으로 바꾸고 제일 아래 줄에 입력하세요.
```shell
AllowUsers [계정명]
AllowUsers ramy
```

- 설정 내용을 반영하기 위해 SSH 서비스를 재시작 합시다.
```shell
sudo service sshd restart
```


### 방화벽 - iptables
- 다음 명령어는 방화벽의 상태를 보여주는 명령어 입니다.
```shell
sudo iptables -L
```

| 구분    | 설명                                                                                                        |
| ------- | ----------------------------------------------------------------------------------------------------------- |
| INPUT   | 서버를 목적지로 하여 들어오는 모든 패킷은 이 체인을 거침                                                    |
| OUTPUT  | 서버에서 만들어진 모든 패킷은 이 체인을 거쳐서 다른 곳으로 가게 됨                                          |
| FORWARD | 이 체인은 INPUT 체인을 통해 들어온 패킷 중 목적지가 서버가 아닌 패킷이 거친 후 다른 곳으로 가게 되는 체인임 |

##### 초기화
```shell
sudo iptables -F
sudo iptables -X 
sudo iptables -P INPUT ACCEPT
sudo iptables -P FORWARD ACCEPT
sudo iptables -P OUTPUT ACCEPT
```

```shell
sudo iptables -F && sudo iptables -X  && sudo iptables -P INPUT ACCEPT && sudo iptables -P FORWARD ACCEPT && sudo iptables -P OUTPUT ACCEPT
```
###### iptables 옵션
| 옵션 | 설명                         |
| ---- | ---------------------------- |
| `-F` | 체인들의 모든 규칙을 삭제    |
| `-X` | 규칙이 없는 모든 체인 삭제   |
| `-P` | 해당 체인의 기본 정책을 설정 |

##### 기본설정
```ad-note
1. 로컬에서 로컬로(Loopback)의 모든 접속은 허용한다.
2. 22번 포트(SSH)로 들어오는 것을 허용한다.
3. 패키지 업데이트에 관한 패킷들을 허용한다.  
    새로운 연결 요청이지만, 기존의 연결과 관련된 패킷(RELATED)과 새로운 연결 요청에 관한 그후의 패킷(ESTABLISHED)을 허용하는 것인데 그냥 패키지 업데이트를 허용하는 것이라 생각하면 된다.
4. 위에서 허용하지 않는 모든 패킷은 DROP(폐기) 처리 한다.
5. 서버를 거쳐 다른곳으로 가는 모든 패킷도 DROP(폐기) 처리 한다.
```

```shell
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT 
sudo iptables -A INPUT -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT
sudo iptables -P INPUT DROP
sudo iptables -P FORWARD DROP
```

```shell
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT && sudo iptables -A INPUT -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT && sudo iptables -P INPUT DROP && sudo iptables -P FORWARD DROP
```

-  ufw 설치
```shell
sudo apt-get install ufw
```

- samba 포트 번호
```shell
sudo ufw allow 137,138/udp
sudo ufw allow 139,445/tcp

sudo iptables -A INPUT -p tcp --dport 139 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 445 -j ACCEPT

sudo iptables -A INPUT -p udp --dport 137 -j ACCEPT
sudo iptables -A INPUT -p udp --dport 445 -j ACCEPT
```

```shell
sudo ufw allow 137,138/udp && sudo ufw allow 139,445/tcp && sudo iptables -A INPUT -p tcp --dport 139 -j ACCEPT && sudo iptables -A INPUT -p tcp --dport 445 -j ACCEPT && sudo iptables -A INPUT -p udp --dport 137 -j ACCEPT && sudo iptables -A INPUT -p udp --dport 445 -j ACCEPT
```

- 실제 나의 시스템에서 쓰는 포트 확인
```shell
cat /etc/services
or
less /etc/services
or
more /etc/services
```

###### 설정 확인
```shell
sudo iptables -L
```

##### 규칙제거
```shell
sudo iptables -D INPUT [규칙 위치]
```

```ad-attention
- 하지만 여기서 끝이 아닙니다.
- 우분투 서버가 재부팅 되면 설정이 모두 사라지게 되므로 설정을 저장을 해야 하기에 방화벽 관리 패키지를 설치하여 저장하도록 합시다.
```

##### 저장
- 방화벽 관리 패키지 설치
```shell
sudo apt install iptables-persistent -y
```

- 방화벽 규칙 저장 및 적용
```shell
sudo netfilter-persistent save
sudo netfilter-persistent reload

sudo netfilter-persistent save && sudo netfilter-persistent reload
```


### fail2ban - 침입차단
- `fail2ban` 은 비밀번호를 무작위로 대입해서 로그인을 시도하는 해커들로부터 홈서버를 보호해줍니다.  
- 똑같은 IP로 n번 로그인 실패를 했을 경우 정해진 시간 접속이 불가능 하게 설정할 수 있습니다.

#### 필요성 파악
- 내 네트워크 상황을 실시간으로 보여줌 
```shell
journalctl -f
```

#### 설치
```shell
sudo apt install fail2ban -y

# 설치 이후에는 iptables에 새로운 체인이 생성됨
sudo iptables -L
sudo iptables -L INPUT
```

#### 설정
- fail2ban 에 대한 감옥파일 `jail.local` 파일을 만든 뒤 내용을 상황에 맞게 수정합시다.
```shell
sudo vim /etc/fail2ban/jail.local
```

```shell
[DEFAULT]
ignoreip=192.168.0.0/24
bantime=-1
# bantime=-1 은 영구차단
maxretry=3
findtime=86400

[sshd]
enabled = true
port=22
filter=sshd
logpath=/var/log/auth.log
```

```shell
[DEFAULT]
ignoreip=192.168.0.0/24
bantime=-1
maxretry=3
findtime=86400

[sshd]
enabled = true
port=22
filter=sshd
logpath=/var/log/auth.log
```

```ad-note
`[DEFAULT]` fail2ban에 지정할 모든 서비스에 대한 설정 입니다.  
`[sshd]` ssh 접속 서비스에 대한 설정 입니다.

- `ignoreip` 설정을 적용하지 않을 IP 리스트 입니다.  
    보통 내부에서의 접속들은 fail2ban을 적용하지 않습니다.  
    자신의 홈서버가 외부로 바로 연결되어 있거나 내부에서도 안전하지 않으신 분들은 이 옵션을 사용하지 마세요.
- `bantime` 이상 접속을 감지했을 때 접속을 불가능하게 할 `초 단위` 의 시간입니다.
- `maxretry` 허용해 줄 횟수 입니다.  
    로그인 가능 횟수라 보시면 됩니다.
- `findtime` 이상 접속의 횟수를 총괄 낼 `초 단위` 의 시간 입니다.
- `enable` 동작 여부를 나타냅니다.
- `port` 감지할 포트 입니다.
- `filter` 이상 동작이라고 판단할 문자열 입니다.  
    정규식(Regex)를 사용할 수 있습니다.
- `logpath` 필터링 할 전체 문자열 파일입니다.
```

- 요약👉 ==`fail2ban` 서비스는 `logpath` 에서 `filter` 항목을 찾아 `findtime` 시간 동안 `maxretry` 횟수 만큼 접속을 시도한 IP를 `bantime` 시간동안 차단합니다.==

#### 적용 및 확인
```shell
sudo service fail2ban restart

sudo fail2ban-client status sshd

sudo iptables -L
```

#### 차단 풀기
- 본인의 홈서버인데 비밀번호를 잘못 쳐서 fail2ban 이 차단해버린다면 당황할 것입니다.
- 아래 명령어로 차단을 풀 수 있습니다.
```shell
sudo fail2ban-client set sshd unbanip [외부ip]
```

#### 참고자료
- [# 🏠홈서버 만들기🏠 원격관리](https://velog.io/@chch1213/build-home-server-3)
- [# 🏠홈서버 만들기🏠 보안](https://velog.io/@chch1213/build-home-server-4)
- [# 기본적 서버 보안 프로그램, Fail2Ban 사용법 기초부터 실전 사용법까지 알아 보기](https://mytory.net/archives/13121)
