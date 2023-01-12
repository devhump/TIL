# BOJ_11047 동전 0 / 그리디


import sys

sys.stdin = open("BOJ_11047_input.txt", "r")

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

    # max_ = max(conins_list)
    max_ = coins_list[-1]
    if max_ > sum_result:
        coins_list.pop()
        continue
    else:
        sum_result -= max_
        cnt += 1

print(cnt)

# 풀이 자체는 금방 끝냈으나, 계속 시간초과에 걸려서 애를 먹었다.
# readline 코드 (7번줄), pypy3 방식 등
# 통과하기는 했으나, 23번줄 max 구하는 방식과 (288ms)
# 24번줄 인덱싱 이용하는 방법은 시간 차이가 매우 컸다. (2720ms)
