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


### 기본 명령어
#### 디렉터리의 이동과 파일 표시 관련
##### cd
- cd(Change Directory): 디렉터리 이동 
```shell
cd dir_name
# 이때 절대경로, 상대경로 무관

cd 
# 단독으로 쓰이면, 홈 디렉터리로 이동
```

##### pwd
- pwd(Print work Directory): 커런트 디렉터리의 절대 경로를 표시

##### ls
- ls(List directory): 디렉터리 정보를 조사
```shell
# /beginner/data/ 밑에 a, b 폴더와 sample1.txt, sample2.txt 가 있을 때
ls data
>>> a b sample1.txt sample2.txt

# 디렉터리명 또는 파일명을 생략하면 커런트 디렉터리에 대한 내용을 표시
ls 

ls -1 # 상세정보가 나타난다.
ls -a # 숨김파일 (.dot 파일)도 전부 나타낸다. 

```


#### 파일 및 디렉터리 작성/삭제 관련
##### touch
- 파일 생성
```shell
touch test1
touch sample.txt
```
##### mv
- mv(MoVe file): 파일명을 변경하거나 파일을 이동할 때 사용
```shell
# 1. 파일명 변경
# mv [원래이름] [변경후이름]
mv sample1.txt sample

# 2. 파일 이동
# mv [이동하고자하는 파일명] [이동할 디렉터리 경로]
mv sample data
```
- 📌파일명과 같은 이름의 디렉터리가 있는 경우 경로를 올바르게 입력하지 않으면 '파일명 변경' 대신 '파일 이동'이 실행될 수 있으니 주의!

##### cp
- cp(CoPy file): 파일을 복사할 때 사용하는 명령
```shell
# cp [복사하고자 하는 파일명] [복사할 디렉터리 경로]
cp sample3.txt data
```

##### mkdir
- mkdir(MaKe DIRectory): 새로운 디렉터리 생성
```shell
mkdir temp
```

##### rmdir 
- rmdir(ReMove DIRectory): 빈 디렉터리 삭제 명령
```shell
rmdir temp
```

##### rm
- rm(ReMove file): 파일이나 디렉터리 삭제 명령
```shell
rm sample3.txt

# 파일이나 디렉터리가 들어있는 디렉터리(내용 포함)를 삭제하는 옵션
rm -r temp
```

#### 파일 조작 관련
##### cat
- cat(conCATenate): 파일의 내용 열람
```plain
# sample1.txt

I love Linux
```

```shell
$ cat sample1.txt
>>> I love Linux
```

- 파일명을 지정하지 않으면 키보드 입력 대기 상태가 되어 키보드로 입력한 내용을 반복적으로 표시한다. 
```shell
$ cat
>>> test
test
>>> test2
test2
>>>
```
- 입력 대기 해제시에는 `ctrl + c`를 사용한다. 

##### sort
- sort 명려은 지정한 텍스트 파일 내용을 정렬하여 표시한다. 
- 옵션이 없으면 오름차순(알파벳), `-r`을 붙이면 역순(내림차순)으로 정렬한다.

```plain
# cat.txt
kkoma
alex
ran
sham
```

```shell
$ sort cat.txt
alex
kkoma
ran
sham
```

- 이때, 파일명을 지정하지 않으면 키보드 입력 대기 상태가 되고, `ctrl + D` 를 누르면 입력한 내용을 정렬하여 표시한다. (bash의 경우)
	- **쉘에 따라서 로그아웃하는 경우도 있으니 주의!**

```shell
$ sort
>>> dog 
>>> mouse
>>> bird
# 여기서 ctrl + D 를 누르면
bird
dog
mouse
```

##### grep
- grep (Global Regular Expression Print) : 여러 파일 중에서 문자열을 검색하는 명령

```plain
# linenumber1
sinseol-dong
dongdaemun
jongro 5-ga
jongro 3-ga
jonggak
```

```shell
# grep [검색할 문자열(정규표현)] [파일명(경로)]
$ grep jongno linenumber1
>>> jongno 5-ga
>>> jongno 3-ga
```
- 지정한 문자열을 포함한 모든 행이 표시된다.

#### 파일 및 명령을 검색하는 명령관련
##### find
- 파일을 검색하기 위한 명령. 닷 파일도 검색이 가능하다.
- 커런트 디렉터리 이하 모든 폴더와 파일에 대해 검색을 한다.
```shell
find namelist # 파일명 또는 임의의 문자열

# find [검색 시작 디렉터리] [파일명 또는 임의의 문자열]
find data namelsit
```

##### which
- 지정된 명형의 본체를 검색하여 그 절대경로를 표시한다. 
```shell
# which [명령이름]
which ls
>>> /bin/ls # ls 명령의 절대경로가 표시된다.
```

##### whereis
- 명령 경로 뿐만 아니라, 매뉴얼이나 소스코드 파일 등의 경로도 동시에 조사하여 표시한다. 
```shell 
# whereis [명령이름]
whereis ls
```


#### 와일드 카드
##### *
- `find a*` 에서, `'a*'`은 **첫 글자가 a이면 그 후의 문자는 무엇이든 괜찮다**라는 의미
- 임의의 0개 이상의 문자열을 나타냄
##### ?
- 한 개의 문자열
- `find a?` 라는 명령은 **a로 시작하는 두 문자의 문자열을 검색하라**는 의미

- 와일드 카드는 문자열의 전후, 혹은 사이에 껴있어도 가능하다.
	- `*sample`, `pict?data` 등

- 주요 와일드 카드

| 기호           | 기능                              | 표기 예               | 의미                                               |
| :--------------: | :--------------------------------: | :---------------------: | :-------------------------------------------------- |
| [ ]             | [] 안의 임의의 1문자              | `[dog]` <br>`[a-z]`   | d,o,g라는 세개의 문자<br>a부터 z까지의 모든 알파벳 |
| `[^]`<br>`[!]` | []안의 문자열 이외의 임의의 1문자 | `[^dog]` <br>`[!dog]` | d, o, g 이외의 문자                                |
| {}             | {} 안에 지정된 각각의 문자열      | {dog, rat}            | dog, rat 이라는 두개의 문자열                      |
