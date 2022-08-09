# BOJ_1264.모음의 개수

import sys
sys.stdin = open("BOJ_1264_input.txt")

# vowel: 모음
vowel = "aeiouAEIOU" #대문자도 포함시켜야함

while True:
    cnt = 0
    str_ = input()
    # print(str_)

    if (str_ == '#'):
        break

    for char in str_:
        if char in vowel:
            cnt += 1

    print(cnt)
