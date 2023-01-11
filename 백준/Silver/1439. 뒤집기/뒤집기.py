# BOJ_1439 뒤집기 / 그리디

digit_list = input()

change_cnt = 0
start_sym = digit_list[0]
for i in range(1, len(digit_list)):

    if digit_list[i] == digit_list[i - 1]:
        continue
    else:
        change_cnt += 1

if change_cnt == 2:
    change_cnt /= 2
elif change_cnt > 2:
    if change_cnt % 2 == 0:
        change_cnt /= 2
    else:
        change_cnt /= 2
        change_cnt += 1

print(int(change_cnt))
