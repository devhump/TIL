---
tags: [python, "-"]
---

- 👇유사한 문서들
	- [얕은 복사와 깊은 복사(fin)](얕은%20복사와%20깊은%20복사(fin).md)
	- [copy — 얕은 복사와 깊은 복사 연산](copy%20—%20얕은%20복사와%20깊은%20복사%20연산.md)
	- [얕은 복사(shallow copy)와 깊은 복사(deep copy)](얕은%20복사(shallow%20copy)와%20깊은%20복사(deep%20copy).md)

#python 

파이썬에서 대입문은 객체를 복사하지 않고, 대상과 객체 사이에 바인딩을 만듭니다.가변(mutable) 컬렉션 또는 가변(mutable) 항목들을 포함한 컬렉션의 경우때로 컬렉션을 변경하지 않고 사본을 변경하기 위해 복사가 필요합니다.이 모듈은 일반적인 얕은 복사와 깊은 복사 연산을 제공합니다. (아래 설명 참고)

인터페이스 요약:

`copy.copy(_x_)`
↪  _x_의 얕은 사본을 반환합니다.

`copy.deepcopy(_x_[, _memo_])`
↪ _x_의 깊은 사본을 반환합니다.

_exception_ copy.Error
↪ 모듈 특정 에러의 경우 발생됩니다.

얕은 복사와 깊은 복사의 차이점은 복합 객체(리스트 또는 클래스 인스턴스들과 같은 다른 객체를 포함한 객체)에만 유효합니다.

-   _얕은 복사_는 새로운 복합 객체를 만들고,(가능한 범위까지) 원본 객체를 가리키는 _참조_를 새로운 복합 객체에 삽입합니다.
-   _깊은 복사_는 새로운 복합 객체를 만들고,재귀적으로 원본 객체의 _사본_을 새로 만든 복합 객체에 삽입합니다.
    

깊은 복사 연산은 얕은 복사 연산에는 없는 두 가지 문제가 있습니다:

-   재귀 객체(직접적 또는 간접적으로 자신에 대한 참조를 포함하는 복합 객체)는 순환 루프의 원인이 될 수 있습니다.
-   깊은 복사는 모든 것을 복사하기 때문에, 지나치게 많이 복사할 수 있습니다. 가령, 복사본 간에 공유할 의도가 있는 것까지도.
    

[`deepcopy()`](https://docs.python.org/ko/3/library/copy.html?highlight=mutable#copy.deepcopy "copy.deepcopy") 함수는 다음과 같은 방법으로 이 문제들을 피합니다:

-   현재 복사 패스 중에 이미 복사된 객체의 `memo` 딕셔너리를 가지고 있습니다; 그리고
-   사용자 정의 클래스가 복사 연산 또는 복사된 구성요소 집합을 재정의하도록 합니다.
    
This module does not copy types like module, method, stack trace, stack frame, file, socket, window, or any similar types. It does “copy” functions and classes (shallow and deeply), by returning the original object unchanged; this is compatible with the way these are treated by the [`pickle`](https://docs.python.org/ko/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.") module.

딕셔너리의 얕은 복사는 [`dict.copy()`](https://docs.python.org/ko/3/library/stdtypes.html#dict.copy "dict.copy")를 사용하여 복사할 수 있습니다.그리고 리스트의 얕은 복사는 예를 들어 `copied_list = original_list[:]` 처럼전체 리스트의 슬라이스를 대입하여 리스트를 복사할 수도 있습니다.

클래스는 피클링을 제어하기 위해 사용하는 것과 같은 인터페이스를 사용하여 복사를 제어할 수 있습니다.이러한 메서드들의 정보는 [`pickle`](https://docs.python.org/ko/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.") 모듈 설명을 참고하세요.실제로 [`copy`](https://docs.python.org/ko/3/library/copy.html?highlight=mutable#module-copy "copy: Shallow and deep copy operations.") 모듈은 [`copyreg`](https://docs.python.org/ko/3/library/copyreg.html#module-copyreg "copyreg: Register pickle support functions.") 모듈에 등록된 피클 함수를 사용합니다.

In order for a class to define its own copy implementation, it can define special methods `__copy__()` and `__deepcopy__()`. The former is called to implement the shallow copy operation; no additional arguments are passed. The latter is called to implement the deep copy operation; it is passed one argument, the `memo` dictionary. If the `__deepcopy__()` implementation needs to make a deep copy of a component, it should call the [`deepcopy()`](https://docs.python.org/ko/3/library/copy.html?highlight=mutable#copy.deepcopy "copy.deepcopy") function with the component as first argument and the memo dictionary as second argument. The memo dictionary should be treated as an opaque object.

---
출처: [copy — 얕은 복사와 깊은 복사 연산](https://docs.python.org/ko/3/library/copy.html?highlight=mutable)