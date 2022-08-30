# 문제 14. 문자의 갯수 구하기

> 문자열 word가 주어질 때, 해당 문자열에서 `a` 개수를 구하세요. **`count()` 메서드 사용 금지**

### Input

```
apple
```

### Output

```
1
```

아래의 테스트 케이스로도 확인 해보세요.

```python
banana # 3
kiwi # 0
```

---

# 문제 15. 문자의 위치 구하기

> 문자열 word가 주어질 때, 해당 문자열에서 `a` 가 처음으로 등장하는 위치(index)를 출력해주세요. `a` 가 없는 경우에는 `-1`을 출력해주세요. `**find()` `index()` 메서드 사용 금지**

### Input

```
banana
```

### Output

```python
1
```

아래의 테스트 케이스로도 확인 해보세요.

```python
apple # 0
kiwi # -1
```

# 문제 15 +. 추가 문제

> 문자열 word가 주어질 때, 해당 문자열에서 `a` 의 모든 위치(index)를 출력해주세요. **`find()` `index()` 메서드 사용 금지**

### Input

```
HappyHacking
```

### Output

```
1 6
```

아래의 테스트 케이스로도 확인 해보세요.

```python
banana # 1 3 5
kiwi # 
```







---

# 문제 16. 모음 등장 여부 확인하기

> 문자열 word가 주어질 때, 해당 문자열에서 모음의 갯수를 출력하시오. 모음 : a, e, i, o, u `**count()` 사용 금지**

### Input

```
apple
```

### Output

```
2
```

아래의 테스트 케이스로도 확인 해보세요.

```python
aeiou # 5
zxcvb # 0
```





---

# 문제 17. 소문자-대문자 변환하기

> 소문자로 구성된 문자열 word가 주어질 때, 모두 대문자로 바꾸어 표현하시오. `**.upper()`, `.swapcase()` 사용 금지**

### Input

```
banana
```

### Output

```python
BANANA
```

## 추가 정보

아스키코드는 영문 알파벳을 사용하는 대표적인 문자 인코딩이고, 이후 아스키 기반의 확장 인코딩(유니코드 등)이 등장하게 되었다.

[ASCII - 위키백과, 우리 모두의 백과사전](https://ko.wikipedia.org/wiki/ASCII)

[유니코드 - 위키백과, 우리 모두의 백과사전](https://ko.wikipedia.org/wiki/유니코드)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c8becbe8-9922-4fac-b3ef-2fbeb0f8b209/Untitled.png)

### 파이썬 활용

특정 문자에 대응 되는 유니코드 숫자로 반환하는 함수는 `ord` 이다.

https://docs.python.org/ko/3/library/functions.html#ord

```python
ord('a') 
# 97
```

해당 유니코드 숫자를 문자로 반환하는 함수는 `chr`이다.

https://docs.python.org/ko/3/library/functions.html#chr

```python
chr(97)
# 'a'
```



---

# 문제 18.  알파벳 등장 갯수 구하기

> 문자열 word가 주어질 때, `**Dictionary**`를 활용해서 해당 문자열에서 등장한 모든 알파벳 개수를 구해서 출력하세요.

### Input

```
banana
```

### Output

```python
b 1
a 3
n 2
```



---

# 문제 19. 숫자의 길이 구하기

> 양의 정수 number가 주어질 때, 숫자의 길이를 구하시오. **양의 정수number를 문자열로 변경하는 것은 금지입니다. str() 사용 금지**

### Input

```
123
```

### Output

```
3
```



---

# 문제 20. 각 자릿수의 합 구하기

> 정수 number가 주어질 때, 각 자릿수의 합을 구해서 출력하세요. ****

### Input

```
123
```

### Output

```
6
```



---

# 문제 21. 숫자 뒤집기

> 주어진 숫자를 뒤집은 결과를 출력하시오.

- 문자열이 아닌 숫자로 활용해서 풀어주세요. str() 사용 금지

> 

### Input

```python
1234
```

### Output

```python
4321
```

