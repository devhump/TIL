# BOJ_1100. 하얀 칸

from pprint import pprint
import sys
sys.stdin = open("BOJ_1100_input.txt")

# M x N : 8 x 8 : 체스판

chess_array = []
for i in range(8):
    chess_array.append(input())
# pprint(chess_array)

cnt = 0

for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0: # 체스판에서 두 좌표의 합이 짝수면 흑 아니면 백이겠지
            if chess_array[i][j] == "F":
                cnt += 1

print(cnt)