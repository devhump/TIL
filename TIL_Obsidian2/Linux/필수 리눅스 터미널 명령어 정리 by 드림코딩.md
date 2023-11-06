---
tags : [Linux]
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



- [유튜브- 필수 리눅스 터미널 명령어 정리 by 드림코딩](https://youtu.be/EL6AQl-e3AQ)

### 목차
```ad-note
- [[#다양한 쉘의 종류들|다양한 쉘의 종류들]]
- [[#Manual|Manual]]
	- [[#Manual#man|man]]
	- [[#Manual#clear|clear]]
	- [[#Manual#pwd|pwd]]
	- [[#Manual#ls|ls]]
- [[#Navigating file system|Navigating file system]]
	- [[#Navigating file system#cd|cd]]
	- [[#Navigating file system#find|find]]
	- [[#Navigating file system#which|which]]
- [[#Create and manage files|Create and manage files]]
	- [[#Create and manage files#파일 생성|파일 생성]]
		- [[#파일 생성#touch|touch]]
		- [[#파일 생성#cat|cat]]
		- [[#파일 생성#echo|echo]]
	- [[#Create and manage files#디렉터리 생성|디렉터리 생성]]
		- [[#디렉터리 생성#mkdir|mkdir]]
	- [[#Create and manage files#파일 관리|파일 관리]]
		- [[#파일 관리#cp / mv / rm|cp / mv / rm]]
		- [[#파일 관리#grep|grep]]
- [[#환경 변수 설정하기|환경 변수 설정하기]]
```


### 다양한 쉘의 종류들

| Unix | Windows |
 | :----: | :------: |
| - Bourne Shell<br>- Bash<br>- fish<br>- zsh     |- cmd.exe<br>- PowerShell |

- 윈도우즈에서 리눅스를 사용하려면?
	- Cygwin 설치
		- https://www.cygwin.com/
	- WSL(Windows Subsystem for Linux)
		- [Linux용 Windows 하위 시스템 설명서](https://learn.microsoft.com/ko-kr/windows/wsl/)

### Manual
#### man
- manual 확인
```shell
man man

man ls
```

- PowerShell
```powershell
GET-help 
# mand의 Alias
# 파워쉘에서는 
```
#### clear
- 프롬프트 화면 정리
```
clear
```

#### pwd
-  PWD (Print Working Directory)
- 현재 작업중 인 디텍터리 츨력
```
pwd

# PowerShell
# Get-location 도 가능
```

#### ls
- ls (LiSt)
```shell
ls
ls dir1 # 디렉터리 내부 리스트 출력
ls -l # long, 파일에 대한 상세한 내용 출력
ls -a # all, 숨김파일도 출력
ls - la # long & all 옵션 동시 사용 가능

#PowerShell
ls # 상세 내용 출력
ls -name # 파일명만 간단 출력
ls dir1 # 디렉터리 내부 리스트 출력
ls -force # 숨김파일도 출력
```

```shell
open . 
# 현재 디렉터리에서 파일 탐색기 열기

explorer .
# (windows) 현재 디렉터리에서 파일 탐색기 열기
```


### Navigating file system
#### cd
- cd (Change Directory)
```shell
. # 현재 경로
.. # 상위 경로 

cd .
cd ..
cd ~ # 홈 폴더로 이동
cd - # 이전 경로로 이동

#PowerShell
# Set-location의 Alias
cd .
cd ..
cd ~ # 홈 폴더로 이동
cd - # 이전 경로로 이동
```


#### find
```shell
find . -type file -name "*.txt"
# 현재 및 하위 디렉터리의 모든 텍스트 파일을 찾아라

find . -type file -name "*.json"
# 현재 및 하위 디렉터리의 모든 json 파일을 찾아라

find . -type directory -name "*2"
# 현재 및 하위 디렉터리 중 '2'로 끝나는 디렉터리를 찾아라
```

- Powershell의 경우
```powershell
Get-ChildItem -File -Filter "*.txt" -Recurse
# Recurse 옵션은 하위 디렉터리 재귀적 확인을 위한 옵
# Alias 없음
```


#### which
- 특정 프로그램의 실행 경로 출력
```shell
which node
# node 실행경로 출력
which code
# vs code 실행경로 출력
```

- Powershell의 경우
```powershell
get-command cmd.exe
gcm notepadd
```

### Create and manage files
#### 파일 생성
##### touch
- 동일한 이름의 파일이 없을 경우 파일 생성
- 동일한 이름의 파일이 없을 경우 파일 수정 날짜 업데이트

##### cat
- 파일 내용 출력

##### echo
- 동일한 내용 프롬프트에 표시
- 신규 파일에 문자열 입력/저장

```shell
touch new_file.txt
cat new_file1.txt new_file2.txt # concatenate and print file

echo "hello world"
>>> hello world

echo "Hello world" > new_file3.txt
cat new_file3.txt 
>>> Hello world
# new_file3 만들고 Hello world 입력 후 저장

echo "Hello world2" > new_file3.txt
cat new_file3.txt 
>>> Hello world2 
# 새로운 내용이 덮어씌워짐

echo "Hello world3" >> new_file3.txt
cat new_file3.txt 
>>> Hello world2 
Hello world3
# 기존 내용에 추가가 
```

- Powershell의 경우
```powershell
new-item new_file1.txt
# touch Alias 없음

# cat과 echo 는 unix와 동일 
```


#### 디렉터리 생성
##### mkdir
- mkdir (MaKe DIRectory)
```shell
mkdir dir3

mkdir -p dir4/sudir1/subdir2 
# p 옵션을 통해 신규 하위 디렉터리 한번에 생성 가능
```


#### 파일 관리
##### cp / mv / rm
- cp (CoPy)
- mv (MoVe)
- rm (ReMove)
```shell
cp file1.txt dir1/
# 특정 파일을 특정 디렉터리로 복사
mv file2.txt dir/
# 특정 파일을 특정 디렉터리로 이동
rm file2.txt
# 특정 파일 삭제
rm -r dir2
# 특정 디렉터리 삭제
```

- Powershell의 경우
```powershell
Copy-Item
# cp alias

rm dir2/
# 옵션 메시지 출력 

re dir2/ -recurse
# 옵션 출력 없이 바로 삭
```

##### grep
- grep (Global regular expression print)
```shell
grep "world" *.txt
# 모든 txt 파일에서 world를 찾아라

grep -n "world" *.txt 
# 몇번째 행에서 찾았는지 같이 출력

grep -ni "world" *.txt 
# 대소문자 구분없이(insensitive) + 몇번째 행에서 찾았는지 같이 출력

grep -nir  "world" .
# 현재 폴더와 하위 디렉터리에 한해 모든(recursive) world를 찾아라
```

- Powershell의 경우
```powershell
# alias 없음

select-string *.txt -pattern "world"
select-string *, */* -pattern "world"
# recursive 옵션이 없어 찾고자 하는 범위의 모든 경로를 나열해야 한다. 

select-string *, */* -pattern "world" -CaseSensitive
# 기본적으로 대소문자 구별이 없기 때문에, 구별하고자 할 경우 CaseSensitive 옵션 사용 
```


### 환경 변수 설정하기
- 환경변수?
	- 내 컴퓨터에서 특정한 키워드가 어떤 동작이나, 경로를 저장하도록 하는 것

```shell
export MY_DIR="dir1"
# 대문자 사용 + 띄어쓰기는 underbar(_) 사
env
# 모든 환경 변수 출력

cd $MY_DIR
# dir1 디렉터리로 이동
unset MY_DIR
# 환경 변수 삭제
```

- Powershell의 경우
```powershell
$env:MY_DIR = "dir1"
ls env:
# 모든 환경 변수 출력

set Path

cd $env:MY_DIR
# dir1 디렉터리로 이동

$env:MY_DIR = ""
# 환경 변수 삭제
```

