---
tags:
  - Linux/Linux_note
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


### 네트워크 명령
#### 네트워크 어댑터 정보의 확인
- 네트워크 어댑터에 할당된 IP주소 등의 정보를 확인하려면 ifconfig 명령을 사용한다. 
```shell
ifconfig
```

- 단, 최근에는 ifconfig 대신 ip 명령을 사용하는 방법이 권장되고 있다. 같은 결과를 얻으려면 다음과 같이 기술해야 한다. 
```shell
ip addr
```

#### nslookup 명령
- nslookup 명령은 지정한 호스트명(DNS명 또는 IP주소)에 관한 정보를 DNS 서버에서 취득한다. 
```shell
nslookup www.cyber.co.kr
```

![](assets/Linux%20note-13.png)

### 네트워크 설정
- 네트워크를 설정하려면 관리자로 로그인해야 한다. 

#### 설정  파일의 소재
- 네트워크와 관련된 설정은 기본적으로 `/etc/sysconfig` 안에 있는 network라는 파일과 `/etc/sysconfig/network-scripts`안에 있는 설정 파일로 관리되고 있다. 

#### 네트워크 설정의 기본항목
- 네트워크 설정은 다방면에 걸쳐있지만, 여기서는 다음의 여섯 가지 항목에 대해 살펴본다. 
	- 호스트명
	- DNS 서버
	- IP 주소
	- 넷마스크
	- 게이트웨이 주소
	- DHCP의 유무

##### 호스트명의 설정
- 호스트명은 `/etc/hostname` 이라는 텍스트 파일에 기술되어 있다. 
	- centOS 6까지는 `/etc/sysconfig/network`에 저장되어 있다. 

```shell
localhost.localdomain # 완전 수식 도메인명(FQDN)
[호스트명].[도메인명]
```
