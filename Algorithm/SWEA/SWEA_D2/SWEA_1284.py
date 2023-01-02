# W 리터 사용
# A사 1리터당 요금 P (정액제)
# B사 기본료(Q) R리터 이하의 경우 기본료만!
# 기본료 이상(R리터 기준) 이후 1리터당 S원
# P Q R S W
# 0 1 2 3 4

import sys
sys.stdin = open("SWEA_1284_input.txt", "r")

T = int(input())

fee_A = 0
fee_B = 0
cnt = 0

for i in range(T):
    cnt += 1
    fee_list = map(int, input().split())
    fee_list = list(fee_list)

    fee_A = fee_list[4] * fee_list[0]

    if (fee_list[4] - fee_list[2]) > 0: #기본료 초과
        fee_B += fee_list[1]
        fee_B += (fee_list[4] - fee_list[2])*fee_list[3]
    else:
        fee_B = fee_list[1]
    
    if fee_A > fee_B:
        print(f"#{cnt} {fee_B}")
    else:
        print(f"#{cnt} {fee_A}")
