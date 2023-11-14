---
tags:
  - HomeServer
---
### apt lgn(ignore) 
- apt 업데이트시, 계속 로딩이 길어지면서, ign가 표시되고, 진행이 안 되는 상태
```shell
sudo vim /etc/resolv.conf
```

- 👇 아래내용 추가(변경)
```shell
nameserver 8.8.8.8 # google 네임서버
```

### 내부 IP 접속이 안 될 때
```ad-attention
- Remote side unexpectedly closed network connection
- Network error: Connection timed out
```

```shell
sudo vim /etc/hosts.allow
```

```vim
sshd : ALL
# 또는
ALL : 192.168.219.
```

