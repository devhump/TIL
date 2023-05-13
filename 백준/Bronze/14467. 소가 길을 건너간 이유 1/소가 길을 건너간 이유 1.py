cow_check = [2] * 11
cnt = 0
for _ in range(int(input())):
    cow, road = map(int, input().split())
    
    if cow_check[cow] != road:
        if cow_check[cow] == 2:
            cow_check[cow] = road
        else:
            cow_check[cow] = road
            cnt += 1

# print(cow_check)
print(cnt)