# BOJ_5576 콘테스트

import sys
sys.stdin = open('BOJ_5576_input.txt', 'r')

w_univ = []
for _ in range(10):
    w_univ.append(int(input()))

k_univ = []
for _ in range(10):
    k_univ.append(int(input()))

w_univ.sort()
k_univ.sort()

print(sum(w_univ[-3:]), sum(k_univ[-3:]))