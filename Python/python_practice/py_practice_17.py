# 문제 17. 소문자-대문자 변환하기
# 소문자로 구성된 문자열 word가 주어질 때, 모두 대문자로 바꾸어 표현하시오.
# .upper(), .swapcase() 사용 금지
# ASCII 코드로 A 65, a 97 로 대소문자 간에 "32" 차이 존재!

word = 'apple'
word = list(word)

ascii_num = 0
change_num = 0

# print(f"origin: {word}")

for i in range(len(word)):
    ascii_num = ord(word[i])
    change_num = ascii_num - 32
    word[i] = chr(change_num)


#풀이1
word_result = ''
for char in word:
    word_result += char

print(f"changed: {word_result}")

#풀이2
print(''.join(word))
