T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    
    matrix = [list(map(int, input().split())) for _ in range(N)]

    W = N-M+1 # 

    def mat_sum(a,b):
        result = 0 
        for i in range(M):
            for j in range(M):
                result += matrix[i+a][j+b]
    
        return result

    res = []
    for a in range(W):
        for b in range(W):
            res.append(mat_sum(a,b))

    print(f'#{t+1} {max(res)}')
