# BOJ_11652 카드
# * 금방 풀 줄 알았는데...흐미... ㅠㅠ
import sys
sys.stdin = open("BOJ_11652_input.txt", "r")

# import sys 
# input = sys.stdin.readline

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

# for j in range(len(cards_li)-1):
#     if cards_li[j][1] == cards_li[-1][1]: # 최대 개수가 최고 기록이랑 같고
#         if cards_li[j][1] == cards_li[j+1][1]: # 두 카드의 최대 개수가 같으면
#             if cards_li[j][0] > cards_li[j+1][0]: # 카드의 숫자가 작은 것으로 교체 
#                 result = cards_li[j+1][0]
#             else:
#                 result = cards_li[j][0]
        
    
# print(result)