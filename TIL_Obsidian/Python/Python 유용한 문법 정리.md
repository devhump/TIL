#python 

#### 논리값 검사
- 모든 객체는 논리값을 검사할 수 있는데, [`if`](https://docs.python.org/ko/3/reference/compound_stmts.html#if) 또는 [`while`](https://docs.python.org/ko/3/reference/compound_stmts.html#while) 조건 또는 다음에 나오는 논리 연산의 피연산자로 사용될 수 있도록 합니다.

-   거짓으로 판명되는 예시
	-   거짓으로 정의된 상수: `None` 과 `False`.
	-   모든 숫자 형들의 영: `0`, `0.0`, `0j`, `Decimal(0)`, `Fraction(0, 1)`
	-   빈 시퀀스와 컬렉션: `''`, `()`, `[]`, `{}`, `set()`, `range(0)`

- 논리값을 돌려주는 연산과 내장 함수는 달리 명시하지 않는 한 항상 거짓의 경우 `0` 이나 `False` 를, 참이면 `1` 이나 `True` 를 돌려줍니다. (중요한 예외: 논리 연산 `or` 와 `and` 는 항상 피연산자 중 하나를 돌려줍니다.)

#### 논리 연산 — `and`, `or`, `not`
- 논리 연산 우선 순위

| 연산자  | 내용                                                                                                                                      |
| ------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `x or y`  | 첫 번째 인자가 거짓일 때만 두 번째의 값을 구합니다.                                                                                       |
| `x and y` | 첫 번째 인자가 참일 때만 두 번째의 값을 구합니다.                                                                                         |
| `not x`   | `not` 은 비논리 연산자들보다 낮은 우선순위를 갖습니다. <br> 그래서, `not a == b` 는 `not (a == b)` 로 해석되고,<br> `a == not b` 는 문법 오류입니다. |


- 비교 연산 8가지( 우선 순위 같음)
![](assets/Pasted%20image%2020230227214624.png)

#### 숫자 형 — [`int`](https://docs.python.org/ko/3/library/functions.html#int), [`float`](https://docs.python.org/ko/3/library/functions.html#float), [`complex`](https://docs.python.org/ko/3/library/functions.html#complex)[¶](https://docs.python.org/ko/3/library/stdtypes.html#numeric-types-int-float-complex)
- 세가지 숫자형
	- 정수 (integers)
	- 실수 (floating point numbers)
	- 복소수 (complex numbers)
   
#####   연산자의 종류
| 연산              | 결과                                          |
|-----------------|---------------------------------------------|
| x + y           | x 와 y 의 합                                   |
| x - y           | x 와 y 의 차                                   |
| x * y           | x 와 y 의 곱                                   |
| x / y           | x 와 y 의 몫                                   |
| x // y          | x 와 y 의 정수로 내림한 몫                           |
| x % y           | x / y 의 나머지                                 |
| -x              | 음의 x                                        |
| `+x`            | x 그대로                                       |
| abs(x)          | x 의 절댓값 또는 크기                              |
| int(x)          | 정수로 변환된 x                                   |
| float(x)        | 실수로 변환된 x                                   |
| complex(re, im) | 실수부 re 와 허수부 im 으로 구성된 복소수. <br>im 의 기본값은 0입니다. |
| c.conjugate()   | 복소수 c 의 켤레                                  |
| divmod(x, y)    | 쌍 (x // y, x % y)                           |
| pow(x, y)       | x 의 y 거듭제곱                                  |
| x ** y          | x 의 y 거듭제곱                                  |

##### 연산자의 우선 순위
- [링크](https://docs.python.org/ko/3/reference/expressions.html#operator-summary)

|                                  연산자                                  | 설명                                                                                           |
|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------- |
| (expressions...),[expressions...], <br>{key: value...}, {expressions...} | 결합(binding) 또는 괄호 친 표현식, <br>리스트 디스플레이, 딕셔너리 디스플레이, 집합 디스플레이 |
|       x[index], x[index:index], <br> x(arguments...), x.attribute        | 서브스크립션, 슬라이싱, 호출, 어트리뷰트 참조                                                  |
|                                 await x                                  | 어웨이트 표현식                                                                                |
|                                    `**`                                    | 거듭제곱                                                                                   |
|                               `+x, -x, ~x`                               | 양, 음, 비트 NOT                                                                               |
|                             `*, @, /, //, %`                             | 곱셈, 행렬 곱셈, 나눗셈, 정수 나눗셈, 나머지                                             |
|                                  `+, -`                                  | 덧셈과 뺄셈                                                                                    |
|                                `<< , >>`                                 | 시프트                                                                                         |
|                                    &                                     | 비트 AND                                                                                       |
|                                    ^                                     | 비트 XOR                                                                                       |
|                        pipe line (enter 위의 키)                         | 비트 OR                                                                                        |
|            in, not in, is, is not, <br> <, <=, >, >=, !=, ==             | 비교, 멤버십 검사와 아이덴티티 검사를 포함합니다                                               |
|                                  not x                                   | 논리 NOT                                                                                       |
|                                   and                                    | 논리 AND                                                                                       |
|                                    or                                    | 논리 OR                                                                                        |
|                                if – else                                 | 조건 표현식                                                                                    |
|                                  lambda                                  | 람다 표현식                                                                                    |
|                                    :=                                    | 대입 표현식                                                                                    |



### 함수
#### Zip()
  - 여러 개의 순회 가능한(iterable) 객체를 인자로 받고, 각 객체가 담고 있는 원소를 튜플 형태로 차례로 접근 할 수 있는 반복자(iterator)를 반환 

```python
#기본 문법
numbers = [1, 2, 3]
letters = ["A", "B", "C"]

for pair in zip(numbers, letters):
	print(pair)

>>>
(1, 'A')
(2, 'B')
(3, 'C')
```

  - 병렬처리 (2개 이상의 데이터 셋 처리)
```python
for num, upper, lower in zip("12345", "ABCDE", "abcde"):
	print(num, upper, lower)
>>>
1 A a
2 B b
3 C c
4 D d
5 E e
```


  - unzip
```python

# zip() 을 이용해 패킹
numbers = (1, 2, 3)
letters = ("A", "B", "C")

pairs = list(zip(numbers, letters))
print(pairs)
>>>
[(1, 'A'), (2, 'B'), (3, 'C')]


# unpacking
numbers, letters = zip(*pairs)
print(numbers) # (1, 2, 3)
print(letters) # ('A','B', 'C')
```

  - 딕셔너리 생성에 활용 가능
```python
keys = [1, 2, 3]
values = ["A", "B", "C"]

A = dict(zip(keys, values))
print(A) # {1: 'A', 2: 'B', 3: 'C'}

```
 


### 삭제 키워드

#### del 
- `del` 은 메서드가 아니라 ***예약어이다.*** 
	- (ex) `if` `for` `or` `and`)
- `del list(a)`
- `del list[3:5]`

```python
int_list = [1, 2, 3, 4, 5, 6, 7]
str_list = ['가','나','다','라','마']

del int_list[0]  # 한개의 요소를 삭제
print(int_list)
[2, 3, 4, 5, 6, 7]

del str_list[3:]  # 여러개의 요소를 삭제
print(str_list)
['가', '나', '다']
```


#### remove()
- 하나의 값만 삭제하는 메서드
- `variable.remove()`

```python
numbers = [1, 2, 2, 3, 3, 3]  
# 숫자가 중복된 리스트
numbers.remove(3)
print(numbers)
>>> [1, 2, 2, 3, 3]  # '첫번째 숫자3' 삭제

# 여러개의 인자값 삭제 (반복문 이용)
numbers = [1, 2, 2, 3, 3, 3]
for _ in numbers :
  numbers.remove(3)
print(numbers)
>>> [1, 2, 2]  # 숫자 3이 전부 삭제
```