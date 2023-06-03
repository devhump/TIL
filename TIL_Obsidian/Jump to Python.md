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
