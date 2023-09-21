# 문제 16. 모음 등장 여부 확인하기
# > 문자열 word가 주어질 때, 해당 문자열에서 모음의 갯수를 출력하시오. 
# 모음 : a, e, i, o, u `**count()` 사용 금지**

### Input
# apple
### Output
# 2

# word = 'aeiou' # 5
# word = 'zxcvb' # 0

word = 'apple'


################ 최초 풀이

cnt = 0

for char in word:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' :
        cnt += 1

print(cnt)


################## 다시풀기 22.08.25
cnt_2 = 0

for char in word:
    if char in 'aeiou':
        cnt_2 += 1

print(cnt_2)