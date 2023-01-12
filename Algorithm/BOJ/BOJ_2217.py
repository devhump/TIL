# BOJ_2217 로프 / 그리디

import sys

input = sys.stdin.readline

lope_cnt = int(input())

lope_len_list = []
for i in range(lope_cnt):

    temp = int(input())
    lope_len_list.append(temp)

lope_len_list = sorted(lope_len_list)

sum_list = []
while lope_cnt > 0:
    sum_list.append(lope_cnt * lope_len_list[0])
    lope_cnt -= 1
    lope_len_list.pop(0)

print(max(sum_list))

# 처음 통과(python) -> 5636ms
# pypy3로 변경 후  -> 1920ms
# 3~5 번째 줄 추가 후(sys.stdin.readline) -> 1952ms

# 아래는 인터넷에서 찾은 코드(pypy3 기준, 208ms)
#
# cnt = int(input())

# rope = []
# value = []
# for i in range(cnt):
#     rope.append(int(input()))

# rope.sort(reverse=True)

# for i in range(cnt):
#     value.append(rope[i]*(i+1))

# print(max(value))
