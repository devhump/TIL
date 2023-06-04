- [SWEA_1928 Base64 Decoder](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PR4DKAG0DFAUq)문제
- 한참 봐도 무슨 말인지 모르겠다가, 위키에서 [base64](../../IT%20&%20SC%20Basic/base64.md) 내용 찾아 보고 나니까 조금 알 것 같네.

![예시](../../IT%20&%20SC%20Basic/base64.md#예시)

- 위 문서에 나와있는 마지막 도표를 역순으로 진행하면 된다. 즉, 어떤 천사 같은 분이 정리해주신 내용 대로다. 

```ad-tip
- 문제 요약
1. 표1을 보고 입력받은 문자들을 각각 대응하는 숫자로 변경한다.
2. 각 숫자들을 6자리 이진수로 표현하고, 이 이진수들을 한 줄로 쭉 이어 붙인다.
3. 한 줄로 쭉 이어붙인 이진수들을 8자리씩 끊어서 십진수로 바꾼다.
4. 각각의 십진수를 아스키 코드로 변환한다.
```

#### 통과한 코드
```python
# SWEA_1928. Base64 Decoder

import sys
sys.stdin = open('SWEA_1928_input.txt', 'r')

base_64_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

T = int(input())

for t in range(T):
    temp_str = input()

    long_str = ""
    while temp_str:
        a = base_64_str.index(temp_str[0]) # 인덱스(base64)를 확인한다.
        long_str += bin(a)[2:].zfill(6) # 해당 인덱스 값을 2진수로 바꾸고 
        # 앞 두자리 '0b'는 잘라낸 뒤, 6자리 문자열로 맞춘다. 
        temp_str = temp_str.replace(temp_str[0],"", 1) # 처리된 값 삭제

    ans = ""
    while long_str:
        ans += chr(int(long_str[:8], 2)) # 8자 문자열을 10진수로 변환 후 아스키 코드 매핑
        long_str = long_str.replace(long_str[:8],"", 1) # 처리된 값 삭제
        
    print(f'#{t+1} {ans}')
```

- 문제 이해하는 것에서 부터 애를 먹어, 여러 코드를 참고했는데 이 [블로그](https://osnim.tistory.com/entry/SWEA-1928-Based64-Decoder-%ED%8C%8C%EC%9D%B4%EC%8D%AC)가 도움이 많이 됐다.

#### 간단 문법 정리
- [defaultdict](../../Python/defaultdict.md)

##### bin()
- 해당값을 2진수로 바꿔준다.
```python
bin(2)
# '0b10'

bin(10)
# '0b1010'
```

##### .zfill()
- 문자열의 부족한 자릿수를 채워준다
![](assets/SWEA_1928%20Base64%20Decoder-1.png)

##### int(str_num, 2)
- 문자열 타입의 2진수를 10진수로 바꿔준다
```
int('0010011', 2)
19
```
![](assets/SWEA_1928%20Base64%20Decoder.png)
