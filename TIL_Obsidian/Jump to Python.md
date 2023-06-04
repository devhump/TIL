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