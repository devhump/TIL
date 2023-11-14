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