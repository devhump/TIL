# word = 'apple'
# word = 'kiwi'

word = 'banana'

idx = -1 # 'a' 순서 카운팅을 위한 idx
# yes_or_no = 0 # 해당 문자열이 'a'를 가지고 있는가 검증

# for char in word:
#     if char == 'a':
#         yes_or_no = 1
#         # a가 있으면 1, a가 없으면 0

for char in word:
    # if yes_or_no == 0:
    #     print(-1)
    #     break
    #     # a가 없는 경우 break

    idx += 1

    if char == 'a':
        print(idx, end=' ')
        # break
        # a가 있는 경우 index 값을 출력
    
# 기존 15번 문제에서 불필요한 부분만 주석 처리 해줬음    
