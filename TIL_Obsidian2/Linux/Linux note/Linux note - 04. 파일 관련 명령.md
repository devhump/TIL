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



### 파일 관련 명령
##### 텍스트 출력 페이징
- more 명령과 less 명령은 화면(페이지)을 기준으로 출력 결과를 표시(페이징) 한다. 
- 출력 행이 많은 경우 장동으로 스크롤되는 것을 방지할 수 있으며, 이런 명령을 **페이저**라고 한다.

###### more 명령

```plain
# pet.txt 내용
...
kkoma
alex
ran
sham
...
```

```shell
more pet.txt # 파일명

>>>

...
kkoma
alex
ran
sham
--More--
```

- 출력 결과가 화면에 다 표시되지 않은 경우, 1페이지분이 표시된 후 `--More--`이 표시되고, 내부 명령어는 입력 대기 상태가 된다. 이때 사용 가능한 명령어는 아래와 같다.  
	- 스페이스 → 다음 페이지를 표시
	- enter → 1행씩 스크롤
	- h → 도움말
	- q → 종료

###### less 명령
- 내부 명령이 more 보다 강화되어 있어 간단한 검색이나 점프 이동이 가능하다. 
- 끝까지 표시되어도 자동으로 종료되지 않으므로 'q'를 입력하여 종료한다.
```shell
less pet.txt # 파일명

>>>
...
kkoma
alex
ran
sham
...
```
- 이때, 사용 가능한 내부 명령은 다음과 같다. 

###### 내부 명령

| 명령어          | 기능                             |
| :--------------: | -------------------------------- |
| 스페이스 또는 z | 다음 페이지를 표시               |
| w               | 이전 페이지를 표시               |
| Enter           | 1행씩 스크롤                     |
| < 또는 q        | 맨 앞으로 점프                   |
| > 또는 G        | 맨 끝으로 점프                   |
| / 문자열        | 문자열을 앞으로 검색(/로 재검색) |
| ? 문자열        | 문자열을 뒤로 검색 (?로 재검색)  |
| h               | 도움말                           |
| q               | 종료                             |

- 예시
	- 표시 결과가 많을 경우에 less 명령을 파이프 하면 좋다. 
	- `ls -1 /var/log | less`


#### alias 작성하기
- 자주 사용하는 명령의 경우 몇 번이나 같은 인수나 옵션을 입력하는 것은 번거로운 일이다. 
- 이럴 때, alias 명령을 사용하여 옵션이나 인수를 포함한 명령 기술 내용 자체에 대해 별명(alias)을 설정할 수 있다. 

```shell
alias la='ls -a'
# alias 별명='명령문'
# 별명(alias)에는 기존의 명령 이름은 사용할 수 없다.
```

##### alias 목록 표시하기
- 인수나 옵션을 붙이지 않고, alias 명령을 실행하면 현재 이영 가능한 에일리어스를 표시할 수 있다. 
```shell
alias
```

![](assets/Linux%20note-1.png)

##### alias 삭제하기
```shell
unalias la # 별명(alias)
```


#### 링크 작성하기
- ln 명령어(Link) 명령은 파일이나 디렉터리에 대한 **링크(링크 파일)** 을 만든다.
- 링크에는 **심볼릭 링크와 하드 링크** 두 종류가 있다.
```shell
# ln [옵션명] [링크의 참조대상] [링크명]
ln -s /home/beginner/sample1.txt sample
```

- 이때 옵션(-s)이 붙으면 심볼릭 링크, 없으면 하드링크이다.
```shell
ln -s /home/beginner/sample1.txt sample # 심볼릭 링크
ln /home/beginner/sample1.txt sample # 하드 링크
```

##### 심볼릭 링크와 하드 링크
- 심볼릭 링크 → 파일로의 참조
	- 링크를 삭제해도 원래의 파일에는 영향이 없다
	- 본체를 삭제하면 링크가 끊어진다.
- 하드링크 → 파일 실체로의 참조
	- 보통의 파일은 실체와 이름이 1:1 관계이다.
	- 하드링크를 만들면 하나의 파일을 두 개의 이름으로 참조할 수 있다. 

#### 명령 종류 알아보기 
```shell 
type ps
```

- 내부 명령인 경우
![](assets/Linux%20note-2.png)

- 외부 명령인 경우
![](assets/Linux%20note-3.png)

- alias인 경우
![](assets/Linux%20note-4.png)

#### 파일의 타임스탬프 확인/ 변경하기
- 파일에는 갱신 일시나 접속일시가 기록되어 있는데, 이것들을 **stat** 명령으로 알 수 있다. 
![](assets/Linux%20note-5.png)

- touch 명령을 사용하면 파일의 타임스탬프를 변경할 수 있다. 
```shell
touch -md "2023-05-18 12:00:00" abc.txt # vkdlfaud
# m 으로 변경 일시, a로 접속일 시를 변경한다.
# 둘다 지정하지 않으면 양쪽 모두 수정한다. 

# d로 일시를 지정한다. 
# 지정하지 않으면 현재 일시가 된다.
```

- 파일명만 지정해서 실행아면 크기가 0인 빈 파일이 만들어 진다. 
```shell
touch test.py
touch .gitignore
```
