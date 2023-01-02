# BOJ_1110 더하기 사이클

first_num = int(input())  # 26

cnt = 0
while True:

    # 최초 1회만 실행
    if cnt == 0:
        temp_1 = first_num % 10  # 26의 1의 자리, 6
        temp_10 = first_num // 10  # 26의 10의 자리, 2
        cal_1 = (temp_1 + temp_10) % 10  # 1과 10의 자릿수 합의 1의 자리 == 8
        cal_num = (temp_1 * 10) + cal_1  # '6' + '8'
    else:
        temp_1 = cal_num % 10  # 이후 수의 1의 자리수
        temp_10 = cal_num // 10  # 이후 수의 10의 자리수
        cal_1 = (temp_1 + temp_10) % 10  # 앞선 두 자릿 수의 1의 자리
        cal_num = (temp_1 * 10) + cal_1

    # print(temp_1, temp_10)
    # print(first_num, cal_num)
    cnt += 1

    if first_num == cal_num:
        break

print(cnt)
