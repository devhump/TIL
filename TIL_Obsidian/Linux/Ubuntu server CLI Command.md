---
tags:
  - Linux
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


#### 최신 업데이트 정보 갱신 & 업데이트 실행
```shell
sudo apt update && sudo apt upgrade -y
```

#### 리부팅
```shell
sudo reboot
```

#### 서버 시스템 종료
```shell
sudo shutdown
```


#### 네트워크 관련
```shell
netstat -natp
```


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