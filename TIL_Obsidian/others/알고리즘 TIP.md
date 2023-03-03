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