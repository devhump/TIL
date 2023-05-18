# SWEA_1979 어디에 단어가 들어갈 수 있을까


import sys
sys.stdin = open('SWEA_1979_input.txt', 'r')

T = int(input())

def p_print(list):
    for row in list:
        print(row)

for t in range(T):
    
    N, K = map(int, input().split())

    puzzle = [list(map(int, input().split())) for _ in range(N)]

    puzzle90 = [[0] * N for _ in range(N)] # 전치 행렬 만듦
    for i in range(N):
        for j in range(N):
            puzzle90[i][j] = puzzle[j][i]
    
    for i in range(N): # 각 줄의 마지막에 0을 붙여서 마지막임을 표시 
        puzzle[i].append(0)
        puzzle90[i].append(0)

    ans = 0
    for i in range(N):
        oneCnt = 0
        for j in range(N+1):
            
            if puzzle[i][j] == 1:
                oneCnt += 1 # 1이 나오면 계속 카운팅을 함
            else: # 그러다 0이 나오면 
                if oneCnt == K: # 1 연속체가 K 길이인지 확인
                    ans += 1
                oneCnt = 0 # 1 개수 초기화

    for i in range(N):
        oneCnt = 0
        for j in range(N+1):

            if puzzle90[i][j] == 1:
                oneCnt += 1
            else:
                if oneCnt == K:
                    ans += 1
                oneCnt = 0

    print(f'#{t+1} {ans}')


    
