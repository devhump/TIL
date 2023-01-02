
# import sys
# sys.stdin = open("SWEA_1288_input.txt", "r")

# T = int(input())

# num_add = []
# num_clear = [0,1,2,3,4,5,6,7,8,9]

# for i in range(T):
#     cnt = 0
#     num = int(input())
#     num = list(str(num))
#     num = set(num)

#     # while (len(num_add) < 10): #어차피 0~9 숫자는 10개!
#     while (len(num_add) < 10): #어차피 0~9 숫자는 10개!
#         cnt += 1
#         print(f"while문 내 실행횟수: {cnt}")
#         num_add += num
#         num_add = list(set(num_add))
    
#     print(f"#{T} {cnt}")

#         # for num_char in num:
#         #     if num not in num_add:
#         #         num_add.append(num_char)

#         #         print(f"{cnt}번째 실행")
