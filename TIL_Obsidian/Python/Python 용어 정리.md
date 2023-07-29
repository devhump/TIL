---
tags: [dictionary, python]
---

- 비슷한 문서 👉 [개발 관련 IT 용어 정리](../IT_SC_Basic/개발%20관련%20IT%20용어%20정리.md)

- [Iterable (이터러블)](https://docs.python.org/ko/3/glossary.html?highlight=mutable#term-iterable)
	- 이터러블은 [`for`](https://docs.python.org/ko/3/reference/compound_stmts.html#for) 루프에 사용될 수 있고, 시퀀스를 필요로 하는 다른 많은 곳 ([`zip()`](https://docs.python.org/ko/3/library/functions.html#zip "zip"), [`map()`](https://docs.python.org/ko/3/library/functions.html#map "map"), …) 에 사용될 수 있습니다. 이터러블 객체가 내장 함수 [`iter()`](https://docs.python.org/ko/3/library/functions.html#iter "iter") 에 인자로 전달되면, 그 객체의 이터레이터를 돌려줍니다. 이 이터레이터는 값들의 집합을 한 번 거치는 동안 유효합니다. 이터러블을 사용할 때, 보통은 [`iter()`](https://docs.python.org/ko/3/library/functions.html#iter "iter") 를 호출하거나, 이터레이터 객체를 직접 다룰 필요는 없습니다. `for` 문은 이것들을 여러분을 대신해서 자동으로 해주는데, 루프를 도는 동안 이터레이터를 잡아둘 이름 없는 변수를 만듭니다. [이터레이터](https://docs.python.org/ko/3/glossary.html?highlight=mutable#term-iterator), [시퀀스](https://docs.python.org/ko/3/glossary.html?highlight=mutable#term-sequence), [제너레이터](https://docs.python.org/ko/3/glossary.html?highlight=mutable#term-generator) 도 보세요.

- [iterator (이터레이터)](https://docs.python.org/ko/3/glossary.html?highlight=mutable#term-iterator)
	- 데이터의 스트림을 표현하는 객체. 이터레이터의 [`__next__()`](https://docs.python.org/ko/3/library/stdtypes.html#iterator.__next__ "iterator.__next__") 메서드를 반복적으로 호출하면 (또는 내장 함수 [`next()`](https://docs.python.org/ko/3/library/functions.html#next "next") 로 전달하면) 스트림에 있는 항목들을 차례대로 돌려줍니다. 더 이상의 데이터가 없을 때는 대신 [`StopIteration`](https://docs.python.org/ko/3/library/exceptions.html#StopIteration "StopIteration") 예외를 일으킵니다. 이 지점에서, 이터레이터 객체는 소진되고, 이후의 모든 `__next__()` 메서드 호출은 [`StopIteration`](https://docs.python.org/ko/3/library/exceptions.html#StopIteration "StopIteration") 예외를 다시 일으키기만 합니다. 이터레이터는 이터레이터 객체 자신을 돌려주는 `__iter__()` 메서드를 가질 것이 요구되기 때문에, 이터레이터는 이터러블이기도 하고 다른 이터러블들을 받아들이는 대부분의 곳에서 사용될 수 있습니다. 중요한 예외는 여러 번의 이터레이션을 시도하는 코드입니다. ([`list`](https://docs.python.org/ko/3/library/stdtypes.html#list "list") 같은) 컨테이너 객체는 [`iter()`](https://docs.python.org/ko/3/library/functions.html#iter "iter") 함수로 전달하거나 [`for`](https://docs.python.org/ko/3/reference/compound_stmts.html#for) 루프에 사용할 때마다 새 이터레이터를 만듭니다. 이런 것을 이터레이터에 대해서 수행하려고 하면, 지난 이터레이션에 사용된 이미 소진된 이터레이터를 돌려줘서, 빈 컨테이너처럼 보이게 만듭니다. [이터레이터 형](https://docs.python.org/ko/3/library/stdtypes.html#typeiter) 에 더 자세한 내용이 있습니다.

- [mutale(가변)](https://docs.python.org/ko/3/glossary.html?highlight=mutable#term-mutable) ^ccf590
	- 가변 객체는 값이 변할 수 있지만 id()는 일정하게 유지합니다.
		- 참고([레벨업 파이썬 - 03) Immutable과 Mutable](https://wikidocs.net/91520))
		- ![파이썬의 기본 데이터 구조](../KDT/Data%20structure/assets/파이썬의%20기본%20데이터%20구조.png)
		
- ↔ [immutable (불변)](https://docs.python.org/ko/3/glossary.html?highlight=mutable#term-immutable) ^a1f954
	- 고정된 값을 갖는 객체. 불변 객체는 숫자, 문자열, 튜플을 포함합니다. 이런 객체들은 변경될 수 없습니다. 새 값을 저장하려면 새 객체를 만들어야 합니다. 변하지 않는 해시값이 있어야 하는 곳에서 중요한 역할을 합니다. 예를 들어, 딕셔너리의 키.

- [id(*object*)](https://docs.python.org/ko/3/library/functions.html#id)
	- 객체의 "아이덴티티"를 돌려준다. 이것은 객체의 수명 동안 유일하고 바뀌지 않음이 보장되는 정수입니다. 수명이 겹치지 않는 두 개의 객체는 같은 id() 값을 가질 수 있습니다. ==This is the address of the object in memory== 

- [sequence (시퀀스)](https://docs.python.org/ko/3/glossary.html?highlight=mutable#term-sequence)
	- `__getitem__()` 특수 메서드를 통해 정수 인덱스를 사용한 빠른 요소 액세스를 지원하고, 시퀀스의 길이를 돌려주는 `__len()__` 메서드를 정의하는 이터러블. 몇몇 내장 시퀀스들을 나열해보면, list, str, tuple, bytes 가 있습니다. dict 또한 `__getitem__()`과 `__len__()`를 지원하지만, 조회에 정수 대신 임의의 불변 키를 사용하기 때문에 시퀀스가 아니라 매핑으로 취급된다는 것에 주의해야 합니다. (기본 시퀀스형: list, tuple, range)

- [lambda (람다)](https://docs.python.org/ko/3/glossary.html?highlight=mutable#term-lambda) ^a3ae25
	- 호출될 때 값이 구해지는 하나의 [표현식](https://docs.python.org/ko/3/glossary.html?highlight=mutable#term-expression) 으로 구성된 이름 없는 인라인 함수. 람다 함수를 만드는 문법은 `lambda [parameters]: expression` 입니다.

- [expression (표현식)](https://docs.python.org/ko/3/glossary.html?highlight=mutable#term-expression)
	- 어떤 값으로 구해질 수 있는 문법적인 조각. 다른 말로 표현하면, 표현식은 리터럴, 이름, 어트리뷰트 액세스, 연산자, 함수들과 같은 값을 돌려주는 표현 요소들을 쌓아 올린 것입니다. 다른 많은 언어와 대조적으로, 모든 언어 구성물들이 표현식인 것은 아닙니다. [`while`](https://docs.python.org/ko/3/reference/compound_stmts.html#while)처럼, 표현식으로 사용할 수 없는 [문장](https://docs.python.org/ko/3/glossary.html?highlight=mutable#term-statement) 들이 있습니다. 대입 또한 문장이고, 표현식이 아닙니다.

- **Comprehension**
	- 영어 단어의 뜻은 **이해(understanding) 또는 포함(inclusion)** 이라는 뜻을 가졌다. 가장 많이 쓰이는 `list comprehension`은 **리스트 내포**라고 번역되곤 한다.
	- 같이 보면 좋은 문서 👉 [파이썬(python) # 23_ 컴프리헨션(Comprehension) 이란?](https://doorbw.tistory.com/174)
	- [list comprehension (리스트 컴프리헨션)](https://docs.python.org/ko/3/glossary.html?highlight=mutable#term-list-comprehension)
		- 시퀀스의 요소들 전부 또는 일부를 처리하고 그 결과를 리스트로 돌려주는 간결한 방법. 
			- `result = ['{:#04x}'.format(x) for x in range(256) if x % 2 == 0]` 는 0에서 255 사이에 있는 짝수들의 16진수 (0x..) 들을 포함하는 문자열의 리스트를 만듭니다. [`if`](https://docs.python.org/ko/3/reference/compound_stmts.html#if) 절은 생략할 수 있습니다. 생략하면, `range(256)`에 있는 모든 요소가 처리됩니다.
	- [set comprehension (집합 컴프리헨션)](https://docs.python.org/ko/3/glossary.html?highlight=mutable#term-set-comprehension)
		- 이터러블에 있는 요소 전체나 일부를 처리하고 결과를 담은 집합을 반환하는 간결한 방법. 
			- `results = {c for c in 'abracadabra' if c not in 'abc'}`는 문자열의 집합 `{'r', 'd'}`를 생성합니다. [리스트, 집합, 딕셔너리의 디스플레이(display)](https://docs.python.org/ko/3/reference/expressions.html#comprehensions)을 참조하십시오.
	- [dictionary comprehension (딕셔너리 컴프리헨션)](https://docs.python.org/ko/3/glossary.html?highlight=mutable#term-dictionary-comprehension)
		- 이터러블에 있는 요소 전체나 일부를 처리하고 결과를 담은 딕셔너리를 반환하는 간결한 방법. 
			- `results = {n: n ** 2 for n in range(10)}`은 값 `n ** 2`에 매핑된 키 `n`을 포함하는 딕셔너리를 생성합니다. [리스트, 집합, 딕셔너리의 디스플레이(display)](https://docs.python.org/ko/3/reference/expressions.html#comprehensions)을 참조하십시오.