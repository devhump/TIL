import sys

sys.stdin = open("_퍼펙트셔플.txt")

T = int(input())

for t in range(T):
    
    card_num = int(input())
    card_list = input().split()

    card_shuffle = []
    if (card_num % 2) == 0: # 전체 카드수가 짝수일 경우
        half = int(card_num/2)
        for i in range(half):
            card_shuffle.append(card_list[i])
            card_shuffle.append(card_list[half+i])
    else:                      # 전체 카드수가 홀수일 경우
        mid_idx = int(card_num//2)
        mid_card = card_list.pop(mid_idx) # 가운데 있는 카드 빼서 값 저장
        # print(mid_card)

        half = int((card_num-1)/2)
        for i in range(half):
            card_shuffle.append(card_list[i])
            card_shuffle.append(card_list[half+i])
        card_shuffle.append(mid_card)  # 가운데 있던 카드 마지막에 저장

        # 자꾸 꼬여서포기
        # pair_A = card_list[:half_B]
        # pair_B = card_list[half_B:] 
        
        # for i in range(half_B):
        #     if (i) % 2 == 0:
        #         card_shuffle.append(pair_A.pop(0))
        #     else:
        #         card_shuffle.append(pair_B.pop(0))

    print(f"#{t+1} ", end = "")
    print(*card_shuffle)