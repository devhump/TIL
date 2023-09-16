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


### 한국어 환경
- UNIX가 **EUC** (한국어의 경우 **EUC-KR**)을 표준으로 한데 비해, Windows는 **CP949**를 표준으로 삼아 왔다. 
- 최근에는 다국어를 나타낼 수 있는 **UTF-8**이라는 문자 코드가 표준으로 사용되고 있다. 
- 지역 설정의 한 예로는 로케일(locale)이 있는데, 한국어를 나타내는 LANG 변수 값은 **ko_KR.UTF-8**이다.

#### 문자코드 
- 한국어를 이용할 수 있는 주요 코드에는 **EUR_KR, CP949**가 있다. 이 문자 코드가 정확하게 전당되어야 문자/기호가 바르게 표시된다.
- 최근에는 Unicode의 일종인 **UTF-8**이 표준으로 사용된다. 

| 한국어 대응 문자 코드 | 특징                                                                                                                                                             |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| EUR_KR                   | windows나 osX 이전의 Mac에서 표준으로 채택 되었다.                                                                                                               |
| CP949                    | windows의 기본 코드 페이지로, EUR-KR의 확장형이다.                                                                                                               |
| EUR-KR                   | UNIX를 중심으로 인터넷에서 자주 사용된다. <br>EUR(Extended UNIX Code)라는 이름에서 알 수 있듯이,<br> UNIX로 영어 이외의 언어를 표현하는데 사용된다.                  |
| UTF-8                    | Unicode의 일종으로, ASCII 코드와 호환이 된다.                                                                                                                    |
| UTF-16                   | Unicode의 일종으로, ASCII 코드와 호환이 되지 않는다.<br>BE(Big Endian)와 LE(Little Endian)의 두 종료가 있다.<br>Windows에서 Unicode인 경우 UFF_16 LE를 가르킨다. |


#### 로케일
- 언어나 통화 등을 포함한 지역 정보를 **로케일**이라고 한다. 로케일은 쉘이나 애플리케이션의 표시 및 동작에 영향을 준다. 

##### 현재의 로케일 확인
- **locale** 명령을 사용하면 현재 로케일의 설정을 확인할 수 있다.
```shell
$ locale
# LANG 변수 → 환경변수의 일종이다
LANG=ko_KR.eucKR # 언어_지역.문자코드
LC_CTYPE="ko_KR.eucKR"     # 문자종별
LC_NUMERIC="ko_KR.eucKR"   # 수치 표기
LC_TIME="ko_KR.eucKR"      # 일시 표기
LC_COLLATE="ko_KR.eucKR"   # 조합 순서
LC_MONETARY="ko_KR.eucKR"  # 통화 표기
```

![](assets/Linux%20note-15.png)

##### 로케일 설정
- 사용 언어, 지역, 문자코드는 LANG이라고 하는 환경 변수로 통합하여 설정한다. LANG 변수를 설정하려면 export 명령을 사용한다. 
```shell
export LANG=ko_KR.UTF-8
```
- 👉 export : 환경변수나 쉘 변수 값을 설정한다. 

##### 기타 로케일
- en_GB.UTF-8 : 영국
- en_CA.UTF-8 : 캐나다
- en_US.UTF-8 : 미국
- `export LANG=C` 라고 지정하면, 로케일 지정이 없는 상태, 컴퓨터 본래의 언어를 사용하는 설정이 된다. C는 common의 약자이다. 

- `windows키` + `스페이스`로 일반적인 입력(영어)와 한국어 입력을 전환할 수 있다. 