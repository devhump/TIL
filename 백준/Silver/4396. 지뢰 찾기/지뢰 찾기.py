n = int(input())

mat1 = [list(input()) for _ in range(n)]
mat2 = [list(input()) for _ in range(n)]

mat3 = [[0] * n for _ in range(n)]


dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]
cnt = 0
check = False
for x in range(n):
    for y in range(n):

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if mat1[nx][ny] == "*":
                    mat3[x][y] += 1
                
            if mat1[x][y] == "*" and mat2[x][y] == "x":
                check = True

# pprint(mat1)
# pprint(mat2)
# pprint(mat3)
    
if check:
    for i in range(n):
        for j in range(n):
            if mat1[i][j] == "*":
                print("*", end="")
            elif mat1[i][j] == "." and mat2[i][j] == "x":
                print(mat3[i][j], end="")
            else:
                print('.', end="")
        print()
else:
    for i in range(n):
        for j in range(n):
            if mat2[i][j] == "x":
                print(mat3[i][j], end="")
            else:
                print('.', end="")
        print()
