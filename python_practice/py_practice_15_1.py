# 문제 15. 문자의 위치 구하기
# 문자열 word가 주어질 때, 해당 문자열에서 a 가 처음으로 등장하는 위치(index)를 출력해주세요.
# a 가 없는 경우에는 -1을 출력해주세요.
# find() index() 메서드 사용 금지

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
