import sys
from pprint import pprint

sys.stdin = open("codeup_6098_input.txt")

cnt = 10
matrix = [] 
for i in range(cnt):
  matrix.append(list(map(int, input().split())))

x, y = 1, 1
matrix[x][y] = 9

while True:
  
  if matrix[x+1][y] == 1 and matrix[x][y+1] == 1:
    matrix[x][y] = 9
    break
  
  if matrix[x][y+1] == 1:
    x += 1
    if matrix[x][y] == 2:
      matrix[x][y] = 9
      break
    matrix[x][y] = 9
  else:
    y += 1 
    if matrix[x][y] == 2:
      matrix[x][y] = 9
      break
    matrix[x][y] = 9

  # pprint(matrix)
  # print()

for i in range(cnt):
  print(*matrix[i])