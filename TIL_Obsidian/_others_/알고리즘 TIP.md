---
tags: [Algorithm, syntax]
---

### Input 관련

- txt 형태의 input 값 받기
```python

import sys

sys.stdin = open("BOJ_11047_input.txt", "r")

```

- input 방식 변경하기 (속도가 향상됨)
```python

import sys

input = sys.stdin.readline

```

- 여러 줄의 입력 값 한줄로 처리하기 
	- [3. 리스트 컴프리헨션 (List Comprehension)](../KDT/Data%20structure/04.%20리스트(List).md#3.%20리스트%20컴프리헨션%20(List%20Comprehension))
```python

lecture_list = [list(map(int, input().split())) for _ in range(n)]

```

#### 몇줄일지 모를 때 입력 받기
- 여러 줄 입력 받기
- https://pchild.tistory.com/2

- [readline vs readlines](https://docs.python.org/ko/3/library/io.html?highlight=readlines#io.IOBase.readline)
![](assets/알고리즘%20TIP-1.png)
- (참고) [Python 문법 - 파이썬 입력 받기(sys.stdin.readline)](https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline)
	- 👉 readline에 관한 자세한 설명

```python
# 1. sys 사용하기
import sys 
lines = sys.stdin.readlines() 

for line in lines: 
	A, B = map(int, line.split()) 
	print(A+B)

# 2. EOFError 예외처리
while True:
	try:
		temp += input().rstrip()
	except EOFError:
		break
```


![](../Algorithm%20(theory)/22.%20DP%20-%20problem&solution.md#^de2e19)

### BOJ_2941. 크로아티아 알파벳 (internet)

![](assets/알고리즘%20TIP.png)
- `.replace()` 함수는 생각도 하지 못했다. 그리고, 알파벳 개수만 세면 되는 건데, 계속 원본을 훼손 시키지 않아야 한다고 고집했던 것 같다. 이렇게 또 배워간다.  


##### 최적의 코딩을 결정하는 기본 알고리즘 (by 나동빈)
###### 22강 - 문제 4. 금광
![](assets/알고리즘%20TIP-2.png)
- 👉 `15, 16번째줄`로 `9번줄`에서 입력 받은 **1차원 리스트를 2차원으로 변환**

![](assets/알고리즘%20TIP-3.png)
- 👉 마지막 조건문에서 저렇게 한 줄 표현도 가능하다!

![](assets/알고리즘%20TIP-4.png)

![](assets/알고리즘%20TIP-5.png) ^5fba20