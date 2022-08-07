import sys
sys.stdin = open("exam_07_input.txt")

T = 10
case_num = 0

for i in range(T):
    case_num += 1

    A = int(input())
    list_A = input().split()
    B = int(input())
    list_B = input().split("I ")

    new_list_B = []

    for i in range(1, len(list_B)):
        new_list_B.append(list_B[i])


    # print(f"#{case_num}case")
    # print(A)
    # print(len(list_A))
    # print(B)
    # print(len(new_list_B))

    print(f"#{case_num}case")
    print(A)
    print((list_A))
    print(B)
    print((new_list_B))

    # for i in A:
        
