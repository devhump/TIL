# BOJ_2941 크로아티아 알파벳
croatia = ["dz=", "c=", "c-", "d-", "lj", "nj", "s=", "z="]

while True:
    word = input()
    word_len = len(word)
    cnt = 0

    for char in croatia:
        if (char in word) and (char == "dz="):
            cnt += 1
            word_len -= 3
            print(char, cnt)
        elif char in word:
            cnt += 1
            word_len -= 2
            print(char, cnt)

    print(cnt + word_len)

## 입력 예제가 dz=ak 일 때,
## dz= 한번, z= 로 또 한번 중복 카운팅함
##
## 입력 예제가 c=c= 일 때,
## 한번만 카운팅함
