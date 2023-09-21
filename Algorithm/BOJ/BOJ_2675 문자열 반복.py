# BOJ_2675 문자열 반복

import sys
sys.stdin = open('BOJ_2675_input.txt', 'r')

T = int(input())

for t in range(T):
    n, word = input().split()

    for char in word:
        for i in range(int(n)):
            print(char, end="")
    print()