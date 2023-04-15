# BOJ_14720 딸기 축제
# // 0 딸기 1 초코 2 바나나

num = int(input())
milk_shops = list(map(int, input().split()))


# milks = (0, 1, 2)
cnt  = 0
check = True
next = 0
for i in range(num):
    while milk_shops:

        # 처음 먹는 우유가 딸기 우유인지 확인
        if check:
            if milk_shops[0] == 0:
                milk_shops.pop(0)
                cnt += 1
                check = False
                next = 1
            else:
                milk_shops.pop(0)

        if not check:
            if next == milk_shops[0]:
                cnt += 1
                milk_shops.pop(0)
                next += 1
                if next == 3:
                    next = 0
            else:
                milk_shops.pop(0)

print(cnt) 