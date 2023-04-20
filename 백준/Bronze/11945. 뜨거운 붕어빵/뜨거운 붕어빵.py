n, m = map(int, input().split())

matrix = [input().split() for _ in range(n)]

for i in range(n):
    for j in range(len(matrix[i])):
        print(matrix[i][j][::-1])