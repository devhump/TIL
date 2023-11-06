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


### 그룹 관리 
#### 그룹에서의 관리
- 사용자를 미리 그룹에 소속시켜 놓으면 권한 설정에 따라 그룹에 소속되어 있는 사용자에게 같은 권한을 부여한다. 
- Linux 에서는 사용자 계정 작성 시 사용자 명과 동명의 새로운 그룹이 만들어지며, 거기에 할당된다. 

#### 기본 그룹
- 사용자가 소속된 그룹 중 메인 소속처가 되는 그룹을 기본 그룸(Primary group)이라고 한다. 
	- 기본 그룹 외의 속한 그룹을 하위 그룹(서브 그룹)이라 한다. 

##### 소유 사용자와 소유 그룹
- 파일 및 디렉터리에는 소유 사용자와 소유 그룹이 기록된다. 
- vi 등에서 파일을 새로 만들면 그것을 만든 사용자가 소유 사용자가 되고, 사용자의 기본 그룹이 소유 그룹이 된다. 

##### 소유 사용자와 소유 그룹의 변경
- 소유 사용자는 **chown**(CHange OWNer) 명령으로 소유 그룹은 **chgrp**(CHange GRouP) 명령으로 변경할 수 있다. 
```shell
chown test sample1.txt # 관리자만 이용 가능한 명령어
chgrp hoegye sample1.txt # 관리자와 소유자만 이용 가능
```


#### 그룹 작성
- 새 그룹을 만들거나 삭제하는 방법으로, 관리자만 수행 가능하다. 

##### 그룹 작성
- 그룹 작성 시에 **groupadd**명령을 사용한다.
```shell
groupadd hoegye # 그룹명
```

##### 사용자 등록
- 사용자를 그룹에 등록하여면 **usermod** (USER MODify) 명령을 사용한다. 
- 로그인 중인 사용자의 기본 그룹을 변경하는 경우 변경을 활성화 하려면 다시 로그인 해야 한다. 
```shell
usermod -G hoegye beginner
# usermod [옵션] [그룹명] [사용자명]
```

- 옵션은 `-g` 기본 그룹으로 등록, `-G` 하위 그룹으로 등록, `-aG` 하위 그룹으로 추가 등이 있다.
- 하위 그룹을 기본 그룹으로 만들려면 **newgrp** 명령을 사용한다.
	- 일반 사용자는 본인에 대한 것만 변경 가능
```shell
newgrp hoegye beginner
# newgrp [기본 그룹으로 하고 싶은 그룹명] [사용자명]
```

##### 그룹 삭제
- 그룹을 삭제하려면 **groupdel**명령을 사용한다. 기본 그룹으로 설정한 사용자가 있으면 삭제할 수 없다. 
```shell
groupdel beginner # 그룹명
```

##### 그룹확인 
- 사용자가 어느 그룹에 소속되어 있는지를 확인하는 방법은 여러가지가 있다. 
- 자신의 기본 그룹이나 그 외 소속되어 있는 그룹을 알려면 **id** 명령을 사용하면 된다. 
```shell
id
```

![](assets/Linux%20note-14.png)

- **groups** 명령을 사용하면 자신이 소속된 그룹의 목록만 표시할 수 있다.
```shell
$ groups
>>> 그룹명1, 그룹명2 # 이때, 맨 앞이 기본 그룹
```