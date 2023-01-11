lope_cnt = int(input())

lope_len_list = []
for i in range(lope_cnt):

    temp = int(input())
    lope_len_list.append(temp)

lope_len_list = sorted(lope_len_list)

sum_list = []
while lope_cnt > 0:
    sum_list.append(lope_cnt * lope_len_list[0])
    lope_cnt -= 1
    lope_len_list.pop(0)

print(max(sum_list))