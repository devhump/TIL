---
tags: [python, syntax]
---

```python
TypeError
'int' object is not subscriptable
```
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
-   'str' object does not support item assignment
    

> 📌 '문자열' 형식은 글자를 수정할 수 없다.