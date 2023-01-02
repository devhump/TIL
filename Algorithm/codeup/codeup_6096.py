# import sys
# from pprint import pprint

# sys.stdin = open("codeup_6096_input.txt", "r")

matrix = []
for i in range(19):
  matrix.append(list(map(int, input().split())))
# pprint(matrix)

cnt = int(input())

position = []
for i in range(cnt):
  position.append(list(map(int, input().split())))

# print(cnt, position)

for i in range(cnt):
  for j in range(19):
    if matrix[position[i][0]-1][j] == 1:
      matrix[position[i][0]-1][j] = 0
    else:
      matrix[position[i][0]-1][j] = 1

    if matrix[j][position[i][1]-1] == 1:
      matrix[j][position[i][1]-1] = 0
    else:
      matrix[j][position[i][1]-1] = 1

for i in range(19):
  print(*matrix[i])