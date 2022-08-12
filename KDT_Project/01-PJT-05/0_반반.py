import sys

sys.stdin = open("_반반.txt")

T = int(input())


yes = "Yes"
no = "No"

for t in range(T):

    str_list = list(input())

    # print(str_list, type(str_list))

    str_list_B = list(set(str_list))

    # print(str_list)

    if len(str_list_B) != 2:
        answer = no
    else:
        len_1 = str_list.count(str_list_B[0])
        len_2 = str_list.count(str_list_B[1])

        if  len_1 == 2 and len_2 == 2:
            answer = yes
        else:
            answer = no

    print(f"#{t+1} {answer}")

