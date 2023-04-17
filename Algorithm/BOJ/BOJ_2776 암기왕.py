# BOJ_2776 암기왕

import sys
sys.stdin = open("BOJ_2776_input.txt", "r")

# import sys 
# input = sys.stdin.readline

tc = int(input())

for t in range(tc):
    N = int(input())
    note1_dict = {}
    temp_li_1 = list(map(int, input().split()))
    for i in range(N):
        if note1_dict.get(temp_li_1[i], 0):
            note1_dict[temp_li_1[i]] += 1
        else:
            note1_dict[temp_li_1[i]] = 1

    M = int(input())
    temp_li_2 = list(map(int, input().split()))
    for num in temp_li_2:
        if note1_dict.get(num, 0):
            print("1")
        else:
            print("0")

            