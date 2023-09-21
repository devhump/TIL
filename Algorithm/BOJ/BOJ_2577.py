# A = int(input())
# B = int(input())
# C = int(input())

A, B, C = 150, 266, 427

num = str(A * B * C) #17037300

num_0_to_9 = str("0123456789")

num_cnt_dict = {}

for char in num_0_to_9:
    num_cnt_dict[char] = num.count(char)

for i in num_0_to_9:
    print(num_cnt_dict[i])

