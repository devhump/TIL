#미완

import sys
sys.stdin = open("BOJ_1157_input.txt")

T = 4

for i in range(T):

    num_list = []
    #word = list(map(str, input().split())) # 이거는 왜 오류가 났을 까
    
    word = input()
    print(word, type(word), len(word))


    # for i in range(len(word)):
    #     num_list.append(int(ord(word[i])))

    # print(num_list)

    for num in num_list:
        if int(num) > 96: # 97부터 소문자 시작 (a)
            print("실행이 되나??")
            num -= 32 # 대문자-소문자 차이
   
    # print(num_list)

