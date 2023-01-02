# import sys
# sys.stdin = open("SWEA_1926_input.txt", "r")

num = int(input())
# num = 100

for i in range(1, num+1):
    cnt = 0
    
    i = list(str(i))

    # 이 코드는 33, 66, 999 코드에 대응 X
    # if '3' in i:
    #     cnt += 1
    # if '6' in i:
    #     cnt += 1
    # if '9' in i:
    #     cnt += 1
    
    cnt += i.count('3')
    cnt += i.count('6')
    cnt += i.count('9')

    if cnt == 3:
        print("---", end=' ')
    if cnt == 2:
        print("--", end=' ')
    elif cnt == 1:
        print("-", end=' ')
    else:
        for j in range(len(i)):
            print(i[j], end='')
        print(end=' ')

    