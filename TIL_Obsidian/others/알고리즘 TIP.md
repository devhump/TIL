#Algorithm

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
	- [3. 리스트 컴프리헨션 (List Comprehension)](../KDT/Data%20structure/04.%20리스트%20(List).md#3.%20리스트%20컴프리헨션%20(List%20Comprehension))
```python

lecture_list = [list(map(int, input().split())) for _ in range(n)]

```


![](../Algorithm%20(theory)/22.%20다이나믹%20프로그래밍%20-%20문제풀이.md#^de2e19)

##### 최적의 코딩을 결정하는 기본 알고리즘 (by 나동빈)

- 22강 - 문제 4. 금광
	
	![](assets/Pasted%20image%2020230304011822.png)
	- 👉 `15, 16번째줄`로 `9번줄`에서 입력 받은 **1차원 리스트를 2차원으로 변환**
	
	![](assets/Pasted%20image%2020230304012032.png)
	- 👉 마지막 조건문에서 저렇게 한 줄 표현도 가능하다!
	
	![](assets/Pasted%20image%2020230304012119.png)
	
	![](assets/Pasted%20image%2020230304013059.png) ^5fba20