# BOJ_2847 게임을 만든 동준이 / 그리디

import sys

sys.stdin = open("BOJ_2847_input.txt", "r")

cnt = int(input())

lv_list = []
for i in range(cnt):
    lv_list.append(int(input()))

minus_cnt = 0
for i in range(1, cnt):

    while lv_list[-i] <= lv_list[-i - 1]:
        lv_list[-i - 1] -= 1
        minus_cnt += 1

print(minus_cnt)

# 입력받은 리스트의 마지막수에서부터 (최대 레벨 경험치)
# 계단식으로 내려오도록 값을 -1씩 감소 시킨다.
# 이 횟수를 모두 더해서 출력
