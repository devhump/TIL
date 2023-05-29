T = 10

for t in range(T):

    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]
    
    temp = []

    temp3, temp4 = 0, 0
    for i in range(100):
        temp.append(sum(matrix[i]))
        temp3 += matrix[i][i]
        temp4 += matrix[i][99-i]
    temp.append(temp3)
    temp.append(temp4)

    for i in range(100):
        temp2 = 0
        for j in range(100):
            temp2 += matrix[j][i]
        
        temp.append(temp2)

    print(f'#{t+1} {max(temp)}')
    
