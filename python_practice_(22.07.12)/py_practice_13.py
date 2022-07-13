# > 주어진 문자열 word가 주어질 때, 
# 해당 단어를 역순으로 뒤집은 결과를 출력하시오.

# ### Input
# apple
# ### Output
# elppa

word = 'abcd'
word = list(word)

len_word = len(word)
# print(int(len_word/2))


if len_word % 2 == 0:

    for i in range(int(len_word/2)):
        temp1 = word[i]
        temp2 = word[-(i+1)]
        print(f"{i+1}번째 temp1 {temp1} temp2 {temp2} (변경전)")

        word[i] = list(temp2)
        word[-(i+1)] = list(temp1)
        print(f"{i+1}번째 temp1 {temp1} temp2 {temp2} (변경후)")

else:
    

print(word, type(word))

# else: