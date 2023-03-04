#python 

### 올림과 내림 (ceil, floor)
```python
import math

## 올림
math.ceil(-3.14)
>>> -3
math.ceil(3.14)
>>> 4

## 내림
math.floor(3.14)
>>> 3
math.floor(-3.14)
>>>-4

```

#### 내림2 (trunc)
```python
import math

math.trunc(-3.14)
>>> -3
math.floor(-3.14)
>>> -4
```

- `trunc()`함수는 내림을 하더라도 0으로 향하는 반면, `floor()` 함수는 <u>무조건 아래를 향해 내림한다. </u> 참고로 `math.trunc()` 함수는 `int()`와 같은 결과를 반환한다.

```python
import math

int(-3.14)
>>> -3
math.trunc(-3.14)
>>> -3
```


### 반올림 (round)
- `round()` 라는 **내장함수**를 사용한다. 
```python
round(3.1415) # 기본값은 일의 자리까지 나타낸다
>>> 3

round(3.1415, 2) # 인자를 추가하여, 특정 소수점 자리수까지 나타낼 수 있다. 
>>> 3.14

round(31.415, -1) # 인자에는 음수가 올 수 있다. 
>>> 30.0
```

- 사사오입
>	- 반올림할 자리의 수가 5이며, 반올림 할 때 앞자리의 숫자가 짝수면 내림, 홀수면 올림한다. 
```python
round(4.5)
>>> 4
round(3.5)
>>> 4
```


출처:  [핵심만 간단히, Hello World! 파이썬 3 - 12_반올림, 내림, 올림](https://wikidocs.net/21113)