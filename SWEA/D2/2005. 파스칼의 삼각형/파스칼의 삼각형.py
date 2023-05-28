T = int(input())

for t in range(T):
    N = int(input())

    pascal = [[1], [1, 1]]

    for i in range(2, 10):
        temp = [1]
        for j in range(len(pascal[i-1])-1):
            temp.append(pascal[i-1][j]+pascal[i-1][j+1])
        temp.append(1)
        pascal.append(temp)

    print(f'#{t+1}')
    for k in range(N):
        for num in pascal[k]:
            print(num, end=' ')
        print()