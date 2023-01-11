import sys

input = sys.stdin.readline

coins_num, sum_result = map(int, input().split())

coins_list = []
for i in range(coins_num):
    temp = int(input())

    if temp > sum_result:
        continue
    else:
        coins_list.append(temp)

cnt = 0
while sum_result != 0:

    max_ = coins_list[-1]
    if max_ > sum_result:
        coins_list.pop()
        continue
    else:
        sum_result -= max_
        cnt += 1

print(cnt)
