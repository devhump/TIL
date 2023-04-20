# BOJ_1547 공 

import sys
sys.stdin = open("BOJ_1547_input.txt")

cups = [1, 2, 3]

for _ in range(int(input())):
    x, y = map(int, input().split())

    x_pos = cups.index(x)
    y_pos = cups.index(y)

    cups[x_pos], cups[y_pos] = cups[y_pos], cups[x_pos] 

print(cups[0])