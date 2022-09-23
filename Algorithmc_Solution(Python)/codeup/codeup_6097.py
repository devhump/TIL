import sys
from pprint import pprint

sys.stdin = open("codeup_6097_input.txt", "r")

# 격자판의 세로(h), 가로(w), 막대의 개수(n), 각 막대의 길이(l),
# 막대를 놓는 방향(d:가로는 0, 세로는 1)과
# 막대를 놓는 막대의 가장 왼쪽 또는 위쪽의 위치(x, y)

h, w = map(int, input().split())
n = int(input())

matrix = [[0]*w for i in range(h)]

for i in range(n):
	l, d, x, y = map(int, input().split())

	if d == 0: #가로방향
		for j in range(l):
			matrix[x-1][y+j-1] = 1

	if d == 1: #세로방향
		for k in range(l):
			matrix[x+k-1][y-1] = 1

for i in range(h):
	print(*matrix[i])