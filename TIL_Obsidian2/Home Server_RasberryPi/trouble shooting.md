### apt lgn(ignore)
- apt 업데이트시, 계속 로딩이 길어지면서, ign가 표시되고, 진행이 안 되는 상태
```shell
vim /etc/resolv.conf
```

- 👇 아래내용 추가(변경)
```shell
nameserver 8.8.8.8 # google 네임서버
```