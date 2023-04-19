# BOJ_2669 직사각형 네개의 합집합의 면적 구하기

# 가장 큰 y값, 가장 큰 x값을 구해서, Matrix를 그린다. 
# 거기에 0으로 채워놓고, 각 직사각형의 넓이에 해당하는 부분을 1로 바꾼다.
# Matrix에서 1의 총합을 구한다.  

        
import sys
sys.stdin = open("BOJ_2669_input.txt")

from pprint import pprint

n = 4

rect_li = []
max_x = 0
max_y = 0
for i in range(n):
    rect_li.append(list(map(int, input().split())))

    # 주어지는 행마다 왼쪽 아래 x,y축 오른쪽 위 x,y축 이라면 
    # idx 2번, 3번이 가장 큰 x, y 꼭지점이다. 
    if max_x < rect_li[i][2]:
        max_x = rect_li[i][2]
    if max_y < rect_li[i][3]:
        max_y = rect_li[i][3]

# print(rect_li, max_x, max_y)

matrix = [[0]*max_y for _ in range(max_x)]

for k in range(n):
    for i in range(rect_li[k][0], rect_li[k][2]): # * x축
        for j in range(rect_li[k][1], rect_li[k][3]): # * 축
            matrix[i][j] = 1


# pprint(matrix)

result = 0 
for _ in range(max_x):
    result += sum(matrix[_])

print(result)
