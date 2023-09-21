import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")

T = int(input())

case_num = 0
for i in range(T):
    case_num += 1
    num, k = map(int, input().split())

    array_list = []
    for j in range(num):
        array_list.append(list(map(int, input().split())))

    # for row in array_list:
    #     print(row)

    cnt = 0
    cnt_num = 0
    for i in range(num):
        for j in range(num-1):

            if array_list[i][j] == 0:
                cnt = 0
            elif array_list[i][j] == 1 and array_list[i][j+1] == 1:
                cnt += 1
                if cnt == (k-1):
                   cnt_num += 1
                elif cnt > (k-1):
                    cnt_num -= 1
                    cnt = 0
                
    # print(cnt_num)

    cnt = 0
    for i in range(num):
        for j in range(num-1):

            if array_list[j][i] == 0:
                cnt = 0
            elif array_list[j][i] == 1 and array_list[j+1][i] == 1:
                cnt += 1
                if cnt == (k-1):
                   cnt_num += 1
                elif cnt > (k-1):
                    cnt_num -= 1
                    cnt = 0     

            

    print(f"#{case_num} {cnt_num}")
