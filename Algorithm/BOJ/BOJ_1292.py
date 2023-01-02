# 미완
# from pprint import pprint

# # a, b = map(int, input().split())

# a, b = 3, 10

# num = 0
# num_idx = 0
# sum_dict = {}


# while(num_idx <= 1000):
#     num += 1
#     num_idx += num
    
#     sum_dict[num_idx] = num

#     # print(f"num:{num} num_idx:{num_idx}") # 이거 보여주기

# # pprint(sum_dict) # 이것도 보여주기2

# result_a = 0
# result_b = 0
# cnt = 0

# if sum_dict.get(a) == True:
#     result_a += sum_dict[a]
# else:
#     while(sum_dict.get(a) == None):
#         a += 1
#     result_a += sum_dict[a]

# if sum_dict.get(b) == True:
#     result_b += sum_dict[b]
# else:
#     while(sum_dict.get(b) == None):
#         b += 1
#     result_b += sum_dict[b]

# print(result_a, result_b)