T = 10

for t in range(T):
    N = int(input())

    matrix = [list(input()) for _ in range(100)]
    
    max_cnt = 0
    for i in range(100):    
        for j in range(100, 2, -1):
            for k in range(101-j):
                if matrix[i][k:j+k] == matrix[i][k:j+k][::-1]: 
                    if len(matrix[i][k:j+k]) > max_cnt:
                        max_cnt = len(matrix[i][k:j+k])
                        break
    # @ 좌로 90도 회전해서
    rot_matrix = [[0] * 100 for _ in range(100)]
    for i in range(100):
        for j in range(100):
            rot_matrix[i][j] = matrix[j][100-1-i]

    for i in range(100):    
        for j in range(100, 2, -1):
            for k in range(101-j):
                if rot_matrix[i][k:j+k] == rot_matrix[i][k:j+k][::-1]: 
                    if len(rot_matrix[i][k:j+k]) > max_cnt:
                        max_cnt = len(rot_matrix[i][k:j+k])
                        break
    print(f'#{t+1} {max_cnt}')