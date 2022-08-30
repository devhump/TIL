# 문제 15-1. 문자의 위치 구하기
# 문자열 word가 주어질 때, 해당 문자열에서 a 의 모든 위치(index)를 출력해주세요.
# find() index() 메서드 사용 금지

# word = 'apple' # 0
# word = 'kiwi' # 
# word = 'HappyHacking' # 1 6
word = 'banana' # 1 3 5

idx = -1 # 'a' 순서 카운팅을 위한 idx

for char in word:

    idx += 1

    if char == 'a':
        print(idx, end=' ')

print()
