# BOJ_15953 상금헌터

# ! 시간 초과도 아니고, 왜 자꾸 에러가 뜨는지 모르겠다 알림.
# ? elif 절 조건문이 안 먹히나 해서 수정,
# ? str으로 출력해서 그런가 또 수정
# ? 왜 틀린지 이해가 안되서 1시간 반 잡고있다가 포기.


import sys
sys.stdin = open("BOJ_15953_input.txt", "r")

T = int(input())

for t in range(T):
    rank = list(map(int, input().split()))

    result = 0

    if rank[0] == 1:
        result += 500
    elif rank[0] <= 3:
        result += 300
    elif rank[0] <= 6:
        result += 200
    elif rank[0] <= 10:
        result += 50
    elif rank[0] <= 15:
        result += 30
    elif rank[0] <= 21:
        result += 10
    else:
        result += 0

    if rank[1] == 1:
        result += 512
    elif 1 < rank[1] <= 3:
        result += 256
    elif 3 < rank[1] <= 7:
        result += 128
    elif 7 < rank[1] <= 15:
        result += 64
    elif 15 < rank[1] <= 31:
        result += 32
    else:
        result += 0

    # cutline = 0
    # for i in range(5):
    #     cutline += 2**i
    #     # print(cutline, int(512//((2**i))))
    #     if rank[1] <= cutline:
    #         result += int(512//((2**i)))
    #         break

    print(str(result)+'0000')



# ! 인터넷에서 찾은 정답 코드인데, 뭐가 다르지...
# t = int(input())

# def fastival1(score):
#     if score == 1:
#         return 5000000
#     elif 1 < score <= 3:
#         return 3000000
#     elif 3 < score <= 6:
#         return 2000000
#     elif 6 < score <= 10:
#         return 500000
#     elif 10 < score <= 15:
#         return 300000
#     elif 15 < score <= 21:
#         return 100000
#     else:
#         return 0
# def fastival2(score):
#     if score == 1:
#         return 5120000
#     elif 1 < score <= 3:
#         return 2560000
#     elif 3 < score <= 7:
#         return 1280000
#     elif 7 < score <= 15:
#         return 640000
#     elif 15 < score <= 31:
#         return 320000
#     else:
#         return 0
# for _ in range(t):
#     first, second = map(int, input().split(' '))
#     print(fastival1(first) + fastival2(second))