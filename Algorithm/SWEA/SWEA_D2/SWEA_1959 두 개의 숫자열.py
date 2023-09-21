# BOJ_1959 두 개의 숫자열
#1 30
#2 63
#3 140
#4 181
#5 63
#6 58
#7 22
#8 120
#9 96
#10 70

import sys
sys.stdin = open('SWEA_1959_input.txt', 'r')

T = int(input())

for t in range(T):
    N, M = map(int, input().split())

    N_list = list(map(int, input().split()))
    M_list = list(map(int, input().split()))
    
    if N < M:
        max_sum = 0
        for i in range(M-N+1):
            temp_sum = 0
            for j in range(N):
                temp_sum += N_list[j] * M_list[i+j]
            # print(temp_sum)
            if temp_sum > max_sum:
                max_sum = temp_sum
    elif N > M:
        max_sum = 0
        for i in range(N-M+1):
            temp_sum = 0
            for j in range(M):
                temp_sum += N_list[j+i] * M_list[j]

            if temp_sum > max_sum:
                max_sum = temp_sum
    elif N == M:
            max_sum = 0
            for j in range(N):
                max_sum += N_list[j] * M_list[j]

    print(f'#{t+1} {max_sum}')