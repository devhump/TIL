#python 

#### iterable
- (programming) _An object that can be iterated over_
- iterate : perform or utter repeatedly.
- 사전적 의미로 '반복해서 행동하다, 말하다(iterate)' 라는 뜻으로, 프로그래밍 분야에서는 ==반복 가능한 객체==를 뜻한다.
- python에서는 대표적으로 `list, dict, set, string, bytes, tuple, range` 등이 이에 속한다. 

#### iterator
- iterator 객체는 ==값을 차례대로 꺼낼 수 있는 객체==를 말한다.
- iterator는 iterable한 객체를 내장함수 또는 iterable 객체의 메소드로 객체를 생성할 수 있다.
```python
a = [1, 2, 3]
a_iter = iter(a)
print(type(a_iter))
>>> <class 'list_iterator'>
```

- iterable객체는 [매직메소드](https://ziwon.github.io/post/python_magic_methods/) `__iter__`를 가지고 있으며, 이 메소드로 iterator를 만들어 본 예시는 아래와 같다. 
```python
b = {1, 2, 3}
print(dir(b))
>>> ['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
b_iter = b.__iter__()
print(type(b_iter))
>>><class 'set_iterator'>
```

- `a_iter`의 요소를 하나씩 꺼내다 보면, `StopIteration` 라는 에러가 발생한다.
```python
>>> next(a_iter)
1
>>> next(a_iter)
2
>>> next(a_iter)
3
>>> next(a_iter)
# Traceback (most recent call last):
#  File "<pyshell#11>", line 1, in <module>
#    next(a_iter)
# StopIteration
```

- iterator 매직 메소드 'next'를 통해 요소를 나열한 결과는 다음과 같다. 
```python
>>> b_iter.__next__()
1
>>> b_iter.__next__()
2
>>> b_iter.__next__()
3
>>> b_iter.__next__()
# Traceback (most recent call last):
#  File "<pyshell#15>", line 1, in <module>
#    b_iter.__next__()
# StopIteration
```

- 참고: [파이썬 - 기본을 갈고 닦자! / 38. iterable과 iterator](https://wikidocs.net/16068)

---
- REPL (Read-Eval-Print-Loop) 의 약자로, 어플리케이션 실행 상태에서 사용자가 입력한 명령어(소스코드)를 읽고(Read), 명령어를 평가(Eval)하고 결과를 출력(Print)한 다음 다시 입력을 기다리는 상태로 돌아가는 것을 반복(Loop)하는 것, 또는 그러한 특징의 소프트웨어를 말한다. 대표적으로 터미널, 브라우저 콘솔, 파이썬의 IDLE 등이 이에 해당한다. [참조](https://developer-talk.tistory.com/542)