### 이스케이프 코드 

|  코드  |                          설명                           |
|:------:|:-------------------------------------------------------:|
|  `\n`  |             문자열 안에서 줄을 바꿀 때 사용             |
|  `\t`  |           문자열 사이에 탭 간격을 줄 때 사용            |
|  `\\`  |             문자 \\를 그래도 표현할 때 사용             |
|  `\'`  |        작은 따옴표(`'`)를 그대로 표현 할 때 사용        |
|  `\"`  |         큰 따옴표(`"`)를 그대로 표현 할 때 사용         |
|  `\r`  | 캐리지 리턴(줄 바꿈 문자, 현재 커서를 가장 앞으로 이동) |
|  `\f`  |    폼 피드(줄 바꿈 문자, 현재 커서를 다음 줄로 이동)    |
|  `\a`  |    벨 소리 (출력할 때 PC 스피커에서 '삑'소리가 난다)    |
|  `\b`  |                       백스페이스                        |
| `\000` |                         널 문자                         |

### 문자열 포매팅
```python
>>> "I eat %d apples" % 3
"I eat 3 apples"

>>> "I eat %s apples" % five
"I eat five apples"

>>> number = 3
>>> >>> "I eat %d apples" % number
"I eat 3 apples"

>>> number = 3
>>> day = "three"
>>> >>> "I eat %d apples. so I sick for %s days" % (number, day)
"I eat 3 apples. so I sick for three days"
```

#### 문자열 포맷 코드

| 코드 |           설명            |
|:----:|:-------------------------:|
| `%s` |       문자열(Sting)       |
| `%c` |    문자 1개(Character)    |
| `%d` |      정수(Interger)       |
| `%d` | 부동 소수(Floating-point) |
| `%o` |           8진수           |
| `%x` |          16진수           |
| `%%` | Literal % (문자 '%' 자체) |

```python
"Error is %d%" % 98
→ Error 발생

"Error is %d%%" % 98
→ 'Error is 98%' 
```

```python
>>> "%10s" % "hi"
'        hi'

>>> "%-10sjane" % "hi"
'hi        jane'

>>> "%0.4f" % 3.42134234
'3.4213'

>>> "%10.4f" % 3.42134234
'    3.4213'
```

##### format 함수 이용
```python
>>>"I eat {0} apples".format(3)
"I eat 3 apples"

>>>"I eat {0} apples".format("five")
"I eat five apples"

>>> number = 3
>>>"I eat {0} apples".format(number)
"I eat 3 apples"


>>> number = 3
>>> day = "three"
>>> >>> "I eat {0} apples. so I sick for {1} days".format(number, day)
"I eat 3 apples. so I sick for three days"

>>> >>> "I eat {number} apples. so I sick for {day} days".format(number=3, day="three")
"I eat 3 apples. so I sick for three days"
```

###### 정렬하기
```python
>>> "{0:<10}".format("hi")
'hi        '

>>> "{0:>10}".format("hi")
'        hi'

>>> "{0:^10}".format("hi")
'    hi    '

>>> "{0:=^10}".format("hi")
'====hi===='

>>> y = 3.42134234
>>> "{0:0.4f}.format(y)"
'3.4213'
>>> "{0:10.4f}.format(y)"
'    3.4213'

>>> "{{ and }}".format()
'{ and }'
```

#### f 문자열 포매팅(f-string)
```python
>>> age = 30
>>> f'나는 내년에 {age+1}살이 된다'
'나는 내년에 31살이 된다'

# f-string에서도 앞서 말한 정렬, 공백 채우기등이 가능하다 
>>> f{"hi":<10}
'hi        '
```

### 리스트
- 리스트의 연산
```python
>>> a = [1, 2, 3]
>>> b = [4, 5]
>>> a + b
[1, 2, 3, 4, 5]

>>> a = [1, 2, 3]
>>> a * 3
[1, 2, 3, 1, 2, 3, 1, 2, 3]

>>> a = [1, 2, 3]
>>> del a[1]
>>> a 
[1, 3]

>>> a = [1, 2, 3]
>>> a.append(4)
>>> a 
[1, 2, 3, 4]
>>> a.append([5])
>>> a
[1, 2, 3, 4, [5]]
```

- insert
```python
a = [1, 2, 3]
a.insert(0,4)
print(a)
# [4, 1, 2, 3]
```

- remove
	- 리스트에서 첫번째로 나오는 x를 삭제하는 함수이다
```python
>>> a = [1, 2, 3, 1, 2, 3]
>>> a.remove(3)
[1, 2, 1, 2, 3]
```

- extent
	- `extend(x)` x에는 리스트만 올 수 있으며, 원래의 리스트에서 리스트 x를 더하게 된다.
```python
>>> a = [1, 2, 3]
>>> a.extend([4,5])
>>> a 
[1, 2, 3, 4, 5]

# a += [4,5] 와 동일
```



### 딕셔너리
- `Keys:Value` 쌍 모두 지우기
```python
>>> a.clear 
>>> a
{}
```

- 비어있는 딕셔너리 생성 방법
	- `a = dict()` 또는 `a = {}`


### 집합 자료형
- 집합 자료형 생성 → set 키워드 사용
```python
>>> s1 = set([1, 2, 3])
>>> s1
{1, 2, 3}

>>> s2 = set("Hello")
>>> s2
{'e', 'H', 'l', 'o'}
```

#### set 의 특징
- 중복을 허용하지 않는다.
- ***순서가 없다(Unordered)***
	- set 자료형의 요소를 인덱스로 접근하려면 list()나 tuple()을 사용해야 한다. 

#### 교집합, 합집합, 차집합
```python
>>> s1 = set([1, 2, 3, 4, 5, 6])
>>> s2 = set([4, 5, 6, 7, 8, 9])

# 교집합
>>> s1 & s2
{4, 5, 6}

>>> s1.intersection(s2)
{4, 5, 6}

# 합집합
>>> s1 | s2
{1, 2, 3, 4, 5, 6, 7, 8, 9}

>>> s1.union(s2)
{1, 2, 3, 4, 5, 6, 7, 8, 9}

# 차집합
>>> s1 - s2
{1, 2, 3}
>>> s2 - s1
{7, 8, 9}

>>> s1.diffrence(s2)
{1, 2, 3}
```

#### 집합 자료형 관련 함수
- 값 1개 추가하기 (add)
```python
>>> s1 = set([1, 2, 3])
>>> s1.add(4)
>>> s1
{1, 2, 3, 4}
```

- 값 여러개 추가하기 (update)
```python
>>> s1 = set([1, 2, 3])
>>> s1.update([4, 5, 6])
>>> s1
{1, 2, 3, 4, 5, 6}
```

- 특정 값 제거하기 (remove)
```python
>>> s1 = set([1, 2, 3])
>>> s1.remove(2)
>>> s1
{1, 3}
```

### bool
```python
>>> bool('python')
True
>>> bool('')
False
>>> bool([1,2,3])
True
>>> bool([])
False
>>> bool(0)
False
>>> bool(3)
True
```

### 제어문 & 조건문 & 반복문
- 조건문 (if, else) 다음에 수행할 문장에 한줄 밖에 되지 않으면 간략하게 코드 작성이 가능하다. `:` 뒤에 바로 내용을 작성하면 된다. 
```python
if 'money' in pocket:
	pass
else:
	print("카드를 꺼내라")

>>> pocket = ['paper', 'money', 'cellphone']
>>> if 'money' in pocket: pass
... else: print("카드를 꺼내라")
```

#### 조건부 표현식
```python
if score >= 60:
	message = "success"
else:
	message = "failure"
```

- 👆 위아래 코드는 동일한 내용👇
```python
message = "success" if score >= 60 else "failure"
# 조건문이 참인 경우 if 조건문 else 조건문이 거짓인 경우
```


#### for문 응용
```python
a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
	print(first+last)
# 3
# 7
# 11
```


### 프로그램의 입출력
- 여러 개의 입력값을 받는 함수 만들기
```python
def add_many(*args):
	result = 0
	for i in args:
		result += i
	return result

result = add_many(1,2,3)
print(result)
# 6

def add_mul(choice, *args):
	if choice == "add":
		result = 0
		for i in args:
			result += i
	if choice == "mul":
		result = 1
		for i in args:
			result *= i
	return result

result = add_mul('mul', 1, 2, 3, 4, 5)
print(result)
# 120
```
* `*args`는 매개변수를 뜻하는 영어 단어 arguments의 약자이며, 관례적으로 자주 사용한다.

```python
def print_kwargs(**kwargs):
	print(kwargs)

print_kwargs(name="foo", age=3)
# {'age':3, 'name':'foo'}
```
- 👉 `**kwargs` 처럼 매개변수 이름 앞에 `**`을 붙이면 매개변수 kwargs는 딕셔너리가 되고, 모든 key=value 형태의 결과값이 그 딕셔너리에 저장된다.
	- kwargs는 keyword arguments의 약자이며, arg와 마찬가지로 관례적으로 사용한다. 

#### 함수의 결과값은 언제나 하나이다
```python
def add_and_mul(a,b):
	return a+b, a*b

result = add_and_mul(3,4)
# result = (7, 12)
res1, res2 = add_and_mul(3,4)
```
- 👉 ==두 개 이상의 결과값이 있을 경우 하나의 튜플로 바꾸어 반환한다.==

```python
def add_and_mul(a,b):
	return a+b 
	return a*b # 실행되지 않음
```
- 👉 ==두개 이상의 return 값이 있을 경우 첫번째 return 문만 실행됨==

```python
def say_nick(nick):
	if nick == "바보"
		return
	print("나의 별명은 %s 입니다" % nick)

>>> say_nick("야호")
'나의 별명은 야호입니다'
>>> say_nick("바보")
>>>
```
- 특별한 상황일 때 함수를 빠져나가고 싶다면 return을 단독으로 써서 함수를 즉시 빠져나갈 수 있다. 

##### 매개변수에 초깃값 미리 설정하기
```python
def say_myself(name, old, man=True):
	print("나의 이름은 %s입니다." % name)
	print("나는 %d살 입니다." % old)
	if man:
		print("남자입니다.")
	else:
		print("여자입니다.")
```
- 이때, 매개변수의 초깃값을 설정한 이후에는 일반 변수가 올 수 없다. 
```python
def say_myself(name, man=True, old):
⇒ 에러 발생
SyntaxError: non-default argument follows default argument
```

#### lambda 함수
```python
add = lambda a,b: a+b
result = add(3,4)
print(result)
# 7
```

#### print()
```python
>>> print("a" "b" "c")
abc
>>> print("a", "b", "c")
a b c
```


#### 파일 읽고 쓰기 
```python
f = open("새파일.txt", "w")
f.close()

# 파일객체 = open(파일이름, 파일열기모드)
```

##### 파일 열기 모드

| 파일 열기 모드 |                           설명                           |
|:--------------:|:--------------------------------------------------------:|
|       r        |            읽기 모드 - 파일 읽기만 할 때 사용            |
|       w        |           쓰기 모드 - 파일에 내용을 쓸 때 사용           |
|       a        | 추가 모드 - 파일의 마지막에 새로운 내용을 추가할 때 사용 |

##### 파일을 쓰기 모드로 열어 출력값 적기
```python
# writedata.py
f = open("C:/doit/새파일.txt", 'w')
for i in range(1, 11):
	data = "%d번째 줄입니다.\n" % i
	f.write(data)
f.close()
```

#### 프로그램 외부에 저장된 파일을 읽는 여러가지 방법
##### readline
```python
# readline.py

f = open("C:/doit/새파일.txt", 'r')
line = f.readline()
print(line)
f.close()

# readline_all.py

f = open("C:/doit/새파일.txt", 'r')
while True:
	line = f.readline()
	if not line: break
	print(line)
f.close()

```

##### readlines
```python
f = open("C:/doit/새파일.txt", 'r')
lines = f.readlines()
for line in lines:
	print(line)
f.close()
```

##### read
```python
f = open("C:/doit/새파일.txt", 'r')
data = f.read()
print(data)
f.close()
```

#### with문과 함께 사용하기
```python
with open("foo.txt", "w") as f:
	f.write("Life is too short, you need python")
```
- 👉 ***with 블록을 벗어나는 순간 열린 파일 객체 f가 자동으로 close되어 편리하다.***

#### sys 모듈로 매개 변수 주기
##### case 1
```python
# sys1.py
import sys

args = sys.argv[1:]
for i in args:
	print(i)
```

```python
$ python sys1.py aaa bbb ccc
aaa
bbb
ccc
```

##### case 2
```python
# sys2.py
import sys

args = sys.argv[1:]
for i in args:
	print(i.upper(), end=" ")
```

```python
$ python sys2.py aaa bbb ccc
AAA BBB CCC
```


### 클래스 만들기
```python
>>> class FourCal:
...	pass
    
>>> a = FourCal()
>>> type(a)
<class '__main__.FourCal'>
```

```python
class FourCal:
	def setdata(self, first, second):
		self.first = first
		self.second = second

>>> a = FourCal()
>>> a.setdata(4,2) 
```
- 👉 self는 매개변수로 넘겨주지 않아도, setdata를 호출한 객체 a가 자동으로 전달된다.

```python
>>> a = FourCal()
>>> FourCal.setdata(a, 4, 2)

>>> a = FourCal()
>>> a.setdata(4,2)
```
- 👉 '클래스 이름.메서드' 형태로 호출할 때는 객체 a를 매개변수 self에 꼭 전달해 주어야 한다. 
	- 반면, '객체.메서드' 형태로 호출할 때에는 self를 반드시 생략해서 호출해야 한다.

```python
>>> a = FourCal()
>>> a.setdata(4,2)

→ 이 때, def setdata(a, first, second): 에서
a.first = first
a.second = second 로 해석된다.

print(a.first)
# 4
```

```python
>>> a = FourCal()
>>> a.setdata(4,2)
>>> b = FourCal()
>>> b.setdata(4,2) 

>>> id(a.first)
1838194944
>>> id(b.first)
1838194928
```
- 각 객체의 속성은 다른 id값을 지닌다 → ***객체 변수는 고유한 메모리값을 지닌다!***
	- 👉==객체 변수는 다른 객체들 영향을 받지 않고 독립적으로 그 값을 유지한다.==

###### 클래스에 기능 추가하기
```python
class FourCal:
	def setdata(self, first, second):
		self.first = first
		self.second = second
	def add(self):
		result = self.first + self.second
		return result
	def mul(self):
		result = self.first * self.second
		return result
	def sub(self):
		result = self.first - self.second
		return result
	def div(self):
		result = self.first / self.second
		return result
```

```python
>>> a = FourCal()
>>> a.setdata(4,2)
>>> a.add()
6
>>> a.mul()
8
>>> a.div()
2
>>> a.sub()
2
```

#### 생성자(constructor)
![](assets/Jump%20to%20Python.png)

- 👉 FourCal 클래스의 인스턴스 a에 setdata 메서드를 수행하지 않고 add 메서드를 수행하면 오류가 발생한다. setdata 메서드를 수행해야 객체 a의 객체변수 first 와 second가 생성되기 때문이다.

###### 생성자란? (constructor) 
- 객체가 생성될 때 자동으로 호출되는 메서드를 의미한다
- 파이썬 메서드 이름으로 `__init__`를 사용하면 이 메서드는 생성자가 된다.
```python
class FourCal:
	def __init__(self, first, second):
		self.first = first
		self.second = second

	def setdata(self, first, second):
		self.first = first
		self.second = second
	def add(self):
		result = self.first + self.second
		return result
	def mul(self):
		result = self.first * self.second
		return result
	def sub(self):
		result = self.first - self.second
		return result
	def div(self):
		result = self.first / self.second
		return result
```

![](assets/Jump%20to%20Python-1.png)
- 👉 생성자가 있을 경우에 변수 값 없이 호출하면 에러가 발생한다. 
```python
>>> a = FourCal(4,2)
>>> a.first
4
```

#### 클래스의 상속
- class 클래스 이름(상속할 클래스 이름)
```python
class MoreFourCal(FourCal):
	pass
```

```python
>>> a = MoreFourCal(4,2)
>>> a.add()
6
>>> a.mul()
8
>>> a.div()
2
>>> a.sub()
2
```
- 👉 ***상속 받은 클래스는 부모의 클래스 기능을 모두 사용할 수 있다!***

##### 자식 클래스의 기능 추가
```python
class MoreFourCal(FourCal):
	def pow(self):
		result = self.first ** self.second
		return result

>>> a = MoreFourCal(4,2)
>>> a.pow()
16
```

```ad-tip
- 상속은 기존 클래스는 그대로 놔둔 채 클래스의 기능을 확장 시킬 때 주로 사용한다.
- 기존 클래스를 수정하지 않고, 상속으로 처리하는 이유는 → ==기존 클래스가 라이브러리 형태로 제공되거나 수정이 허용되지 않는 상황에서는 상속을 이용해야 하기 때문이다.==
```

##### 메소드 오버라이딩
- 부모 클래스에 있는 메서드를 동일한 이름으로 다시 만드는 것을 **메서드 오버라이딩(Overriding, 덮어쓰기)**한다. 이렇게 메서드를 오버라이딩하면 부모클래스의 메서드 대신 오버라이딩한 메서드가 호출된다.
```python
>>> a = FourCal(4,0)
>>> a.div()

→ 에러 발생!
```

![](assets/Jump%20to%20Python-2.png)

```python
class SafeFourCal(FourCal):
	def div(self):
		if self.second == 0:
			return 0
		else:
			return self.first / self.second
```

![](assets/Jump%20to%20Python-3.png)

#### 클래스 변수
- 클래스 변수는 클래스 안에 함수를 선언하는 것과 마찬가지로, 클래스 안에 변수를 선언하여 생성한다. 
```python
>>> class Family:
>>> 	lastname = "김"

>>> print(Family.lastname)
김
>>> a = Family()
>>> a.lastname
김
>>> b = Family()
>>> b.lastname
김

# 클래스 변수 값의 변경
>>> Family.lastname = "박"
>>> a.lastname
박

# 클래스 변수의 id값은 동일
>>> id(Family.lastname)
4480159136
>>> id(a.lastname)
4480159136
>>> id(b.lastname)
4480159136
```


### 모듈
- 모듈이란 함수나 변수 또는 클래스를 모아 놓은 파일이다. 

```python
# mod1.py
def add(a, b):
	return a + b

def sub(a, b):
	return a - b
```

![](assets/Jump%20to%20Python-4.png)

```plain
import 모듈 이름

from 모듈 이름 import 모듈 함수
from 모듈 이름 import 모듈함수1, 모듈함수2
from 모듈 이름 import *
```

- 위 방식으로 모듈을 호출하여 해당 모듈의 함수를 사용할 수 있다.

#### `if __name__=="__main__":` 의 의미
- mod1 파일을 수정하고 실행하였다.
```python
# mod1.py
def add(a, b):
	return a + b

def sub(a, b):
	return a - b

print(add(1,4))
print(add(4,2))
```
![](assets/Jump%20to%20Python-5.png)

- 파이썬 환경에서 import 한 결과 아래와 같은 결과가 나온다. 
![](assets/Jump%20to%20Python-6.png)

- 👇 아래와 같이 수정을 하면
```python
# mod1.py
def add(a, b):
	return a + b

def sub(a, b):
	return a - b

if __name__=="__main__":
	print(add(1,4))
	print(add(4,2))
```

![](assets/Jump%20to%20Python-7.png)

- 해당 파일(모듈)을 직접 실행 시킬 때에만 print 구문이 실행되는 것을 알 수 있다. 

```ad-tip
- `__name__` 변수란?
	- 파이썬의 `__name__` 변수는 파이썬이 내부적으로 사용하는 특별한 변수 이름이다.
	- mod1.py을 직접 실행 시킬 경우 `__name__`에는 `__main__`값이 저장된다.
	- 하지만, 다른 파이썬 쉘이나 모듈에서 import 할 경우에는 mod1.py의 `__name__` 변수에 mod1.py의 모듈값 mod1이 저장된다.
```

```python
# mod2.py

PI = 3.141592

class Math:
	def solv(self, r):
		return PI * (r ** 2)

def add(a,b):
	return a+b
```

![](assets/Jump%20to%20Python-8.png)

```python
# modtest.py
import mod2
result = mod2.add(3, 4)
print(result)
```

![](assets/Jump%20to%20Python-9.png)

##### 다른 디렉터리에 있는 모듈 불러오기
1. sys.path.append(모듈을 저장한 디렉터리) 사용하기
![](assets/Jump%20to%20Python-10.png)
```shell
python
```

```python
>>> import sys
>>> sys.path
>>> sys.path.append("C:/doit/mymod")
```

2. PYTHONPATH 환경 변수 활용하기
	- 해당 명령어는 cmd 환경에서만 가능
```shell
$ set PYTHONPATH=C:\doit\mymod
$ python
```

```python
>>> import mod2
>>> print(mod2.add(3,4))
```

### 패키지
#### 모듈 불러오기

```cmd
$ set PYTHONPATH=C:/doit
```

```python
>>> import game.sound.echo
>>> game.sound.echo.echo_test()
echo
```

```python
>>> from game.sound import echo
>>> echo.echo_test()
echo
```

```python
>>> from game.sound.echo import echo_test
>>> echo_test()
echo
```

![](assets/Jump%20to%20Python-11.png)

![](assets/Jump%20to%20Python-12.png)

- 👉 import game을 수행하면 game 디렉터리의 모듈 또는 game 디렉터리의 `__init__.py`에 정의한 것만 참조할 수 있다. 
- 👉 도트 연산자(`.`)를 사용해서 import a.b.c 처럼 import 할 때 가장 마지막 항목인 c는 반드시 모듈 또는 패키지여야만 한다.

#### `__init__.py`의 용도
- `__init__.py` 파일은 해당 디렉터리가 패키지의 일부임을 알려주는 역할을 한다. 만약 game, sound, graphic 등 패키지에 포함된 디렉터리에 `__init__.py` 파일이 없다면 패키지로 인식하지 않는다. 

```ad-tip
- python3.3 버전부터는 `__init__.py` 파일이 없어도 패키지로 인식한다. (PEP 420) 하지만 하위 버전 호환을 위해 `__init__.py` 파일을 생성하는 것이 안전한 방법이다.
```

![](assets/Jump%20to%20Python-13.png)

- 특정 디렉터리의 모듈을 `*`를 사용하여 import 할 때는 다음과 같이 해당 디렉터리의  `__init__.py` 파일에 `__all__` 변수를 설정하고 import할 수 있는 모듈을 정의해 주어야 한다.
```python
# C:/doit/game/sound/__init__.py
__all__ = ['echo']

# C:/doit/game/graphic/__init__.py
__all__ = ['render']
```

![](assets/Jump%20to%20Python-14.png)

```python
# render.py
# from game.sound.echo import echo_test
from ..sound.echo import echo_test # 위와 동일

def render_test():
	print("render")
	echo_test()
```
- 👉 이런 relative한 접근자는 모듈 내에서만 사용해야 한다. <br>인터프리터에서 사용시 오류발생 !

### 예외 처리
```python
try:
	...
except [발생 오류 [as 오류 메시지 변수]]:
	...
```

```python
try:
	4 / 0
except ZerodivisionError as e:
	print(e)

# division by Zero
```

#### try ... finally
- finally 블록은 예외 발생 유무와 상관없이 실행 됨.
```python
f = open('foo.txt', 'w')
try:
	# 무언가를 수행한다.
finally:
	f.close()
```

#### 여러개의 오류 처리
```python
try:
	a = [1, 2]
	print(a[3])
	4/0
except ZeroDivisioError as e:
	print(e)
except IndexError as e:
	print(e)
```

```python
try:
	a = [1, 2]
	print(a[3])
	4/0
except (ZeroDivisioError, IndexError) as e:
	print(e)
```
- 👉 2개 이상의 오류를 한번에 처리하기 위해 괄호를 사용할 수 있다. 

#### 오류 회피하기
```python
try:
	f = open("나없는파일", 'r')
except FileNotFoundError:
	pass 	
# 파일이 존재하지 않더라도 오류 발생 없이 통과 시킨다.
```

#### 오류 일부러 발생 시키기
- 프로그래밍 하다 보면 종종 오류를 일부러 발생시켜야 할 경우가 생기는데, 파이썬은 raise 명령어를 통해 오류를 강제로 발샐 시킬 수 있다.

```python
class Bird:
	def fly(self):
		raise NotImplementedError
```
- NotImplementedError: 아직 구현되지 않은
	- 파이썬 내장 오류로, 꼭 작성해야 하는 부분이 구현되지 않았을 경우, 일부러 오류를 발생시키기 위해 사용한다.

- 해당 부분 구현 없이 작동하면?
```python
class Eagle(Bird):
	pass

eagle = Eagle()
eagle.fly()
```

![](assets/Jump%20to%20Python-15.png)
- 👉 NotImplementedError가 발생한다.

```python
class Eagle(Bird):
	def fly(self):
		print("very fast")

eagle = Eagle()
eagle.fly()
# very fast
```
- 따라서 해당 부분 구현 후 작동해야 한다. 

#### 예외 만들기
```python
class MyError(Exception):
	pass
```
- 커스텀 에러 작성을 위해서 파이썬 내장 클래스인 Exception을 상속받아 사용한다. 

```python
def say_nick(nick):
	if nick == '바보':
		raise MyError()
	print(nick)
```

![](assets/Jump%20to%20Python-16.png)

```python
try:
	say_nick("천사")
	say_nick("바보")
except MyError:
	print("허용되지 않는 별명입니다.")

또는 

try:
	say_nick("천사")
	say_nick("바보")
except MyError as e:
	print(e)

#############################
class MyError(Exception):
	def __str__(self):
		return "허용되지 않는 별명입니다."

```

### 내장 함수

#### all
- all(x)는 반복가능한(iterable) 자료형 x를 입력 인수로 받으며, 이 x가 모두 참이면 True, 거짓이 하나라도 있으면 False를 돌려준다. 
```python
>>> all([1,2,3])
True

>>> all([1,2,3,0])
False
```

#### any
- any(x)는 x중 하나라도 참이 있으면 True를 돌려주고, x가 모두 거짓일 때에만 False를 돌려준다. all(x)의 반대이다. 
```python
>>> any([1, 2, 3, 0])
True

>>> any([0, ""])
False
```

#### dir
- dir은 객체가 자체적으로 가지고 있는 변수나 함수를 보여준다. 다음 예는 리스트와 딕셔너리 객체 관련 함수(메서드)를 보여주는 예제이다.
```python
dir([1,2,3])
dir({'1':'a'})
```


![](assets/Jump%20to%20Python-17.png)

#### dicmod
- divmod(a, b)는 2개의 숫자를 입력으로 받는다. 그리고 a를 b로 나눈 몫과 나머지를 튜플 형태로 돌려주는 함수이다. 
```python
>>> divmod(7,3)
(2, 1) # ← 7나누기 3의 몫과 나머지
```

#### enumerate
- enumerate는 '열거하다'라는 뜻이다. 이 함수는 순서가 있는 자료형을 입력으로 받아, 인덱스 값을 포함하는 enumerate 객체를 돌려준다. 
```python
>>> for i, name in enumerate(['boy', 'foo', 'bar'])
... 	print(i, name)
...
0 body
1 foo
2 bar
```


#### eval
- eval(expression)은 실행가능한 문자열을 받아 문자열을 실행한 결과값을 돌려주는 함수이다. 
```python
>>> eval('1+2')
3
>>> eval("'hi' + 'a'")
'hia'
>>> eval('divmod(4, 3)')
(1, 1)
```
- 👉 보통 eval은 입력받은 문자열로 파이썬 함수나 클래스를 동적으로 실행하고 싶을 때 사용한다.

#### filter
- '걸러낸다'는 단어의 뜻처럼, filter 함수도 동일한 의미를 가진다. 
- 첫번째 인수로는 함수 이름을, 두번째 인수로 그 함수에 차례로 들어갈 반복 가능한 자료형을 받는다. 그리고 두번째 인수인 반복 가능한 자료형 요소가 첫번째 인수인 함수에 입력되었을 때 반환 값이 참인 것만 걸러내서 돌려준다. 
```python
# positive.py
def position(l):
	result = []
	for i in l:
		if i > 0:
			result.append(i)
	return result

print(positive([1, -3, 2, 0, -5, 6]))
# [1, 2, 6]
```

- 위 함수를 filter 함수로 나타내면
```python
# filter1.py
def positive(x):
	return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6])))
# [1, 2, 6]

####################
# lambda 함수 황용

list(filter(lambda x : x > 0, [1, -3, 2, 0, -5, 6]))
```


#### hex
- hex(x)는 정수 값을 입력받아 16진수(hexadecimal)로 변환하여 돌려주는 함수이다.
```python
>>> hex(234)
'0xea'
>>> hex(3)
'0x3'
```

#### id
- id(object)는 객체를 입력받아 객체의 고유한 주소값을 돌려주는 함수 이다.

#### int
- int(x)는 문자열 형태의 숫자나 소수점이 있는 숫자 등을 정수 형태로 돌려주는 함수로, 정수를 입력 받으면 그대로 돌려준다.

##### int(x, radix)
- int(x, radix)는 radix 진수로 표현된 문자열 x를 10진수로 변환하여 돌려준다.
```python
>>> int('11', 2) # 2진수 11을 10진수 값으로
3
>>> int('1A', 16) # 16진수 1A를 10진수 값으로
26
```

#### isinstance
- isinstance(object, class)는 첫번째 인수로 인스턴스, 두번째 인수로 클래스 이름을 받는다. 입력으로 받은 인스턴스가 그 클래스의 인스턴스인지를 판단하여 참이면 True, 거짓이면 False를 돌려준다.
```python
>>> class Person: pass # 아무 기능 없는 Person 클래스 생성
...
>>> a = Person()
>>> isinstance(a, Person)
True

>>> b = 3
>>> isinstance(b, Person)
False
```

#### list
- list(s)는 반복 불가능한 자료형 s를 입력받아 리스트로 만들어 돌려주는 함수이다.
- list 함수에 리스트를 입력으로 주면 똑같은 리스트를 복사하여 돌려준다.
```python
>>> a = [1, 2, 3]
>>> b = list(a)
>>> b 
[1, 2, 3]
```


#### map
- map(f, iterable)은 함수(f)와 반복가능한(iterable) 자료형을 입력으로 받는다. map은 입력 받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려주는 함수이다.
```python
# two_times.py
def two_times(numberList):
	result = []
	for number in numberList:
		result.append(number*2)
	return result

result = two_times([1,2,3,4])
print(result)
# [2, 4, 6, 8]

########################
# map으로 바꾸면

>>> def two_times(x): return x*2
...
list(map(two_times, [1, 2, 3, 4]))

#########################
# map & lambda 로 바꾸면

list(map(lambda a:a*2, [1, 2, 3, 4]))
```

#### max & min
- max(iterable) & min(iterable)은 인수로 반복 가능한 자료형을 입력받아 그 최댓값 / 최솟값을 돌려주는 함수이다. (근데 문자열도 가능하다!)
```python
>>> max("python")
'y'
>>> min("python")
'h'
```

#### oct
- oct(x)는 정수형태의 숫자를 8진수 문자열로 바꾸어 돌려주는 함수이다.
```python
>>> oct(34)
'0o42'
>>> oct(12345)
'0o30071'
```


#### open
- `open(filename, [mode])`은 '파일 이름'과 '읽기 방법'을 입력 받아 파일 객체를 돌려주는 함수이다. 읽기 방법(mode)를 생략하면 기본값인 읽기 전용 모드(r)로 파일 객체를 만들어 돌려준다.

| 모드 | 설명                  |
| ---- | --------------------- |
| w    | 쓰기 모드로 파일 열기 |
| r    | 읽기 모드로 파일 열기 |
| a    | 추가 모드로 파일 열기 |
| b    | 바이너리 모드로 파일 열기 |

- 👉 이때, b는 w, r, a와 함께 사용한다. 

```python
f = open("binary_file", "rb")
```

#### pow
- pow(x, y)는 x의 y제곱한 결과값을 돌려주는 함수이다. 
```python
>>> pow(2, 4)
16
>>> pow(3, 3)
27
```

#### sorted
- sorted(iterable)함수는 입력값을 정렬한 후 그 결과를 리스트로 돌려주는 함수이다. (문자도 가능)
```python
>>> sorted(['a', 'c', 'b'])
['a', 'b', 'c']
>>> sorted("zero")
['e', 'o',' r', 'z']
>>> sorted((3,2,1)) # 튜플을 정렬해서 리스트로 반환
[1, 2, 3]
```

#### zip
- zip(iterable)은 동일 개수로 이루어진 자료형을 묶어주는 역할을 하는 함수이다. 
```python
>>> list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9]))
[(1,4,7), (2,5,8), (3,6,9)]
>>> list(zip("abc", "def"))
[('a', 'd'), ('b', 'e'), ('c', 'f')]
```


### 외장 함수
#### sys
- 명령 행에서 인수 전달하기
```shell
C:/User/home> python test.py abc pey guido
```

```python
# argv_test.py
import sys
print(sys.argv)
```

![](assets/Jump%20to%20Python-18.png)

- 강제로 스크립트 종료하기
```python
>>> sys.exit()
```

- 자신이 만든 모듈 불러와 사용하기
```python
>>> import sys
>>> sys.path
```
![](assets/Jump%20to%20Python-19.png)
- '' 는 현재 디렉터리를 뜻한다.

```python
# path_append.py
import sys
sys.path.append("C:/doit/Mymod")
```

#### pickle
- pickle은 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈이다.
```python
>>> import pickle
>>> f = open("test.txt", 'wb')
>>> data = {1: 'python', 2: 'you need'}
>>> pickle.dump(data, f)
>>> f.close()
```
- 👉 위 예시는 pickle 모듈의 dump 함수를 사용하여 딕셔너리 객체인 data를 그대로 파일에 저장하는 방법을 보여준다. 

```python
>>> import pickle
>>> f = open("test.txt", 'rb')
>>> data = pickle.load(f)
>>> print(data)
{1: 'python', 2: 'you need'}
```
- 👉 위 예시는 pickle.dump로 저장한 파일을 pickle.load를 사용해서 원래 있던 딕셔너리 객체(data) 상태 그대로 불러오는 예이다. 
- ==위 예시들에서는 딕셔너리 객체를 사용했지만, 어떤 자료형이든 저장하고 불러올 수 있다.==

### OS
- OS 모듈은 환경 변수나 디렉터리, 파일 등의 OS 자원을 제어할 수 있게 해주는 모듈이다. 

- 내 시스템의 환경 변수 값을 알고 싶을 때
```python
>>> import sys
>>> os.environ
```

![](assets/Jump%20to%20Python-20.png)

- 이때, 돌려받은 객체가 딕셔너리이기 때문에 다음과 같이 호출 할 수 있다. 
```python
>>> os.evinron['PATH']
```

- 디렉터리 위치 변경하기
```python
>>> os.chdir("C:\WINDOS")
```

- 디렉터리 위치 돌려받기
```python
>>> os.getcwd()
```
- os.getcwd()는 현재 자신의 디렉터리 위치를 돌려준다.

- 시스템 명령어 호출하기
	- 시스템 자체의 프로그램이나 기타 명령어를 파이썬에서 호출할 수도 있다. 
	- os.system("명령어")처럼 사용한다.
```python
>>> os.system("dir")
```

- 실행한 시스템 명령어의 결과값 돌려받기
	- os.popen은 시스템 명령어를 실행한 결과값을 읽기 모드 형태의 파일 객체로 돌려준다.
```python
>>> f = os.popen("dir")
>>> print(f.read()) # 읽어들인 객체의 내용을 보기 위해
```

- 기타 유용한 os 관련 함수

| 함수                | 설명                                                                    |
| ------------------- | ----------------------------------------------------------------------- |
| os.mkdir(디렉터리)  | 디렉터리를 생성한다.                                                    |
| os.rmdir(디렉터리)  | 디렉터리를 삭제한다. <br> (단, 디렉터리가 비어 있어야 삭제가 가능하다.) |
| os.unlink(파일이름) | 파일을 지운다.                                                          |
| os.rename(src, dst) | src라는 이름의 파일을 dst라는 이름으로 바꾼다.                          |


### shutil
- shutil은 파일을 복사해 주는 파이썬 모듈이다. 
- 다음 예시는 src라는 이름의 파일을 dst로 복사하다. 만약 dst가 디렉터리 이름이라면 src라는 파일 이름으로 dst 디렉터리에 복사하고, 동일한 파일 이름이 있을 경우에는 덮어쓴다.
```python
>>> import shutil
>>> shutil.copy("src.txt", "dst.txt")
```


### glob
- 특정 디렉터리에 있는 파일 이름 모두를 알아야 할 때 사용할 수 있다.

- 디렉터리에 있는 파일들을 리스트로 만들기 - glob(pathname)
	- glob 모듈은 디렉터리 안의 파일들을 읽어서 돌려준다. `*, ?` 같은 메타 문자를 써서 원하는 파일만 읽어 들일 수도 있다. 
```python
>>> import glob
>>> glob.glob("c:/doit/mark*")
```
- 👉 위 예시는 C:/doit 디렉터리에 있는 파일 중 이름이 mark로 시작하는 파일들을 모두 찾아서 읽어들이는 예이다. 


### tempfile
- 파일을 임시로 만들어서 사용할 때 유용한 모듈이다. 
- tempfile.mktemp()는 중복되지 않는 임시 파일의 이름을 무작위로 만들어서 돌려준다. 
```python
>>> import tempfile
>>> filename = tempfile.mktemp()
>>> filename
```

- tempfile.TemporaryFile()은 임시 저장 공간으로 사용할 파일 객체를 돌려준다. 이 파일은 기본적으로 바이너리 쓰기 모드(wb)를 갖는다. f.close()가 호출되면 이 파일 객체는 자동으로 사라진다. 
```python
>>> import tempfile
>>> f = tempfile.TemporaryFile()
>>> f.close() # 생성한 임시 파일이 자동으로 삭제됨
```


### time
- time.time
	- time.time은 UTC를 사용하여 현재 시간을 실수 형태로 돌려주는 함수이다. 
	- 1970년 1월 1일 0시 0분 0초를 기준으로 지난 시간을 초 단위로 돌려준다.
```python
>>> import time
>>> time.time()
1685893836.1411939
```

- time.localtime
	- time.localtime은 time.time()이 돌려준 실수 값을 사용해서, 연도, 월, 일 , 시, 분, 초 ... 의 형태로 바꾸어 주는 함수이다. 
```python
>>> time.localtime(time.time())
time.struct_time(tm_year=2023, tm_mon=6, tm_mday=5, tm_hour=0, tm_min=52, tm_sec=1, tm_wday=0, tm_yday=156, tm_isdst=0)
```

- time.asctime
	- 위 time.localtime에 의해 반환된 튜플 형태의 값을 인수로 받아서 날짜와 시간을 알아보기 쉬운 형태로 돌려주는 함수이다.
```python
>>> time.asctime(time.localtime(time.time()))
'Mon Jun  5 00:53:38 2023'
```

- time.ctime
	- time.asctime(time.localtime(time.time()))은 time.ctime()을 사용해 간편하게 표시할 수 있다. 
	- asctime과 다른 점은 ctime은 항상 현재 시간만을 돌려준다.
```python
>>> time.ctime()
'Mon Jun  5 00:55:31 2023'
```

- time.strftime
```python
time.strftime('출력할 형식 포맷 코드', time.localtime(time.time()))
```

| 코드 | 설명                                | 예                |
| ---- | :----------------------------------: | :---------------: |
| %a   | 요일 줄임말                         | Mon               |
| %A   | 요일                                | Monday            |
| %b   | 달 줄일말                           | Jan               |
| %B   | 달                                  | January           |
| %c   | 날짜와 시간을 출력함                | 06/01/01 17:22:21 |
| %d   | 날(day)                             | `[00, 31]`        |
| %H   | 시간(hour): 24시간 출력 형태        | `[00, 23]`        |
| %l   | 시간(hour): 12시간 출력 형태        | `[01, 12]`        |
| %j   | 1년 중 누적 날짜                    | `[001, 366]`      |
| %m   | 달                                  | `[01, 12]`        |
| %M   | 분                                  | `[01, 59]`        |
| %p   | AM or PM                            | AM                |
| %S   | 초                                  | `[01, 61]`        |
| %U   | 1년 중 누적 주: 일요일을 시작으로   | `[01, 53]`        |
| %w   | 숫자로 된 요일                      | `[0(일요일), 6]`  |
| %W   | 1년 중 누적 주- 월요일을 시작으로   | `[01, 53]`        |
| %x   | 현재 설정된 지역에 기반한 날짜 출력 | 06/01/01          |
| %X   | 현재 설정된 지역에 기반한 시간 출력 | 17:22:21          |
| %Y   | 연도 출력                           | 2001              |
| %Z   | 시간대 출력                         | 대한민국 표준시   |
| `%%` | 문자                                | %                 |
| %y   | 세기 부분을 제외한 연도 출력        | 01                |

```python
>>> import time
>>> time.strftime('%x', time.localtime(time.time()))
'05/01/01'
>>> time.strftime('%c', time.localtime(time.time()))
'05/01/01 17:22:21'
```

- time.sleep
	- 이 함수를 사용하여 일정한 시간 간격(n초)을 두고 루프를 실행 할 수 있다. 
```python
# sleep1.py
for i in range(10):
	print(i)
	time.sleep(1) # 실수도 가능하다. time.sleep(0.5)
```


### calendar 
- calendar.calendar(연도)로 사용하면 그해의 전체 달력을 볼 수 있다. 
```python
>>> import calendar
>>> print(calendar.calendar(2015))

>>> calendar.prcal(2015) # 위와 동일한 결과값이 나온다.

>>> calendar.prmonth(2015, 12)
   December 2015
Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6
 7  8  9 10 11 12 13
14 15 16 17 18 19 20
21 22 23 24 25 26 27
28 29 30 31
```

- calendar.weekday
	- calendar.weekday(연도, 월, 일) 함수는 그 날짜에 해당하는 요일 정보를 돌려준다. 
	- 월: 0 ~ 일: 6
```python
>>> calendar.weekday(2015, 12, 31)
3 # 목요일
```


- calendar.monthrange
	- calendar.monthrange(연도, 월)함수는 입력 받은 달의 1일이 무슨 요일인지와 그 달이 며칠까지 있는지를 튜플 형태로 돌려준다. 
```python
>>> calendar.monthrange(2015, 12)
(1, 31) # 15.12.01은 화요일이고, 31일까지 있다. 
```


#### random
- random은 난수를 발생 시키는 모듈이다
- random.random() 은 0.0에서 1.0 사이의 실수 중에서 난수 값을 돌려준다
- random.randint(1, 10) 는 1에서 10 사이의 정수 중에서 난수 값을 돌려준다.
```python
>>> import random
>>> random.random()
0.05884093823005654

>>> random.randint(1,10)
9
```

```python
# random_pop.py
import random
def random_pop(data):
	number = random.randint(0, len(data)-1)
	return data.pop(number)

if __name__ == "__main__":
	data = [1, 2, 3, 4, 5]
	while data: print(random_pop(data))
```

```shell
PS C:\doit> python .\random_pop.py
5
2
1
3
4
```

- 이때, random 모듈의 choice 함수를 이용하여 더 직관적으로 만들 수 있다.
```python
def random_pop(data):
	number = random.choice(data)
	data.remove(number)
	return number
```

- 리스트 항목을 무작위로 섞고 싶을 떄는 random.shuffle 함수를 사용한다.
```python
>>> import random
>>> data = [1, 2, 3, 4, 5]
>>> random.shuffle(data)
>>> data
[5, 1, 3, 4, 2]
```

#### webbrowser
- webbrowser는 자신의 시스템에서 사용하는 기본 웹 브라우저를 자동으로 실행하는 모듈이다. 다음 예제는 웹 브라우저를 자동으로  실행하고 해당 URL인 google.com으로 가게 해준다.
```python
>>> import webbrowser
>>> webbrowser.open("http://google.com")
```
- webbrowser의 open 함수는 웹 브라우저가 이미 실행된 상태라면 입력 주소로 이동하며, 웹 브라우저가 실행되지 않은 상태라면 새로 웹 브라우저를 실행한 후 해당 주소로 이동한다. 

```python
>>> webbrowser.open_new("http://google.com")
```
- open_new 함수는 이미 웹 브라우저가 실행된 상태이더라도 새로운 창으로 해당 주소가 열리게 한다.

```ad-tip
- threading 모듈
	- 컴퓨터에서 동작하고 있는 프로그램을 프로세스라고 한다. 보통 1개의 프로세스는 한 가지 일만 하지만, 스레드를 사용하면 한 프로세스 안에서 2가지 또는 그 이상의 일을 동시에 수행할 수 있다.
```


### 간단한 메모장 만들기
```python
# C:/doit/memo.py
import sys 

option = sys.argv[1]
memo = sys.argv[2]

print(option)
print(memo)
```

![](assets/Jump%20to%20Python-21.png)

- txt 파일에 값 저장하도록 수정하기
```python
# C:/doit/memo.py
import sys 

option = sys.argv[1]

if option == '-a':
	memo = sys.argv[2]
	f = open('memo.txt', 'a')
	f.write(memo)
	f.write('\n')
	f.close()
```
![](assets/Jump%20to%20Python-22.png)

![](assets/Jump%20to%20Python-23.png)

- 메모 파일(txt) 읽도록 수정하기
```python
# C:/doit/memo.py
import sys 

option = sys.argv[1]

if option == '-a':
	memo = sys.argv[2]
	f = open('memo.txt', 'a')
	f.write(memo)
	f.write('\n')
	f.close()
elif option == '-v':
	f = open('memo.txt')
	memo = f.read()
	f.close()
	print(memo)
```

![](assets/Jump%20to%20Python-24.png)

### 하위 디렉터리 검색하기
```python
# C:/doit/sub_dir_search.py

import os

def search(dirname):
	filenames = os.listdir(dirname)
	for filename in filenames:
		full_filename = os.path.join(dirname, filename)
		print(full_filename)

search("C:/")
```

![](assets/Jump%20to%20Python-25.png)

- 파이썬 파일(.py)만 출력하게 수정하기
```python
# C:/doit/sub_dir_search.py

import os

def search(dirname):
	filenames = os.listdir(dirname)
	for filename in filenames:
		full_filename = os.path.join(dirname, filename)
		ext = os.path.splitext(full_filename)[-1]
		if ext == '.py':
			print(full_filename)

search("C:/")
```

- c:/ 하위 디렉터리에 있는 모든 파이썬 파일 이름 출력하기
```python
# C:/doit/sub_dir_search.py

import os

def search(dirname):
	try:
		filenames = os.listdir(dirname)
		for filename in filenames:
			full_filename = os.path.join(dirname, filename)
			if os.path.isdir(full_filename):
				search(full_filename) # 재귀 호출
			else:
				ext = os.path.splitext(full_filename)[-1]
				if ext == '.py':
					print(full_filename)
	except PermissionError: 
	# 접근 권한이 없는 파일 만나도 오류 발생없이 pass
		pass

search("C:/")
```

```ad-tip
- 하위 디렉터리 검색을 쉽게 해주는 os.walk
	- os.walk를 사용하면 위에서 작성한 코드를 보다 간편하게 만들 수 있다. os.walk는 시작 디렉터리부터 시작하여 그 하위 모든 디렉터리를 차례대로 방문하게 해주는 함수이다.
	```python
	import sys

	for (path, dir , files) in os.walk("C:/"):
		for filename in files:
		ext = os.path.splitext(filename)[-1]
		if ext == '.py':
			print("%s%s" % (path, filename))
	```
```


### 정규표현식
- 정규 표현식에서 사용되는 메타문자
```
.^$*+?{}[]\|()
```

#### 문자 클래스 `[]`

- 정규표현식 `[abc]`
	- a, b, c 증 한 개의 문자와 매치

| 문자열 | 매치여부 | 설명                                                                                        |
| ------ | -------- | ------------------------------------------------------------------------------------------- |
| a      | yes      | 'a'는 정규식과 일치하는 'a'가 있으므로 매치                                                 |
| before | yes      | 'before'는 정규식과 일치하는 'b'가 있으므로 매치                                            |
| dude   | no       | 'dude'는 정규식과 일치하는 문자인 a,b,c 중 어느 하나도 포함하고 있지 않으므로 매치되지 않음 |

- 하이픈(`-`)을 이용하면 여러 문자열을 한번에 표시할 수 있다.
```re
[a-c] : a, b, c
[a-zA-Z] : 모든 알파벳
[0-9] : 모든 숫자
```

- `^`은 반대(not)의 의미를 갖는다
	- `[^0-9]` : 숫자가 아닌 문자

#### 자주 사용하는 문자 클래스

| 정규표현식 | 설명                                                                                                    |
| ---------- | ------------------------------------------------------------------------------------------------------- |
| `\d`       | 숫자와 매치, `[0-9]`와 동일한 표현식이다                                                                |
| `\D`       | 숫자가 아닌 것과 매치, `[^0-9]`와 동일한 표현식이다.                                                    |
| `\s`       | whitespace 문자와 매치 `[ \t\n\r\f\v]`와 동일한 표현식.<br> 맨 앞의 빈칸은 공백 문자(space)를 의미한다. |
| `\S`       | whitespace 문자가 아닌 것과 매치, `[^ \t\n\r\f\v]`와 동일한 표현식.                                     |
| `\w`       | 문자+숫자(alphanumeric)와 매치, `[a-zA-Z0-9_]`와 동일한 표현식                                          |
| `\W`       | 문자+숫자(alphanumeric)가 아닌 문자와 매치, `[^a-zA-Z0-9_]`와 동일한 표현식                             |

- whitespace 문자? → space나 tab 처럼 공백을 표현하는 문자
- ==대문자로 사용된 것은 소문자의 반대임을 추측할 수 있다.==

#### Dot(`.`)
- 줄바꿈 문자인 `\n`을 제외한 모든 문자와 매치됨을 의미한다. 
```
a.b 
```
- 👉 a와 b사이에 줄바꿈 문자를 제외한 어떤 문자가 들어가도 모두 매치

- 정규식 `a.b`

| 문자열 | 매치 여부 |
| ------ | --------- |
| aab    | yes       |
| a0b    | yes       |
| abc    | No        |

```
a[.]b
```
- 👉`"a.b"` 문자열과는 매치, `"a0b"`와는 매치되지 않음

#### 반복(`*`)
- `*` 앞의 문자가 **0부터** 무한대로 반복될 수 있다는 의미
```
ca*t
```

| 문자열 | 매치여부 | 설명             |
| ------ | -------- | ---------------- |
| ct     | yes      | ==a가 0회 반복== |
| cat    | yes      | a가 1회 반복     |
| caaat  | yes      | a가 3회 반복     |

#### 반복(`+`)
- `+` 앞의 문자가  **최소 1번이상** 무한대로 반복될 수 있다는 의미
```
ca+t
```

| 문자열 | 매치여부 | 설명             |
| ------ | -------- | :----------------: |
| ct     | No      | ==a가 0회 반복<br>(최소 1회 이상이어야 함)== |
| cat    | yes      | a가 1회 반복     |
| caaat  | yes      | a가 3회 반복     |

#### 반복(`{m,n},?`)
```
ca{2}t # a가 2번 반복되면 매치
ca{2,5}t # a가 2~5번 반복되면 매치

ab?c # ← b가 0~1번 사용되면 매치
```


### 파이썬에서 정규 표현식을 지원하는 re 모듈
- regular expression
```python
improt re
p = re.compile('ab*')
```

#### 정규식을 사용한 문자열 검색
- 이제 컴파일된 패턴 객체를 사용하여 문자열 검색을 수행 할 수 있다. 컴파일 된 패턴 객체는 다음과 같은 4가지 메서드를 제공한다.
	- 패턴이란 정규식을 컴파일한 결과이다.

| 메서드     | 목적                                                                    |
| ---------- | ----------------------------------------------------------------------- |
| match()    | 문자열의 처음부터 정규식과 매치되는지 조사한다.                         |
| search()   | 문자열의 전체를 검색하여 정규식과 매치되는지 조사한다.                  |
| findall()  | 정규식과 매치되는 모든 문자열(substring)을 리스트로 돌려준다.           |
| finditer() | 정규식과 매치되는 모든 문자열(substring)을 반복 가능한 객체로 돌려준다. |

- 👉 match, search는 정규식과 매치될 떄는 match 객체를 돌려주고, 매치되지 않을 때는 None을 돌려준다.

#### 예시

```python
import re
p = compile('[a-z]+')
```

##### match 
- 매치되면 match 객체를, 아닐 경우 None을 돌려준다.
```python
m = p.match("python")
print(m)
```
![](assets/Jump%20to%20Python-26.png)

```python
m = p.match("3 python")
print(m)
```
![](assets/Jump%20to%20Python-27.png)

- 파이썬 정규식 프로그램의 예시
```python
p = re.compile(정규표현식)
m = p.match("조사할 문자열")
if m:
	print('Match found', m.group())
else:
	print('No match')
```


#### search
```python
m = p.search("python")
print(m)
```
![](assets/Jump%20to%20Python-28.png)

```python
m = p.search("3 python")
print(m)
```

![](assets/Jump%20to%20Python-29.png)


#### findall
```python
>>> result = p.findall("life is too short")
>>> print(result)
```

![](assets/Jump%20to%20Python-30.png)

#### finditer
```python
>>> result = p.finditer("life is too short")
>>> print(result)
```
![](assets/Jump%20to%20Python-31.png)

```python
>>> result = p.finditer("life is too short")
>>> for r in result: print(r)
```

![](assets/Jump%20to%20Python-32.png)

#### match 객체의 메서드

| 메서드  | 목적                                                   |
| ------- | ------------------------------------------------------ |
| group() | 매치된 문자열을 돌려준다.                              |
| start() | 매치된 문자열의 시작위치를 돌려준다.                   |
| end()   | 매치된 문자열의 끝 위치를 돌려준다.                    |
| span()  | 매치된 문자열의 (시작, 끝)에 해당하는 튜플을 돌려준다. |

```python
>>> import re
>>> p = re.compile('[a-z]+')
>>> m = p.match("python")
>>> m.group()
'python'
>>> m.start()
0
>>> m.end()
6
>>> m.span()
(0, 6)
```

```python
>>> import re
>>> p = re.compile('[a-z]+')
>>> m = p.match("3 python")
>>> m.group()
'python'
>>> m.start()
2
>>> m.end()
8
>>> m.span()
(2, 8)
```

```ad-tip 
- 모듈 단위로 수행하기
	- 지금까지 우리는 re.compile을 사용하여 컴파일된 패턴 객체로 그 이후의 작업을 수행했다. re 모듈은 이를 조금 더 축약한 형태로 사용할 수 있는 방법을 제공한다. 
	```python
	>>> p = re.compile('[a-z]+')
	>>> m = p.match("python")
	
	###########################
	>>> m = re.match('[a-z]+', "python")
	```
	- 위 예처럼 컴파일과 match 메서드를 한번에 수행할 수 있다. 보통 한 번 만든 패턴 객체를 여러번 사용할 때는 이 방법보다 re.compile을 사용하는 것이 편하다.
```

#### 컴파일 옵션

| 옵션이름   | 약어 | 설명 |
| ---------- | ---- | ---- |
| DOTALL     | S    | dot 문자(`.`)가 줄바꿈 문자를 포함하여 모든 문자와 매치한다.    |
| IGNORECASE | I    | 대/소문자와 관계없이 매치한다.      |
| MULTILINE  | M    |  여러 줄과 매치한다. <br> (`^, $` 메타문자 사용과 관계있는 옵션이다.)    |
| VERVOSE           |  X    | verbose 모드를 사용한다. <br>(정규식을 보기 편하게 만들 수도 있고, 주석들을 사용할 수도 있다.)     |

- 옵션을 사용할 때는 `re.DOTALL` 처럼 전체 옵션 이름을 써도 되고, `re.S` 처럼 약어를 써도 된다.

##### DOTALL, S
- `.`메타 문자는 줄바꿈 문자 (`\n`)을 제외한 모든 문자와 매치되는 규칙이 있다. 만약 `\n` 문자도 포함하여 매치하고 싶다면, re.DOTALL 또는 re.S 옵션을 사용해 정규식을 컴파일 하면 된다. 
```python
>>> import re
>>> p = re.compile('a.b')
>>> m = p.match('a\nb')
>>> print(m)
None

>>> p = re.compile('a.b', re.DOTALL)
>>> m = p.match('a\nb')
>>> print(m)
```
![](assets/Jump%20to%20Python-33.png)

##### IGNORECASE, I
- re.IGNORECASE 또는 re.I 옵션은 대소문자 구별 없이 매치를 수행할 때 사용하는 옵션이다.
```python
>>> p = re.compile('[a-z]', re.I)
>>> p.match('python')
<re.Match object; span=(0, 1), match='p'>
>>> p.match('Python')
<re.Match object; span=(0, 1), match='P'>
>>> p.match("PYTHON")
<re.Match object; span=(0, 1), match='P'>
```
- `[a-z]` 정규식은 소문자만을 의미하지만 re.I 옵션으로 대소문자 구별 없이 매치된다.

##### MULTILINE, M
- re.MULTILINE 또는 re.M 옵션은 메타 문자 `^, $`와 연관된 옵션이다. 
- `^`는 문자열의 처음을, `$`는 문자열의 마지막을 의미한다.
- `^python`은 문자열의 처음은 항상 python 으로 시작해야하고, `python$`은 문자열의 마지막은 항상 python으로 끝나야 매치된다는 의미이다. 

```python
import re
p = re.compile("^python\s\w+")

data = """python one
life is too short
python two
wou need python
python three"""

print(p.findall(data))
```
- `^python\s\w+` 는 python 이라는 문자열로 시작하고, 그 뒤에 whitespace, 그 뒤에 단어가 와야 한다는 의미이다. 

```python
['python one']
```
- 위 스크립트를 실행하면 다음과 같은 결과를 돌려준다. 

- 하지만 `^` 메타 문자를 문자열 전체의 처음이 아니라 각 라인의 처음으로 인식시키고 싶은 경우, 이때 re.MULTILINE 또는 re.M 옵션을 사용한다.

```python
import re
p = re.compile("^python\s\w+", re.MULTILINE)

data = """python one
life is too short
python two
wou need python
python three"""

print(p.findall(data))
```

- 위 스크립트의 실행 결과는 아래와 같다. 
```python
['python one', 'python two', 'python three']
```
- 👉 즉, re.MULTILINE 옵션은 `^, $` 메타문자를 문자열의 각 줄 마다 적용시켜 주는 것이다. 

##### VERBOSE, X
- 복잡한 정규표현식 문법을 가독성이 좋게 나열하여 표현 할 수 있다. 
```python
charref = re.compile(r'&[#](0[0-7]+|[0-9]+|[0-9a-fA-F]+);')
```

```python
charref = re.compile(r"""
&[#]             # start of a numeric entity reference
(
	0[0-7]+      # Octal form
|[0-9]+          # Decimal form
|[0-9a-fA-F]+    # Hexadecimal form
)
;                # trailing semicolon
""", re.VERBOSE)
```

- 위 두 문장은 동일한 기능을 한다. 
- re.VERBOSE 옵션을 사용하면 문자열에 사용된 whitespace는 컴파일할 때 제거된다. ( 단 `[]` 안에 사용한 whitespace는 제외)
- 그리고 줄 단위로 `#` 기호를 사용하여 주석문을 작성할 수 있다. 

#### 백슬래시 문제 
```python
\section
```
- 이라는 표현식은

```python
[\t\n\r\f\v]ection
```
- 이라고 해석이 된다. ←`\s`가 이스케이프 코드  `\t\n\r\f\v`로 해석됨

- 따라서
```python
\\section

p = re.compile('\\section')
```
-  위 처럼 사용해야한다. 

- `\\section` 이라는 문자열을 전달하기 위해선 
```python
p = re.compile('\\\\section')

또는

p = re.compile(r'\\section')
```

- 이처럼 작성해야 한다. 이를 Raw String 규칙이라고 한다. 


#### 메타문자
- 앞에서 살펴본 메타문자 (`+, *, [], {}`)는 매치가 진행될 때 현재 매치되고 있는 문자열의 위치가 변경된다. (***보통 소비된다고 표현함***)
- 이에 반해 문자열을 소비시키지 않는 (zero-width assertions) 문자에 대해 알아 보자

##### `|`
- | 메타 문자는 or 과 동일한 의미로 사용된다.
```python
>>> p = re.compile("Crow|Servo")
>>> m = p.match("CrowHello")
>>> print(m)
<re.Match object; span=(0, 4), match='Crow'>
```

##### `^`
- ^메타 문자는 문자열의 맨 처음과 일치함을 의미한다.
```python
>>> print(re.search('^Life', 'Life is too short'))
<re.Match object; span=(0, 4), match='Life'>
>>> print(re.search('^Life', 'My Life'))
None
```

##### `$`
- $ 메타문자는 문자열의 끝과 매치함을 의미한다. (^ 문자와 반대)
```python
>>> print(re.search('short$', 'Life is too short'))
<re.Match object; span=(12, 17), match='short'>
>>> print(re.search('short$', 'Life is too short, you need python'))
None
```

- ^또는 $ 문자를 메타 문자가 아닌 문자 그 자체로 매치하고 싶은 경우, `[^], [$]` 처럼 사용하거나 `\^, \$`로 사용하면 된다.

##### `\A`
- \A는 문자열의 처름과 매치됨을 의미한다. ^ 메타 문자와 동일한 의미이지만, re.MULTILINE 옵션을 사용할 경우에는 다르게 해석된다. re.MULTILINE 옵션을 사용할 경우 ^은 각 줄의 문자열의 처음과 매치되지만, \A는 줄과 상관없이 전체 문자열의 처음하고만 매치된다. 

##### `\Z`
- \Z 는 문자열의 끝과 매치됨을 의미한다. 이것 역시 \A와 동일하게 re.MULTILINE 옵션을 사용할 경우 $ 메타 문자와는 달리 전체 문자열의 끝과 매치된다.

##### `\b`
- \b란 단어 구분자(word boundary)이다. 보통 단어는 whitespace에 의해 구분된다.
```python
>>> p = re.compile(r'\bclass\b')
>>> print(p.search('no class at all'))
<re.Match object; span=(3, 8), match='class'>
```
- `'\bclass\b'` 정규식은 앞뒤가 whitespace로 구분된 class 라는 단어와 매치됨을 의미한다. 

```python
>>> print(p.search('no declassified algorithm'))
None
>>> print(p.search('one subclass is'))
None
```
- 위 처럼 whitespace로 구분된 단어가 아니면 매치가 되지 않는다.
- \b 자체는 백스페이스를 의미하므로 반드시 `r'\bclass\b'` 처럼 맨 앞에 r을 붙여줘야 한다. (raw string을 의미)

##### `\B`
- \B는 \b와는 반대의 경우다. 즉, whitespace로 구분된 단어가 아닌 경우에만 매치된다. 
```python
>>> p = re.compile(r'\Bclass\B')
>>> print(p.search('no class at all'))
None
>>> print(p.search('no declassified algorithm'))
<re.Match object; span=(5, 10), match='class'>
>>> print(p.search('one subclass is'))
None
```


#### 그루핑
- ABC 문자열이 계속해서 반복되는지 조사하는 정규식을 작성하고 싶다면?
- 이때, 그루핑(Grouping)이 필요하다. 
```python
(ABC)+
```

- 그룹을 만들어 주는 메타 문자가 바로 `()`이다.
```python
>>> p = re.compile('(ABC)+')
>>> m = p.search('ABCABCABC OK?')
>>> print(m)
<re.Match object; span=(0, 9), match='ABCABCABC'>
>>> print(m.group(0))
ABCABCABC
```

```python
>>> p = re.compile(r'\w+\s+\d+[-]\d+[-]\d+')
>>> m = p.search("park 010-1234-1234")
```
- `'\w+\s+\d+[-]\d+[-]\d+'`은 '이름 + " " +전화번호' 형태의 문자열을 찾는 정규식이다. 이렇게 매치된 문자열 중에서 이름만 뽑아내고 싶다면 어떻게 해야 할까? 
- 보통 반복되는 문자열을 찾을 때 그룹을 사용하는데, 그룹을 사용하는 보다 큰 이유는 위에서 볼 수 있듯이 매치된 문자열 중에서 특정 부분의 문자열만 뽑아 내기 위해서인 경우가 더 많다. 

```python
>>> p = re.compile(r'(\w+)\s+\d+[-]\d+[-]\d+')
>>> m = p.search("park 010-1234-1234")
>>> print(m.group(1))
park
```

- 이름에 해당하는 `\w+` 부분을 그룹 `(\w+)` 으로 만들면 match 객체의 group 메서드를 사용하여 그루핑 된 부분의 문자열만 뽑아 낼 수 있다. 
- group 메서드의 인덱스는 다음과 같은 의미를 갖는다. 

| group(인덱스) | 설명                           |
| ------------- | ------------------------------ |
| group(0)      | 매치된 전체 문자열             |
| group(1)      | 첫 번째 그룹에 해당하는 문자열 |
| group(2)      | 두 번째 그룹에 해당하는 문자열 |
| group(n)      | n 번째 그룹에 해당하는 문자열  |

```python
>>> p = re.compile(r'(\w+)\s+(\d+[-]\d+[-]\d+)')
>>> m = p.search("park 010-1234-1234")
>>> print(m.group(2))
010-1234-1234

>>> p = re.compile(r'(\w+)\s+((\d+)[-]\d+[-]\d+)')
>>> m = p.search("park 010-1234-1234")
>>> print(m.group(3))
010
```
- 위의 두번째 예시처럼 그룹을 중첩되게 사용하는 것도 가능하며, 이 경우 바깥쪽부터 시작하여 안쪽으로 들어갈 수록 인덱스가 증가한다. 

###### 그루핑된 문자열 재참조 하기 
- 그룹의 또 하나 좋은 점은 한번 그루핑한 문자열을 재참조(Backreference) 할 수 있다는 점이다. 
```python
>>> p = re.compile(r'(\b\w+)\s+\1')
>>> p.search('Paris in the the spring').group()
'the the'
```
- 정규식 `'(\b\w+)\s+\1'` 은 '(그룹) + " " + 그룹과 동일한 단어'와 매치됨을 의미한다. 이렇게 정규식을 만들게 되면 2개의 동일한 단어를 연속적으로 사용해야만 매치가 된다. 
- 이것을 가능하게 해주는 것이 바로 재참조 메타 문자인 `\1`이다. 
- `\1`은 정규식의 그룹 중 첫번째 그룹을 가리킨다.

##### 그루핑된 문자열에 이름 붙이기 
- 정규식 안에 그룹이 많아진다면, 사용하는데 굉장히 번거로울 것이다. 따라서 그룹을 인덱스가 아닌 이름(Named Group)으로 참조할 수 있게 했다. 
```python
(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)
```

- 참조하는 예시
```python
>>> p = re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")
>>> m = p.search("park 010-1234-1234")
>>> print(m.group("name"))
park
```

- 재참조 하는 예시
```python
>>> p = re.compile(r'(?P<word>\b\w+)\s+(?P=word)')
>>> p.search("Paris in the the spring").group()
'the the'
```
- 👉 재참조 시에는 ***(?P=그룹이름)*** 이라는 확장 구문을 사용해야 한다.


#### 전방 탐색
```python
>>> p = re.compile(".+:")
>>> m = p.search("http://google.com")
>>> print(m.group())
http:
```

- 정규식 ".+:" 과 일치하는 문자열로 http: 를 돌려주었다. 만약 http: 라는 검색 결과에서 :를 제외하고 출력하려면 어떻게 해야 할까? 위 예는 그나마 간단하지만 훨씬 더 복잡한 정규식이어서 그루핑을 추가로 할 수 없다는 조건까지 더해진다면 어떻게 해야할까? 

- 이럴 때 사용할 수 있는 것이 바로 전방 탐색이다. 전방 탐색에는 긍정(Positive)와 부정(Negative)의 2종류가 있고 다음과 같이 표현한다. 

| 정규식    | 종류             | 설명                                                                                            |
| --------- | ---------------- | ----------------------------------------------------------------------------------------------- |
| `(?=...)` | 긍정형 전방 탐색 | ... 에 해당하는 정규식과 매치되어야 하며, <br> 조건이 통과되어도 문자열이 소비되지 않는다.      |
| `(?!...)` | 부정형 전방 탐색 | ... 에 해당하는 정규식과 매치되지 않아야 하며, <br> 조건이 통과되어도 문자열이 소비되지 않는다. |


#### 긍정형 전방탐색
- 긍정형 전방 탐색을 사용하면 http:의 결과를 http로 바꿀 수 있다. 
```python
>>> p = re.compile(".+(?=:)")
>>> m = p.search("http://google.com")
>>> print(m.group())
http
```

- 정규식중 :에 해당하는 부분에 긍정형 전방탐색 기법을 적용하여 (?=:)로 변경하였다. 
- 이렇게 되면 기존 정규식과 검색에서는 동일한 효과를 발휘하지만, :에 해당하는 문자열이 정규식 엔진에 의해 소비되지 않아 (검색에는 포함되지만 검색 결과에는 제외됨) 검색 결과에서는 :이 제거된 후 돌려주는 효과가 있다. 


```python
.*[.].*$
```
- 이 정규식은 '파일 이름 + . + 확장자'를 나타내는 정규식이다. 
	- 이 정규식은 'foo.bar, autoexec.bat, sendmail.cf' 같은 형식의 파일과 매치 될 것이다. 
- 이 정규식에 확장자가 'bat인 파일은 제외해야 한다'는 조건을 추가해 보자. 
```python
.*[.][^b].*$
```
- 이 정규식은 확장자가 b라는 문자로 시작하면 안 된다는 의미이다. 하지만 이 정규식은 'foo.bar'라는 파일 마저 걸러낸다. 

```python
.*[.]([^b]..|.[^a].|..[^t])$
```
- 이 정규식은 | 메타 문자를 사용하여 확장자의 첫번째 문자가 b가 아니거나 두번째 문자가 a가 아니거나 세번째 문자가 t가 아닌 경우를 의미한다. 
- 이 정규식으로는 foo.bar는 제외되지 않고, autoexec.bat 은 제외되지만, sendmail.cf 같은 확장자의 개수가 2개인 케이스는 포함하지 못한다. 

```python
.*[.]([^b].?.?|.[^a]?.?|..?[^t]?)$
```

- 확장자가 2개여도 통과되는 정규식이 만들어졌다. 하지만 정규식은 점점 더 복잡해지고 이해하기 어려워 졌다. 
- 그런데 여기에서 bat 파일 말고 exe 파일도 제외하라는 조건이 추가로 생긴다면 어떻게 될까? 이 모든 조건을 만족하는 정규식을 구현하려면 패턴은 더욱더 복잡해 질 것이다. 

#### 부정형 전방 탐색
- 이런 상황에서 부정형 전방 탐색을 사용할 수 있다. 
```python
.*[.](?!bat$).*$
```
- 확장자가 bat가 아닌 경우에만 통과 된다는 의미이다. bat 문자열이 있는지 조사하는 과정에서 문자열이 소비되지 않으므로 bat가 아니라고 판단되면 그 이후 정규식 매치가 진행된다. 

- exe 역시 제외하라는 조건이 추가되더라도 다음과 같이 간단히 표현할 수 있다.
```python
.*[.](?!bat$|exe$).*$
```


#### 문자열 바꾸기
- sub 메서드를 사용하면 정규식과 매치되는 부분을 다른 문자로 쉽게 바꿀 수 있다. 
```python
>>> p = re.compile('(blue|white|red)')
>>> p.sub('colour', 'blue socks and red shoes')
'colour socks and colour shoes'
```

- sub 메서드의 첫번째 매개변수는 '바꿀 문자열(replacement)'이 되고, 두번째 매개변수는 '대상 문자열'이 된다. 
- 만약, 바꾸는 횟수를 지정하고 싶으면 세번째 매개변수로 count 값을 넘기면 된다.

```python
>>> p.sub('colour', 'blue socks and red shoes', count=1)
'colour socks and red shoes'
```

##### subn
- subn 역시 sub와 동일한 기능을 하지만, 반환 결과를 튜플로 돌려준다는 차이가 있다. 돌려준 첫번째 요소는 변경된 문자열이고, 두번째 요소는 바꾸기가 발생한 횟수이다. 
```python
>>> p = re.compile('(blue|white|red)')
>>> p.subn('colour', 'blue socks and red shoes')
('colour socks and colour shoes', 2)
```

##### sub 메서드 사용할 때 참조 구문 사용하기 
```python
>>> p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
>>> print(p.sub("\g<phone> \g<name>", "park 010-1234-1234"))
010-1234-1234 park
```
- 위 예제는 '\g<그룹이름>'으로 정규식의 그룹 이름을 참조했다. 

```python
>>> p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
>>> print(p.sub("\g<2> \g<1>", "park 010-1234-1234"))
010-1234-1234 park
```
- 참조 번호를 사용해도 동일한 결과를 돌려준다.

##### sub 메서드의 매개변수로 함수 넣기
```python
>>> def hexrepl(match):
	... "Return the hex string for a decimal number"
	... value = int(match.group())
	... return hex(value)

>>> p = re.compile(r'\d+')
>>> p.sub(hexreplm, "Call 65490 for printingm 49152 for user code.")
'Call 0xffd2 for printingm 0xc000 for user code.'
```


#### Greedy vs Non-Greedy
- 정규식에서 Greedy란 어떤 의미일까? 
```python
>>> s = '<html><head><title>Title</title>'
>>> len(s)
32
>>> print(re.match('<.*>', s).span())
(0, 32)
>>> print(re.match('<.*>', s).group())
<html><head><title>Title</title>
```

- `'<.*>'`  정규식의 매치 결과로 `<html>` 문자열을 돌려주기를 기대했을 것이다. 하지만 `*` 메타 문자는 매우 탐욕스러워서 매치할 수 있는 최대한의 문자열인  `<html><head><title>Title</title>` 문자열을 모두 소비해 버렸다. 어떻게 하면 이 탐욕스러움을 제한하고 `<html>` 문자열 까지만 소비하도록 막을 수 있을까> 

- 다음과 같이 non-greedy 문자인 `?`를 사용하면 `*` 의 탐욕을 제한 할 수 있다. 
```python
>>> print(re.match('<.*?>', s).group())
<html>
```
- non-greedy 문자인 `?`는 `*?, +?, ??, {m,n}?` 와 같이 사용할 수 있다. 가능한 가장 최소한의 반복을 수행하도록 도와주는 역할을 한다. 