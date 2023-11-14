---
tags:
  - HomeServer
---

### 관련 패키지 설치
```shell
sudo apt-get install net-tools ethtool wakeonlan
```

### 네트워크 카드 이름 확인
```shell
ifconfig
```

![[WOL on Ubuntu.png]]

```shell
# wol 수동으로 켜기
sudo ethtool -s 인터페이스명 wol g

# wol 작동상태 확인
sudo ethtool 인터페이스명
# sudo ethtool enp2s
```

- 👉 Wake-on 항목이 'g'로 설정되어 있으면 정상적으로 작동된 것이다.

### 부팅시마다 켜주도록 설정
- 방금 ethtool로 설정했던 사항은 리부팅을 하면 초기화가 된다.<br>부팅할 때마다 해당 설정을 켜주도록 네트워크 인터페이스 설정 파일을 수정해주어야 한다.

```shell
sudo vim /etc/network/interfaces
```

```vim
post-up /sbin/ethtool -s 인터페이스명 wol g
post-down /sbin/ethtool -s 인터페이스명 wol g
```

(우분투 18.04 부터 /etc/network/interfaces 를 수정하는 것이 적용되지 않는다는 정보가 있어 netplan을 추가 설정해주도록 한다.)

```shell
sudo nano /etc/netplan/...yaml
```

![[WOL on Ubuntu-2.png]]

```shell
sudo netplan apply
```
