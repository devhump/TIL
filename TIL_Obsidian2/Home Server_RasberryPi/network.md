---
tags:
  - Linux
  - HomeServer
---
```shell
sudo apt install net-tools

sudo netstat -plnut

sudo lsof -i -n -P | grep LISTEN

# 리눅스에서 열려있는 특정 포트 번호만 확인하는법
netstat -tnlp | grep 포트번호

```

#### 네트워크 경로 추적
```shell
tracert google.com
```

#### 임시 http 서버 띄우기
```shell
python3 -m http.server 8888
```