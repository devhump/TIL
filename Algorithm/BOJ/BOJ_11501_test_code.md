```python
# BOJ_11501 주식 / 그리디
# 시간초과ㅠㅠ (3중 for문 & max)

import sys

sys.stdin = open("BOJ_11501_input.txt", "r")
# import sys

input = sys.stdin.readline
total_cnt = int(input())

for i in range(total_cnt):
    cnt = int(input())

    price_list = list(map(int, input().split()))

    buy_dict = {}
    for j in range(cnt - 1):

        for num in price_list[j:]:

            if num > price_list[j]:

                buy_dict[j] = price_list[j]

    result = 0
    for key in buy_dict:

        result += max(price_list[key:]) - buy_dict[key]

    print(result)

```

```python
# BOJ_11501 주식 / 그리디
# 시간초과ㅠㅠ (sort 방식으로 변경)

import sys

sys.stdin = open("BOJ_11501_input.txt", "r")
# import sys

input = sys.stdin.readline
total_cnt = int(input())

for i in range(total_cnt):
    cnt = int(input())

    price_list = list(map(int, input().split()))

    buy_dict = {}
    for j in range(cnt - 1):

        sort_A = sorted(price_list[j:])

        if sort_A[-1] > price_list[j]:
            buy_dict[j] = price_list[j]

    result = 0
    for key in buy_dict:

        sort_B = sorted(price_list[key:])
        result += sort_B[-1] - buy_dict[key]

    print(result)

```

```python
# 구조를 더 단순하게 바꿨는데 여전히 시간 초과ㅠㅠ

import sys

input = sys.stdin.readline
total_cnt = int(input())

for i in range(total_cnt):
    cnt = int(input())

    price_list = list(map(int, input().split()))

    result = 0
    for j in range(cnt - 1):

        sort_A = sorted(price_list[j:])

        if sort_A[-1] > price_list[j]:

            result += sort_A[-1] - price_list[j]

    print(result)
```

```python

# BOJ_11501 주식 / 그리디
# 시간초과ㅠㅠ

import sys

sys.stdin = open("BOJ_11501_input.txt", "r")
# import sys

input = sys.stdin.readline
total_cnt = int(input())

for i in range(total_cnt):
    cnt = int(input())

    price_list = list(map(int, input().split()))

    result = 0
    for j in range(cnt - 1):  # 모든 날짜의 주가 확인

        max_ = 0
        for num in price_list[j:]:  # 해당 일 이후의 주가 확인

            if num > max_:  # 가장 큰 값을 갱신해서 저장
                max_ = num

        if max_ != 0:

            result += max_ - price_list[j]  # 순이익분을 저장해서 누적

    print(result)


```
