import sys
import copy

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