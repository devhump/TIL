# SWEA_1221. [S/W 문제해결 기본] 5일차 - GNS
# 
import sys
sys.stdin = open('SWEA_1221_input.txt', 'r')

planet = {
    "ZRO" : 0, 
    "ONE" : 1,
    "TWO" : 2,
    "THR" : 3, 
    "FOR" : 4, 
    "FIV" : 5,
    "SIX" : 6,
    "SVN" : 7,
    "EGT" : 8,
    "NIN" : 9
    }
re_planet = {
    0 : "ZRO",
    1 : "ONE",
    2 : "TWO",
    3 : "THR", 
    4 : "FOR", 
    5 : "FIV",
    6 : "SIX",
    7 : "SVN",
    8 : "EGT",
    9 : "NIN"
    }

T = int(input())

for t in range(T):
    a, b = input().split()
    str_num = list(map(str, input().split()))

    temp = []
    for word in str_num:
        temp.append(planet[word])

    temp.sort()

    res = []
    for i in temp:
        res.append(re_planet[i])

    print(f'#{t+1}')
    for i in range(int(b)):
        print(res[i], end=" ")
