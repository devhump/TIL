#word = input()
word = 'apple'
word = list(word)

cnt = 0

for i in word:
    cnt += 1

    if i == 'a':
        word[cnt-1] = '' 



word = str(word)

# print(word, type(word))
print(word)

#########################################
# 출력값을 하나의 문자열로 만드는 방법 생각해보기 