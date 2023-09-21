# 문제 18.  알파벳 등장 갯수 구하기
# > 문자열 word가 주어질 때, `**Dictionary**`를 활용해서 
# 해당 문자열에서 등장한 모든 알파벳 개수를 구해서 출력하세요.

### Input
# banana
# ### Output
# b 1
# a 3
# n 2

# 각 알파벳의 아스키값 확인
# print(ord('a')) #97
# print(ord('z')) #122 # a~z 25차이
# print(ord("A"), ord("Z")) # 65 , 90

word = 'Banana'
word = list(word)

#a:z 까지를 키값으로 갖는 0인 딕셔너리 생성
az_dic = {}
for i in range(97, 122+1):
    az_dic[chr(i)] = 0

word_2 =''
for char in word:
    if 65 <= ord(char) <= 90: # 각 알파벳이 대문자라면~
        char = chr(ord(char) + 32) # 소문자로 바꿔서
        word_2 += char #소문자를 저장
    else:
        word_2 += char #알파벳 저장

    az_dic[char] += 1 #알파벳별 딕셔너리 값 +1

print(word_2)

for char in word_2:
    if az_dic[char] != 0:
        print(char, az_dic[char]) #각 알바벳별 출력
    
    az_dic[char] = 0 # 한 단어 내 동일한 알바벳 중복 방지를 위해