
cnt = int(input())

card_dict = {}
for i in range(cnt):

    temp = int(input())
    if card_dict.get(temp, 0):
        card_dict[temp] += 1
    else:
        card_dict[temp] = 1

cards_li = []
for k, v in card_dict.items():
    cards_li.append((k,v))
# print(cards_li)

cards_li.sort(key = lambda x : (x[1], -x[0]))
# print(cards_li)
print(cards_li[-1][0])