# 매핑을 한 이후에 반대로 출력하는 과정이 인상적이네요 👍
# 다만 뒷부분에서 for문을 for char in str_list: 로 바꾸고
# 조건문들을 char=='b' 처럼 바꾼다면 더 간결하게 바꿀 수 있을 것 같습니다.

# SWEA_10804.문자열의 거울상 #D3

import sys
sys.stdin = open("exam_03_input.txt")

T = int(input())
case_num = 0

for i in range(T):
    case_num += 1
    str_list = input()
    # print(str_list, len(str_list), type(str_list))

    mirror_result = '' # 비어있는 문자열 생성

    for char in str_list: #알파벳만 교체해줌

        if char == "b":
            mirror_result += "d"
        elif char == "d":
            mirror_result += "b"
        elif char == "p":
            mirror_result += "q" 
        elif char == "q":    
            mirror_result += "p"

    print(f"#{case_num} {mirror_result[::-1]}") # 저장된 순서 반대로 출력