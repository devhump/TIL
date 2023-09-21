# 문제 12. 문자열 조작하기
# 주어진 문자열 word가 주어질 때, 
# 해당 단어에서 ‘a’를 모두 제거한 결과를 출력하시오.

#word = input()

######################
# 풀이 1 
######################

# word = 'apple'
# word = list(word)

# cnt = 0

# for i in word:
#     cnt += 1
#     if i == 'a':
#         word[cnt-1] = '' 

# result = ''
# for char in word:
#     result += char

# print(result)

######################
# 풀이 2
######################


word = 'apple'

a = word.replace('a', '')
print(a)
# print(word.replace('a', ''))