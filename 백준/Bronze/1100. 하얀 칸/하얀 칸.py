import sys

# M x N : 8 x 8 : 체스판

chess_array = []
for i in range(8):
    chess_array.append(input())
# pprint(chess_array)

cnt = 0

for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            if chess_array[i][j] == "F":
                cnt += 1

print(cnt)