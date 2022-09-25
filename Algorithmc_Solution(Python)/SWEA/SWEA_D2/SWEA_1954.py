# SWEA_1954.py 달팽이 숫자

#input
# 2    
# 3   
# 4  

import sys
sys.stdin = open("SWEA_1954_input.txt", "r")


T = int(input())

for t in range(T):
    num = int(input())
    # num = 5

    mx = [[0]*(num+2) for i in range(num+2)]


    for i in range(num+2):
        mx[0][i] = '*'
        mx[i][0] = '*'
        mx[num+1][i] = '*'
        mx[i][num+1] = '*'

    # pprint(mx)

    x, y = 1, 1

    for i in range(1, (num*num)+1):
 
        if mx[x][y-1] != 0 and mx[x-1][y] != 0 and mx[x][y+1] == 0: #왼&위 / 오른쪽
            mx[x][y] = i #오른쪽
            y += 1
        elif mx[x-1][y] != 0 and mx[x][y+1] != 0 and mx[x+1][y] == 0 : #위쪽&오른쪽 / 아래쪽
            mx[x][y] = i #오른쪽
            x += 1
        elif mx[x+1][y] != 0 and mx[x][y+1] != 0 and mx[x][y-1] == 0: #아래&오른쪽 / 왼쪽
            mx[x][y] = i #왼쪽으로
            y -= 1
        elif mx[x][y-1] != 0 and mx[x+1][y] != 0 and mx[x-1][y] == 0: #왼쪽&아래
            mx[x][y] = i #위로
            x -= 1
 
    for i in range(num+2):
        for j in range(num+2):
            if mx[i][j] == 0:
                mx[i][j] = num*num

    print(f'#{t+1}')
    for i in range(1, num+2):
        # if i == 0:
        #     print(f'#{t+1}')
        for j in range(1, num+2):
            if mx[i][j] != '*':
                print(mx[i][j], end=' ')
        if i != num+1:
            print()
        
        
        


