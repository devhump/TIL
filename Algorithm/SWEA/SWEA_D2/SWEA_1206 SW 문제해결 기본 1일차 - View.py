# SWEA_1206 [S/W 문제해결 기본] 1일차 - View
# * 처음엔 matrix로 풀려다가 답이 안 나올 것 같아서 방법을 바꿨다.


import sys
sys.stdin = open('SWEA_1206_input.txt', 'r')

T = 10

for t in range(1, T+1):

    N = int(input())
    bd = list(map(int, input().split()))
    
    ans = 0
    for i in range(2, N-2):

        # @ 삼항 연산자를 이용해서 좌측, 우측 각각 2개 블럭이내에 큰 건물을 찾는다.
        tmp_L = (bd[i-2] if bd[i-2] > bd[i-1] else bd[i-1]) 
        tmp_R = (bd[i+2] if bd[i+2] > bd[i+1] else bd[i+1])

        # @ 좌우중 한쪽이라도 현재 건물 보다 큰 경우라면 조망권 획득 실패다.
        if (bd[i] - tmp_L) <= 0:
            continue
        if (bd[i] - tmp_R) <= 0:
            continue

        # @ 조금이라도 조망권이 확보된다면, 좌우의 조망 범위 중 작은 쪽을 택한다.
        res = ((bd[i] - tmp_L) if (bd[i] - tmp_L) < (bd[i] - tmp_R) else (bd[i] - tmp_R))
        
        # * 각 건물들의 누적합
        ans += res
    
    print(f'#{t} {ans}')