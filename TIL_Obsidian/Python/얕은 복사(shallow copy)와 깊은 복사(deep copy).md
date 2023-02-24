## mutable vs immutable
- [mutable 이란?](Python/Python%20용어%20정리.md#^ccf590)
- [immutable 이란?](Python%20용어%20정리#^a1f954)
- 관련 문서
	- [[copy — 얕은 복사와 깊은 복사 연산]]
	- 참고
		- [레벨업 파이썬 - 03) Immutable과 Mutable](https://wikidocs.net/91520)
		- [얕은 복사-깊은 복사 관련 잘 정리된 블로그글1](https://velog.io/@kkamyang/Python-얕은-복사-깊은-복사-shallow-copy-deep-copy)
		- [ ] [얕은 복사-깊은 복사 관련 잘 정리된 블로그글2](https://jinmay.github.io/2019/11/21/python/python-copy-deepcopy/) #todo 

---
### 1 - 1. mutable한 객체
| class |                  설명                  |
|:-----:|:--------------------------------------:|
| list  |    mutable한 순서가 있는 객체 집합     |
|  set  | mutable한 순서가 없는 고유한 객체 집합 |
| dict  | key와 value가 맵핑된 객체, 순서가 없음 |
📌 일반 user가 작성한 class도 대부분 mutable한 객체임


### 1 - 2. immutable한 객체
|   bool    |             참, 거짓              |
|:---------:|:---------------------------------:|
|    int    |               정수                |
|   float   |               실수                |
|   tuple   | immutable한 순서가 있는 객체 집합 |
|    str    |              문자열               |
| frozenset |          immutable한 set          |


### 2- 1. mutable한 객체의 값 변경
1) list의 경우
	- 변수 `a`에 `1, 2, 3`을 원소가 가지는 리스트를 할당해 보자.
	- `id()`는 변수의 메모리 주소값을 리턴해 준다.
	- a의 첫번째 원소를 변경한 후에도 **id값은 변경없이** a의 변수가 변경되었다. 
```python
a = [1, 2, 3]
print(id(a))
>>> 4545429440

a[0] = 5 
print(a)
>>> [5, 2, 3]

print(id(a))
>>> 4545429440 # 기존의 id 주소값과 동일
```

2) set의 경우
	- set에서 `|=` 은 `or` 연산을 의미한다. (합집합)
	- 값은 변경되었으나 **id는 변하지 않는 걸** 확인할 수 있다. 
```python
>>> x = {1,2,3}
>>> x
{1, 2, 3}
>>> id(x)
4544213088
>>> x |= {4,5,6}
>>> x
{1, 2, 3, 4, 5, 6}
>>> id(x)
4544213088
```


### 2 - 2. immutable한 객체의 값 변경
- str의 경우
	- s변수에 첫번째 글자 변경을 시도하면 에러가 발생한다.
		- ==str 타입은 immutable==
	- s에 다른 값을 할당하면, id가 변경되는데, 이는 =='재할당'== 이다.
		👉 **'재할당'** 은 애초에 변수를 다시 할당하는 것으로immutable - mutable과는 다른 문제이다. 
		- (list 또한 값 재할당시 **id가 변경**된다.)
```python
>>> s = 'abc'
>>> s
'abc'
>>> id(s)
4552473552

# 값 변경 시도, 에러 발생
>>> s[0]
'a'
>>> s[0] = 's'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'str' object does not support item assignment

# 값의 재할당
>>> s = 'def'
>>> s
'def'
>>> id(s)
4544259696 # 재할당 결과, id 변경
```


## 변수 간 대입

### 3 - 1. mutable한 객체의 변수 간 대입
- list의 경우
	- b 에 a를 할당하면 **값이 할당되는 것이 아니라 ==같은 메모리 주소를 바라본다.==**
	- <u>b 를 변경하면 a도 같이 바뀐다.</u>
	- **mutable한 다른 객체 또한 같은** 현상이 나타난다.
```python
a = [1, 2, 3]
>>> b = a # shallow copy
>>> b[0] = 5

>>> a
[5, 2, 3]
>>> b
[5, 2, 3]

>>> id(a)
4412210816
>>> id(b)
4412210816
```


### 3-2. immutable한 객체의 변수간 대입
- str 의 경우
	- list의 경우와 동일하게 b를 a에 할당하면 같은 메모리 주소를 바라본다.
	- 하지만, b에 다른 값을 할당하면 재할당이 이루어지며 메모리 주소가 변경된다.
	- 결론적으로 a와 b는 다른 값을 가진다.
```python
>>> a = "abc"
>>> b = a

>>> a
'abc'
>>> b
'abc'

>>> id(a)
4419283920
>>> id(b)
4419283920

>>> b = "abcd" 
>>> a
'abc'
>>> b
'abcd'

>>> id(a)
4419283920
>>> id(b)
4411332528

```

출처 : [파이썬 - 기본을 갈고 닦자! - 12. 얕은 복사(shallow copy)와 깊은 복사(deep copy)](https://wikidocs.net/16038)


