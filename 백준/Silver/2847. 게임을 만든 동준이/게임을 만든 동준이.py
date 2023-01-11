cnt = int(input())

lv_list = []
for i in range(cnt):
    lv_list.append(int(input()))

minus_cnt = 0
for i in range(1, cnt):

    while lv_list[-i] <= lv_list[-i - 1]:
        lv_list[-i - 1] -= 1
        minus_cnt += 1

print(minus_cnt)