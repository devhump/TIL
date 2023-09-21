# import sys
# # from pprint import pprint

# # sys.stdin = open("codeup_6095_input.txt", 'r')

cnt = int(input())

position = []
for i in range(cnt):
  temp = list(map(int, input().split()))
  position.append(temp)

# # print(position)

matrix = []
for i in range(19):
  a = []  
  matrix.append(a)
  for j in range(19):
    a.append(0)

for i in range(cnt):
  matrix[position[i][0]-1][position[i][1]-1] = 1

for i in range(19):
  print(*matrix[i])

# list_A = [[0]*5 for i in range(5)]
# print(list_A)

