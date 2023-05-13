---
tags: [python, syntax]
---

#### TypeError
> 'int' object is not subscriptable
- 여기서의 'subscriptable'이란 파이썬 내부에서 쓰이는 단어로, **'인덱싱이나 슬라이싱'이 가능한** 이라고 해석하면 된다. 
	- 즉, `int`형 문자열을 쪼개려고 해서 생기는 문제이다.


![](assets/Python%20error.png)

-   TypeError: can only concatenate str (not "int") to str
    
![](assets/Python%20error-1.png)
-   'int' object is not subscriptable
    

![](assets/Python%20error-2.png)
-   list indices must be integers or slices, not str 📌리스트의 인덱스는 문자열이 아닌 정수 여야 한다
    

> 위에서 `buy_list` -> `buy_dict` 변환 과정에서 `buy_dict = []` 를 `buy_dict = {}` 로 바꾸는 걸 깜빡함

![](assets/Python%20error-3.png)
-   Exception has occurred: KeyError
    
    -   📌딕셔너리에 해당하는 키가 없다.
        
![](assets/Python%20error-4.png)
>  'str' object does not support item assignment  
- ==📌 '문자열' 형식은 글자를 수정할 수 없다.==

#### UnboundLocalError
> cannot access local variable 'max_cnt' where it is not associated with a value

![](assets/Python%20error-5.png)
- def 문 외부에 `max_cnt = 0` 설정하고, def 문 내부에서 접근하려고 하니 발생한 에러.
- stackoverflow에 같은 에러로 질문한 사람이 있었다. 

```ad-question
- ["cannot access local variable 'a' where it is not associated with a value", but the value is defined [duplicate]](https://stackoverflow.com/questions/74412503/cannot-access-local-variable-a-where-it-is-not-associated-with-a-value-but)
> I don't know why when `a` is located in `def test()` it can not be found and gives the error. I tried setting `a` as `global a` or using a `nonlocal` modifier on it inside the `def` but it doesn't seem to work. Is there a way I can get it to recognize `a` and run properly?


```python
import keyboard
import time

a = 0

def test():
	a+= 1
	print("The number is now ", a)
	time.sleep(1)

while keyboard.is_pressed('i') == False:
	
	test()

```

- 답변 내용을 정리하자면, 변수의 scope 관련된 건데, 함수내에서 선언된 변수는 접근이 불가능하다. (= 함수 밖에서 선언한 변수는 접근이 가능하다. ) ==단, 접근이 가능한 것이지, 값을 변경(update)하는 것은 불가능 하다.==
- 이를 위해선 `global` 키워드를 사용하면 되지만, 되도록 사용을 자제하고, 함수에 파라미터로 넘기는 것이 좋다. 