# BOJ_2897_B

import sys
sys.stdin = open('BOJ_2897_input.txt', 'r')

R, C = map(int, input().split())

mat = []
for _ in range(R):
    mat.append(list(input()))

res = [0, 0, 0, 0, 0]
for x in range(R-1):
    for y in range(C-1):
        temp = [mat[x][y], mat[x][y+1], mat[x+1][y+1], mat[x+1][y]]

        if "#" in temp:
            continue
            # ! 계속 순회가 이상해서 한참 고민했는데, 
            # ! 여기에 break를 써서 루프가 꼬인거였다...
        cnt = temp.count("X")
        res[cnt] += 1

for i in range(5):
    print(res[i])