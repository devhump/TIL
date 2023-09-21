T = int(input())

def p_print(list):
    for row in list:
        print(row)

for t in range(T):
    
    N, K = map(int, input().split())

    puzzle = [list(map(int, input().split())) for _ in range(N)]

    puzzle90 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            puzzle90[i][j] = puzzle[j][i]
    
    for i in range(N):
        puzzle[i].append(0)
        puzzle90[i].append(0)

    ans = 0
    for i in range(N):
        oneCnt = 0
        for j in range(N+1):
            
            if puzzle[i][j] == 1:
                oneCnt += 1
            else:
                if oneCnt == K:
                    ans += 1
                oneCnt = 0

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