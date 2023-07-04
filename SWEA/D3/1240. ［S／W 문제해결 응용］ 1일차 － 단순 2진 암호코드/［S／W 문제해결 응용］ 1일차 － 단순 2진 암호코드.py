
T = int(input())

for t in range(T):
    
    r, c = map(int, input().split())
    
    arr = [input() for i in range(r)]
    
    for j in range(r):
        if '1' in arr[j]:
            start = arr[j][::-1].index('1')            
            code = arr[j][c-start-56:c-start]
            break
    # print(code)
    # print(len(code))
    decode = ""
    while code:
        if code[:7] == "0001101":
            decode += "0"
        elif code[:7] == "0011001":
            decode += "1"
        elif code[:7] == "0010011":
            decode += "2"
        elif code[:7] == "0111101":
            decode += "3"
        elif code[:7] == "0100011":
            decode += "4"
        elif code[:7] == "0110001":
            decode += "5"
        elif code[:7] == "0101111":
            decode += "6"
        elif code[:7] == "0111011":
            decode += "7"
        elif code[:7] == "0110111":
            decode += "8"
        elif code[:7] == "0001011":
            decode += "9"
        
        code = code.replace(code[:7], "", 1)

    # print(decode)
    cal_res = 0
    sum_res = 0
    for i in range(8):
        
        if i % 2 == 0:
            cal_res += (int(decode[i]) * 3)
        else:
            cal_res += int(decode[i])

        sum_res += int(decode[i])

    # print(cal_res, sum_res)
    if cal_res % 10 == 0:
        print(f'#{t+1} {sum_res}')
    else:
        print(f'#{t+1} {0}')