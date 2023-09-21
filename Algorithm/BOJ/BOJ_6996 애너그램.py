# BOJ_6996 애너그램

import sys
import copy
sys.stdin = open('BOJ_6996_input.txt', 'r')

for _ in range(int(input())):
    str_A, str_B = map(str, input().split())

    copy_B = copy.deepcopy(str_B)

    if len(str_A) != len(str_B):
        print(f"{str_A} & {copy_B} are NOT anagrams.")
    else:
        for char in str_A:
            str_B = str_B.replace(char, "", 1)
        
        if len(str_B) == 0:
            print(f"{str_A} & {copy_B} are anagrams.")
        else:
            print(f"{str_A} & {copy_B} are NOT anagrams.")

# todo 이렇게 쉬운 문제를 몇번이나 틀리는 거야ㅠㅠㅠㅠㅠㅠㅠ
# 처음엔 내가 로직 그렇게 짜두고, str_B 출력 안 되는지도 몰라서, 
# 생각없이 복붙하다가 파일 입력 부분 안 지워서, 
# 마지막에는 마침표(.) 안 찍어서...!!!