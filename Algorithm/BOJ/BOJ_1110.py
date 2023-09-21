# BOJ_1110 더하기 사이클
# 적재적소에 값의 형변환을 할 수 있는가의 문제

first_num = input()

if len(first_num) == 1:
    first_num = "0" + first_num

cnt = 0
cal_num = 0
while first_num != cal_num:
    # 첫 회차의 경우에만 처음 입력받은 수로 계산 (first_num)
    if cnt == 0:
        temp = int(first_num[0]) + int(first_num[1])

        cnt += 1

        if temp >= 10:
            temp = str(temp)
            temp = temp[1]
        else:
            temp = str(temp)

        cal_num = first_num[1] + temp

        # print(f"{cnt}회차")
        # print(first_num, type(first_num))
        # print(cal_num, type(cal_num))
    # 이후에는 계산되는 수로 계산 (cal_num)
    else:
        temp = int(cal_num[0]) + int(cal_num[1])

        cnt += 1

        if temp >= 10:
            temp = str(temp)
            temp = temp[1]
        else:
            temp = str(temp)

        cal_num = cal_num[1] + temp

        # print(f"{cnt}회차")
        # print(first_num, type(first_num))
        # print(cal_num, type(cal_num))

print(cnt)
