# SWEA_1970 쉬운 거스름돈
# 50,000 원 0
# 10,000 원 1
# 5,000 원 2 
# 1,000 원 3
# 500 원 4 
# 100 원 5 
# 50 원 6 
# 10 원 7

# ! 시간초과
T = int(input())

for t in range(T):

    won = int(input())

    won_list = [0] * 8
    while won > 0:

        if won >= 50000:
            won -= 50000
            won_list[0] += 1
        elif won >= 10000:
            won -= 10000
            won_list[1] += 1    
        elif won >= 5000:
            won -= 5000
            won_list[2] += 1    
        elif won >= 1000:
            won -= 1000
            won_list[3] += 1    
        elif won >= 500:
            won -= 500
            won_list[4] += 1    
        elif won >= 100:
            won -= 100
            won_list[5] += 1    
        elif won >= 50:
            won -= 50
            won_list[6] += 1    
        elif won >= 10:
            won -= 10
            won_list[7] += 1    

    print(f'#{t+1}')
    for i in range(8):
        print(won_list[i], end=" ")
    print()