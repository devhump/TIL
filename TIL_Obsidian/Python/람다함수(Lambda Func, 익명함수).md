#python 

>[!note]  목차
> - [람다함수?](#람다함수?)
> - [람다함수의 생성](#람다함수의%20생성)
>- [람다함수 사용 예시](#람다함수%20사용%20예시)

![람다 함수의 정의](Python%20용어%20정리.md#^a3ae25)


### 람다함수?
- 람다함수는 익명 함수라고도 한다. 람다 함수를 사용 하는 이유는 **'코드의 간결함' 과 '메모리의 절약'** 이라고 할 수있다. 
- `def` 키워드를 통해서 함수를 생성하는 방법은 리터럴 표기법에 따른 함수 생성 방법으로, 함수 또한 **'클래스를 통해 생성된 객체 인스턴스'** 이다.
```python
def my_func():
	pass
```

- 위의 함수를 생성자를 통해 생성하는 방법을 간단하게 표현하면, 다음과 같다. 
```python
my_func = function(code, globals[, name[, argdefs[, closure]]])
```

- 코드와 이름을 담아서 함수 클래스를 통해서 객체를 생성하고, 그 객체를 함수이름과 동일한 변수에 담는 과정을 ***`def` 키워드가 대신해준다.***
- 함수 객체를 변수에 담은 시점에서, 함수 객체는 메모리에 올라가서 변수를 통해 자신이 호출되기를 기다리게 되는데, 이과정에서 한번만 실행될 함수라면 **불필요한 메모리가 낭비된다.**

### 람다함수의 생성
- 람다함수는 `lambda` 라는 키워드로 사용할 수 있다. 
![](https://wikidocs.net/images/page/22804/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2018-11-07_05.56.24.png)

- 람다함수는 결과를 `return` 키워드 없이, **자동으로 반환**해준다.
- 또, '익명함수' 라는 이름처럼 `lambda` 함수는 함수의 이름을 지정하지 않는다.
```python
>>> lambda x : x + 1
<function <lambda> at 0x0000018630ECB040>
>>> lambda x : x + 1
<function <lambda> at 0x0000018630ECB160>
>>> lambda x : x + 1
<function <lambda> at 0x0000018630ECB0D0>
# 매번 이름(주소값)이 바뀜 ➡ 익명

>>> (lambda x : x + 1)(3) # 정의와 동시에 사용 가능
4
```

- 물론, 람다함수도 객체이기 때문에 <u>정의와 동시</u>에 변수에 담을 수는 있다.
```python 
>>> func = lambda x : x + 1
>>> func(4)
5
```


### 람다함수 사용 예시
- `sorted` 함수의 경우 `key` 위치 인자에 함수를 보내서, 함수에서 지정한 결과값에 따라서 정렬 할 수 있다. 
- 가령, `target = [' cat ', ' tiger ', ' dog', 'snake ']` 와 같은 리스트가 있을 때, 알파벳 순서가 아니라, 앞뒤 불필요한 공백을 제외한 문자의 길이로 정렬을 하고 싶다면, 정렬의 기준으로 사용할 값을 리턴하는 함수를 생성하여, sorted 함수에 넘겨 줘야 한다.
```python
target = [' cat ', ' tiger ', ' dog', 'snake ']

def my_key(string):
	return len(string.strip())

print(sorted(target, key=my_key))
# ['  cat ', '    dog', ' tiger ', 'snake   '] 
# 글자수가 짧은 순서대로 정렬
```


- 하지만 `my_key` 라는 함수는 이번 정렬만을 위한 함수로, **재사용할 이유가 없다면** `lambda` 함수를 생성해서 넘겨주는 편이 낫다. 

```python
target = [' cat ', ' tiger ', ' dog', 'snake ']
print(sorted(target, key=lambda x : len(x.strip())))
# [' cat ', ' dog', ' tiger ', 'snake ']
# 더 짧은 코드로 동일한 결과!
```

---
출처 : [제대로 파이썬/ A.함수/ 4)람다함수(익명함수)](https://wikidocs.net/22804)
