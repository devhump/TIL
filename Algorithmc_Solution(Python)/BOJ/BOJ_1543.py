# BOJ_1543. 문서 검색

"""
2, 2, 1, 3
"""
## 시간 초과 (python3, pypy3) 

import sys
sys.stdin = open("BOJ_1543_input.txt")

T = 4

for t in range(T):
    article = list(input())
    word = list(input())

    word_len = len(word)

    cnt = 0 
    while(article): #기본 골자는 article 전체 순회
        # 남은 article 요소 수가 'word' 보다 짧으면 순회 중단
        if len(article) < word_len:
            break

        if article[0] == word[0]:
            if article[0:word_len] == word:
                cnt += 1
                del article[0:word_len]
        else:
            article.pop(0)

    # print(cnt)
    print(f"#{t+1} {cnt}")