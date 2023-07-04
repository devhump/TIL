# SWEA_1240. [S/W 문제해결 응용] 1일차 - 단순 2진 암호코드
# @ 문제를 이해하는 게 어려웠던 문제
# 여러 배열들 속에 암호문에 숨겨져 있고, 
# 00000000000000
# 00001011010000 <- 101101 이 암호문이 되는 식
# 00001011010000
# 00000000000000
# 이걸 끄집어 내서 다시 디코딩 & 검증을 거치면 된다.

import sys
sys.stdin = open('SWEA_1240_input.txt', 'r')

T = int(input())

for t in range(T):
    
    r, c = map(int, input().split())
    
    arr = [input() for i in range(r)]
    
    for j in range(r):
        if '1' in arr[j]: # 1이 포함되어 있지 않으면 그냥 00000
            start = arr[j][::-1].index('1') # 모든 수(암호문)은 1로 끝나기 때문에 
            code = arr[j][c-start-56:c-start] # 바로 위의 인덱스 -56이 시작하는 인덱스
            # 암호문은 8글자, 각 7자리 2진수 암호문으로 구성 7*8 = 56
            break
    # print(code)
    # print(len(code))
    decode = ""
    while code:
        if code[:7] == "0001101":
            decode += "0"
        elif code[:7] == "0011001":
            decode += "1"
        elif code[:7] == "0010011":
            decode += "2"
        elif code[:7] == "0111101":
            decode += "3"
        elif code[:7] == "0100011":
            decode += "4"
        elif code[:7] == "0110001":
            decode += "5"
        elif code[:7] == "0101111":
            decode += "6"
        elif code[:7] == "0111011":
            decode += "7"
        elif code[:7] == "0110111":
            decode += "8"
        elif code[:7] == "0001011":
            decode += "9"
        
        code = code.replace(code[:7], "", 1) # 암호문 구절에서 7자리 2진수 한자리씩 뽑아주고

    # print(decode)
    cal_res = 0
    sum_res = 0
    for i in range(8):
        
        if i % 2 == 0:
            cal_res += (int(decode[i]) * 3)
        else:
            cal_res += int(decode[i]) # 검산 계산과

        sum_res += int(decode[i]) # 정답 출력을 위한 계산 동시에 진행

    # print(cal_res, sum_res)
    if cal_res % 10 == 0:
        print(f'#{t+1} {sum_res}')
    else:
        print(f'#{t+1} {0}')