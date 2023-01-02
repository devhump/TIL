#BOJ_1269. 대칭 차집합

import sys
sys.stdin = open("BOJ_1269_input.txt")

A_len, B_len = map(int, input().split())
set_A = list(map(int, input().split()))
set_B = list(map(int, input().split()))

# print(set_num, set_A, set_B, sep='\n')

set_AnB = set(set_A) & set(set_B)

print((A_len+B_len)-(len(set_AnB)*2))