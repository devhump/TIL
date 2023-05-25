# SWEA_2001 파리퇴치

import sys
sys.stdin = open('SWEA_2001_input.txt', 'r')

T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    
    matrix = [list(map(int, input().split())) for _ in range(N)]

    W = N-M+1 # 회전 횟수 : 전체 매트릭스-파리채 크기 +1
    # 가령, 5 by 5 평면에 파리채 크기가 2라면, 
    # 5 - 2 + 1 ⇒ 가로 세로 각각 4번씩 회전하며 확인해야 한다.

    def mat_sum(a,b):
        result = 0 
        for i in range(M):
            for j in range(M):
                result += matrix[i+a][j+b] # 시작 지점을 지정해줌
    
        return result

    res = []
    for a in range(W):
        for b in range(W):
            res.append(mat_sum(a,b)) # 해당 좌표를 시작으로 파리채 범위 안의 합을 구함

    print(f'#{t+1} {max(res)}')

            