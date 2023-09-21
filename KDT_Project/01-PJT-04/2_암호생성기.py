import sys

sys.stdin = open("_암호생성기.txt")

T = 10

for i in range(T):
    case_num = int(input())

    num_list = list(map(int, input().split()))

    # print(num_list)

    while 1:

        for cnt in range(1,6): 
        
            num_list[0] -= cnt
            temp = num_list.pop(0)
        
            # print(temp)
            if temp <= 0:
                temp = 0
                num_list.append(0)
                break
            else:
                num_list.append(temp)

        if temp == 0:
            break
        # print(num_list)
    
    print(f"#{case_num}", end=' ')
    for i in range(8):
        print(f"{num_list[i]}", end=' ')
    print()
