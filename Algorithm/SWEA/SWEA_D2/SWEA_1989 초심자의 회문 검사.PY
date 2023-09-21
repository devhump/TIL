# SWEA_1989. 초심자의 회문 검사


import sys
sys.stdin = open('SWEA_1989_input.txt', 'r')

import math 
T = int(input())

for t in range(T):
    word = input()
    
    check = True
    for i in range(math.floor(len(word)/2)):
        if word[i] == word[-i-1]:
            pass
        else:
            check = False

    if check:
        print(f'#{t+1} 1')
    else:
        print(f'#{t+1} 0')

# 옛날에 푼 것
# T = int(input())
 
# for i in range(T):
 
#     a = input()
#     b = a[::-1]
 
#     if a == b:
#         print(f"#{i+1} 1")
#     else:
#         print(f"#{i+1} 0")