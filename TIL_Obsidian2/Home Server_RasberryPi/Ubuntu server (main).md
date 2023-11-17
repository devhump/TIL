---
tags:
  - HomeServer
---

#### 관련 문서
##### RasberryPi
```dataview
list from #rasberrypi  
SORT file.cday DESC
```
##### HomeServer
```dataview
list from #HomeServer
```
##### Linux
```dataview
list from #Linux and !#Linux/Linux_note
SORT file.cday DESC
```
##### Linux note
```dataview
list from #Linux/Linux_note
SORT file.name ASC
```

#### at the begining
```shell
sudo apt update && sudo apt upgrade -y
sudo apt install zsh -y
```

#### 자주 쓰는 명령어
```shell
#프로그램 삭제
sudo apt-get --purge remove zsh

journalctl -f
sudo fail2ban-client status sshd
sudo systemctl status fail2ban

#파일/dir 모드 변경
chmod 777 /dev

# 부팅시 자동시작하게 하기
sudo systemctl enable program

# 방화벽 규칙 설정 (INPUT)
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# 방화벽 규칙 저장
sudo netfilter-persistent save 
sudo netfilter-persistent reload
```

##### 매뉴얼 확인
- [tldr](Linux%20최신%20명령어#tldr) 
```shell
man tar
tldr tar
tar --help
```
#### 최신 업데이트 정보 갱신 & 업데이트 실행
```shell
sudo apt update && sudo apt upgrade -y
```

#### 리부팅
```shell
sudo reboot
sudo reboot now
```

#### 서버 시스템 종료
```shell
sudo shutdown
sudo shutdown now
```

#### 네트워크 관련
- netstat (network statistics)
	- 네트워크의 상태를 모니터링하기 위한 도구
```shell
netstat [옵션] [| grep 포트 번호 or 서비스 명]
netstat -natp
netstat -tnlp
```

| 옵션 |             | 설명                                                                       |
| ---- | ----------- | -------------------------------------------------------------------------- |
| -l   | listen      | 연결 가능한 상태, 수신 소켓을 표시                                         |
| -n   | number port | 서비스 명 대신 포트 번호를 표시                                            |
| -t   | tcp         | 모든 TCP 연결을 표시                                                       |
| -p   | programs    | 프로그램 이름 / PID, <br>포트에서 수신하는 어플리케이션/데몬의 이름을 표시 |
| -a   | all         | 모두                                                                       |
| -u   | udp         | udp                                                                        |
| -i   | interfaces  | 이더넷 카드별 정상/에러/드랍 송수신 패킷 수 확인                           |
| -r   | route       | 라우팅 테이블                                                              |
| -s   | statistics  | 네트워크 통계                                                              |

#### GUI 설치
```shell
# 전체 설치
sudo apt install ubuntu-desktop

# 최소 설치
sudo apt install ubuntu-desktop-minimal

# 설치 후 실행
startx

# 부팅시 X window 자동 실행 되지 않게 함
sudo systemctl set-default multi-user

# 부팅시 X window가 자동 실행 되게 함
sudo systemctl set-default graphical
```


#### 서버 한국 시간으로 설정
```shell
# 현재 설정된 Time Zone 확인
timedatectl

# 한국 시간대로 변경
sudo timedatectl set-timezone Asia/Seoul
```

#### Ubuntu Locale 한글로 바꾸기
- [# Ubuntu Locale 한글로 바꾸기](https://beomi.github.io/2017/07/10/Ubuntu-Locale-to-ko_KR/)


#### 참고자료
- [# 🏠홈서버 만들기🏠 홈서버란](https://velog.io/@chch1213/build-home-server-1)

- WOL 설정 (wake on lan) 
	- [## 우분투 22.04 server WOL 설정 방법(Beelink s12 pro WOL)](https://engpro.tistory.com/m/434)

- SAMBA 설정
	- [# 🐧 삼바(SAMBA) 설치 & 설정 방법 [리눅스 ↔ 윈도우]](https://inpa.tistory.com/entry/LINUX-%F0%9F%93%9A-%EC%82%BC%EB%B0%94SAMBA-%EC%84%A4%EC%B9%98-%EC%84%A4%EC%A0%95-%E2%80%BB-%EC%B4%9D%EC%A0%95%EB%A6%AC)
	- [[SMB(Samba)]]
- [[Ubuntu 20.04] 우분투 서버에 Plex 미디어 스트리밍 서버 구축기](https://shanepark.tistory.com/391)

- [6. 우분투 토렌트 서버 구축하기 (transmission-daemon)](https://blog.djjproject.com/54)
- [Ubuntu 미디어 서버용 Jellyfin 서비스 구축하기(H/W 트랜스코딩)](https://blog.dalso.org/home-server/mediaserver-plex-jellyfin/8082)

