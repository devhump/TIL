# SWEA_1948. 날짜 계산기

##### 입력
# 3 
# 3 1 3 31
# 5 5 8 15
# 7 17 12 24  
###### 출력
#1 31
#2 103
#3 161

import sys
sys.stdin = open("SWEA_1948_input.txt", "r")

T = int(input())
cnt = 0

month = { 1:31,2:28, 3:31, 4:30, 5:31, 6:30,
 7:31, 8:31, 9:30, 10:31, 11:30, 12:31 }

for t in range(T):
    m1, d1, m2, d2 = map(int, input().split())

    result = 0
    if m1 == m2:
        result = d2 - d1 +1
    else:
        for i in range(m1+1 , m2):
            result += month[i]

        result = result + month[m1] - d1 + d2 + 1
    
    print(f'#{t+1} {result}')