# # BOJ_1744 수묶기 / 그리디
# 틀린 코드

# N = int(input())

# numbers = []
# minus_nums = 0
# zero_cnt = 0
# for i in range(N):
#     temp = int(input())

#     if temp < 0:
#         minus_nums += 1
#     elif temp == 0:
#         zero_cnt += 1

#     numbers.append(temp)

# numbers.sort()

# result = 0
# if minus_nums % 2 == 0:
#     while N > 1:
#         temp1 = numbers.pop()
#         if temp1 == 0:
#             N -= 1
#             continue
#         elif temp1 == 1:
#             result += 1
#             N -= 1
#             continue
#         else:
#             temp2 = numbers.pop()
#             result += temp1 * temp2
#             N -= 2
# else:
#     if 0 in numbers:
#         numbers.pop(minus_nums - 1)
#         while N > 1:
#             temp1 = numbers.pop()
#             if temp1 == 0:
#                 N -= 1
#                 continue
#             elif temp1 == 1:
#                 result += 1
#                 N -= 1
#                 continue
#             else:
#                 temp2 = numbers.pop()
#                 result += temp1 * temp2
#                 N -= 2
#     else:
#         result += numbers.pop(minus_nums - 1)
#         while N > 1:
#             temp1 = numbers.pop()
#             if temp1 == 0:
#                 N -= 1
#                 continue
#             elif temp1 == 1:
#                 result += 1
#                 N -= 1
#                 continue
#             else:
#                 temp2 = numbers.pop()
#                 result += temp1 * temp2
#                 N -= 2
