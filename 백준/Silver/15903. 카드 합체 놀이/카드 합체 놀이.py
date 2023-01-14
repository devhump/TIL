card_num, cnt = map(int, input().split())

card_list = list(map(int, input().split()))

card_list = sorted(card_list)

for i in range(cnt):

    temp = card_list[0] + card_list[1]

    card_list[0] = temp
    card_list[1] = temp

    card_list = sorted(card_list)

print(sum(card_list))