# SWEA_1984 중간 평균값 구하기


import sys
sys.stdin = open('SWEA_1984_input.txt', 'r')

T = int(input())

for t in range(T):
    temp = list(map(int, input().split()))

    temp.sort()
    temp = temp[1:9]
    
    print(f'#{t+1} {round(sum(temp)/8)}')
    # ! 문제를 잘 읽자!