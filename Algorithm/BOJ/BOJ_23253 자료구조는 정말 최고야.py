# BOJ_23253 자료구조는 정말 최고야

import sys
sys.stdin = open("BOJ_23253_input.txt", "r")

# import sys 
# input = sys.stdin.readline

data = list(map(int, input().split()))

book_list = [[] for _ in range(data[1])]

# 입력 파트
for i in range(data[1]):
    temp = int(input())
    temp2 = list(map(int, input().split()))
    
    book_list[i].extend(temp2)

k = 1
cnt = 0
i = 0
while True:

    if book_list[i]:
        if book_list[i][-1] == k:
            book_list[i].pop(-1)
            k += 1
            cnt = 0
    else:
        i += 1
        if i == (data[1]):
            i = 0
    cnt += 1
    if cnt > data[1]:
        break

if book_list:
    print("No")
else:
    print("Yes")
