# ASCII 코드로 A 65, a 97 로 대소문자 간에 "32" 차이 존재!


word = 'apple'

word = list(word)

ascii_num = 0
change_num = 0

print(f"origin: {word}")

for i in range(len(word)):
    ascii_num = ord(word[i])
    change_num = ascii_num - 32
    word[i] = chr(change_num)

    #print(word[i], type(word[i]))

print(f"changed: {word}")


# 출력 값 수정요