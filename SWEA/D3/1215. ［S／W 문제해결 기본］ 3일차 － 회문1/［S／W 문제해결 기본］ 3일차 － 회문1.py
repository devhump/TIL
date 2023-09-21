import math

T = 10

for t in range(T):
    N = int(input())

    matrix = [list(input()) for _ in range(8)]
    
    cnt = 0
    for i in range(8):
        for j in range(8-N+1):
            check = True
            for k in range(math.floor(N/2)):
                if matrix[i][j:j+N][k] != matrix[i][j:j+N][-k-1]:
                    check = False
                    continue
            if check:
                cnt += 1
            
            
    rot_matrix = [[0] * 8 for _ in range(8)]
    for i in range(8):
        for j in range(8):
            rot_matrix[i][j] = matrix[j][8-1-i]


    for i in range(8):
        for j in range(8-N+1):        
            check2 = True
            for k in range(math.floor(N/2)):
                if rot_matrix[i][j:j+N][k] != rot_matrix[i][j:j+N][-k-1]:
                    check2 = False
                    continue
            if check2:
                cnt += 1
            


    print(f'#{t+1} {cnt}')