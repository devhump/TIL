### 1장. 기초 : 바로 시작하기

```python
# 현재 작업 디렉터리 반환하는 함수
from os import getcwd

where_am_I = getcwd()
where_am_I
'/Users/ramy/Documents'

# 현재 파이썬 실행중인 플랫폼 출력
import sys
sys.platform
'darwin' # 맥 OS X 커널명

print(sys.version) 실행중인 파이썬 버전 출력
# '3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]'


## bash 환경에서 작동 
## 내 코드가 어떤 폴더에서 실행 중인지를 나타냄
>>> import os 
>>> os.getcwd()
'/Users/ramy'
```

```python
# 개별 환경 변수 및 전체 환경변수에 접근하기

>>> import os
# ('environ'에 포함된 데이터의) 특정 이름의 속성에 접근 
>>> os.getenv('HOME') # 개별 환경 변수에 접근
'C:\\Users\\blues'
>>> os.environ ## 시스템의 전체 환경 변수에 접근
# environ({'ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA': 'C:\\Users\\blues\\AppData\\Roaming', 'ASL.LOG': 'Destination=file', 'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files', 'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 'COMPUTERNAME': 'DESKTOP-D7LHQLN', 'COMSPEC': 'C:\\WINDOWS\\system32\\cmd.exe', 'DRIVERDATA': 'C:\\Windows\\System32\\Drivers\\DriverData', 'FPS_BROWSER_APP_PROFILE_STRING': 'Internet Explorer', 'FPS_BROWSER_USER_PROFILE_STRING': 'Default', 'HOME': 'C:\\Users\\blues', 'HOMEDRIVE': 'C:', 'HOMEPATH': '\\Users\\blues', 'LOCALAPPDATA': 'C:\\Users\\blues\\AppData\\Local', 'LOGONSERVER': '\\\\DESKTOP-D7LHQLN', 'NUMBER_OF_PROCESSORS': '4', 'ONEDRIVE': 'C:\\Users\\blues\\OneDrive', 'OS': 'Windows_NT', 'PATH': 'C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS\\System32\\OpenSSH\\;C:\\Program Files\\Git\\cmd;C:\\sqlite;C:\\Program Files\\Bandizip\\;C:\\Users\\blues\\AppData\\Local\\Programs\\Python\\Python39\\Scripts\\;C:\\Users\\blues\\AppData\\Local\\Programs\\Python\\Python39\\;C:\\Users\\blues\\AppData\\Local\\Microsoft\\WindowsApps;;C:\\Users\\blues\\AppData\\Local\\Programs\\Microsoft VS Code\\bin;C:\\Program Files\\heroku\\bin', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC', 'PROCESSOR_ARCHITECTURE': 'AMD64', 'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 60 Stepping 3, GenuineIntel', 'PROCESSOR_LEVEL': '6', 'PROCESSOR_REVISION': '3c03', 'PROGRAMDATA': 'C:\\ProgramData', 'PROGRAMFILES': 'C:\\Program Files', 'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 'PROGRAMW6432': 'C:\\Program Files', 'PSMODULEPATH': 'C:\\Program Files\\WindowsPowerShell\\Modules;C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\Modules', 'PUBLIC': 'C:\\Users\\Public', 'SESSIONNAME': 'Console', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:\\WINDOWS', 'TEMP': 'C:\\Users\\blues\\AppData\\Local\\Temp', 'TMP': 'C:\\Users\\blues\\AppData\\Local\\Temp', 'USERDOMAIN': 'DESKTOP-D7LHQLN', 'USERDOMAIN_ROAMINGPROFILE': 'DESKTOP-D7LHQLN', 'USERNAME': 'ramy', 'USERPROFILE': 'C:\\Users\\blues', 'WINDIR': 'C:\\WINDOWS'})
```

- p51
```python
>>> import datetime
>>> datetime.date.today() # 오늘 날짜 출력
datetime.date(2023, 3, 9)

## 각각 오늘 날짜, 월, 연도 출력
>>> datetime.date.today().day
9
>>> datetime.date.today().month
3
>>> datetime.date.today().year
2023

## 현재 날짜, 또는 시간을 특정 포맷으로 출력하기
>>> datetime.date.isoformat(datetime.date.today())
'2023-03-09'

>>> import time
>>> time.strftime("%H:%M")
'13:17'

## 요일과 오전/오후 표시
>>> time.strftime("%A %p")
'Thursday PM'

## HTML 라이브러리의 활용
>>> import html
# HTML 문법 인코딩하지 않기
>>> html.escape("This HTML fragment contains a <script>script</script> tag.")
'This HTML fragment contains a &lt;script&gt;script&lt;/script&gt; tag.'
# HTML 문법 인코딩하기
>>> html.unescape("I &hearts; Python's &lt;standard library&gt;.")
"I ♥ Python's <standard library>."


```

- 파이썬 라이브러리에 대한 추가적인 정보  👉 [파이썬 표준 라이브러리](https://docs.python.org/ko/3/library/index.html )
- 3rd 파티 모듈 찾아보기 👉 https://pypi.org/


- 파이썬 변수는 동적으로 할당된다. 
	- 파이썬에서는 처음 변수를 사용할 때 변수가 생성되며, **변수의 유형은 미리 선언할 필요가 없다!**
		- 파이썬의 변수 유형은 변수에 할당(=, 할당 연산자)하는 객체의 유형에 의해 결정된다. 

- 파이썬은 중괄호(`{}`)가 아닌 들여쓰기(indentation)으로 코드 블럭을 구분한다. 
- 또한, 코드블록을 **'스위트(suite)'** 라고도 표현한다. 

- p59
#### 핵심정리

```ad-note
- 파이썬은 IDLE이라는 내장 IDE를 제공한다. IDLE을 이용해 코드 작성/편집/실행 가능하고, 코드 작성후 파일로 저장해서 `F5` 키를 누르면 코드가 실행된다. 
- IDLE은 컴파일-링크-실행 과정을 자동화해주는 파이썬 인터프리터와 상호작용합니다. 따라서 우리는 코드 작성에만 집중할 수 있습니다. 
- 인터프리터는 파일에 저장된 여러분 코드를 꼭대기에서 밑바닥까지 **한 번에 한 행씩** 실행합니다. 파이썬에는 `main()` 함수/메서드의 개념이 없습니다. 
- 파이썬은 많은 재사용할 수 있는 모듈을 제공하는 강력한 표준 라이브러리를 포함하고 있습니다. 앞서 살펴본 `datetime`이 그 예입니다. 
- 파이썬 프로그램을 작성할 때 표준 자료구조 모음을 사용할 수 있습니다. 일례로 배열과 개념이 비슷한 리스트가 있습니다. 
- 파이썬에서는 변수의 유형을 선언할 필요가 없습니다. 변수에 값을 할당하면 변수 유형을 동적으로 결정합니다. 
- `if/elif/else` 문으로 의사 결정을 할 수 있습니다. 파이썬에서는 `if/elif/else` 라는 키워드가 스위트라고 불리는 블록 앞에 등장합니다. 
- 코드 스위트는 항상 들여쓰기 되어 있어서 쉽게 식별 할 수 있습니다. 파이썬에서는 오직 들여 쓰기로 코드를 그룹화 합니다. 
- 코드 스위트 앞에는 콜론(`:`)을 붙입니다. 콜론은 파이썬의 문법적 요구사항입니다. 
```

- p70
- `dir()`은 모듈 및 속성을 출력한다.
```python
import random
dir(random)
# ['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_ONE', '_Sequence', '_Set', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_accumulate', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_floor', '_index', '_inst', '_isfinite', '_log', '_os', '_pi', '_random', '_repeat', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randbytes', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']

help(randdom)
help(random.randint)
```

![[../assets/Head First - Python.png]]

```ad-hint
- randint(self, a, b)
	- Return random integer in range [a, b], including both end points.
```

- ==윈도우나 리눅스의 IDLE에서는 `alt + P`를 누르면 가장 마지막에 입력한 명령이 나타난다. 이때, `P`는 previous의 약자이며, Mac에서는 `ctrl + P`이다. ==


### 2장. 리스트 데이터
