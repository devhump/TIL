# SWEA_2056 연월일 달력

import sys
sys.stdin = open('SWEA_D1/SWEA_2056_input.txt', 'r')

cal_dict = {
    "01": 31,
    "02": 28,
    "03": 31,
    "04": 30,
    "05": 31,
    "06": 30,
    "07": 31,
    "08": 31,
    "09": 30,
    "10": 31,
    "11": 30,
    "12": 31
    }

T = int(input())

for t in range(T):
    num_str = input()

    mon = num_str[4:6]
    days = int(num_str[6:])
        
    # print(mon, days)
    if 1 <= int(mon) <= 12:
        if 1 <= days <= cal_dict[mon]:
            check = True
        else:
            check = False
    else:
        check = False

    if check == True:
        print(f'#{t+1} {num_str[:4]}/{num_str[4:6]}/{num_str[6:]}')
    else:
        print(f'#{t+1} -1')