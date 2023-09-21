# SWEA_1928. Base64 Decoder

import sys
sys.stdin = open('SWEA_1928_input.txt', 'r')

base_64_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

T = int(input())

for t in range(T):
    temp_str = input()

    long_str = ""
    while temp_str:
        a = base_64_str.index(temp_str[0]) # 인덱스(base64)를 확인한다.
        long_str += bin(a)[2:].zfill(6) # 해당 인덱스 값을 2진수로 바꾸고 
        # 앞 두자리 '0b'는 잘라낸 뒤, 6자리 문자열로 맞춘다. 
        temp_str = temp_str.replace(temp_str[0],"", 1) # 처리된 값 삭제

    ans = ""
    while long_str:
        ans += chr(int(long_str[:8], 2)) # 8자 문자열을 10진수로 변환 후 아스키 코드 매핑
        long_str = long_str.replace(long_str[:8],"", 1) # 처리된 값 삭제
        
    print(f'#{t+1} {ans}')

