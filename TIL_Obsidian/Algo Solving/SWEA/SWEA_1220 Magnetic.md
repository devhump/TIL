---
tags: [Algorithm, python]
---

- [SWEA_1220 [S/W 문제해결 기본] 5일차 - Magnetic](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14hwZqABsCFAYD)

### 내 코드
```python

T = 10 

for t in range(10):
    N = int(input()) # 100 고정
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 좌로 90도 회전
    rot_matrix = [[0] * 100 for _ in range(100)]
    for i in range(100):
        for j in range(100):
            rot_matrix[i][j] = matrix[j][100-1-i]

    # @ 각 줄의 0 모두 삭제
    for i in range(100):
        cnt = rot_matrix[i].count(0)
        for j in range(cnt):
            rot_matrix[i].remove(0)

    # @ N, S극 인근 상극 삭제
    for i in range(100):
        while True:
            if rot_matrix[i][0] == 2:
                rot_matrix[i].pop(0)
            else: 
                break
        
        while True:
            if rot_matrix[i][-1] == 1:
                rot_matrix[i].pop()
            else:
                break

    # @ 1, 2 연속선 상에 달라지는 것 카운트
    res = 0
    for i in range(100):
        cnt = 1
        for j in range(1, len(rot_matrix[i])):
            if rot_matrix[i][j-1] != rot_matrix[i][j]:
                cnt += 1

        res += cnt
            
    print(f'#{t+1} {int(res/2)}')
```



### 구글링 코드 1.
- [출처](https://velog.io/@mein-figur/SWEAPython1220.-Magnetic)
```python
for tc in range(1, 11):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]  # 1: N, 2: S
    mag = list(map(list, zip(*arr)))  # transpose
 
    total_res = 0
    for i in range(n):
        idx = 0 # 앞쪽부터 판단
        bidx = n - 1 # 뒤쪽부터 판단
        while idx < n: # S를 만나면 제거, N을 만나면 멈춤
            if mag[i][idx] == 2:
                mag[i][idx] = 0
            elif mag[i][idx] == 1:
                break
            idx += 1
        while bidx >= 0: # N을 만나면 제거, S를 만나면 멈춤
            if mag[i][bidx] == 1:
                mag[i][bidx] = 0
            elif mag[i][bidx] == 2:
                break
            bidx -= 1
 
        res = ''
        for idx in range(n): # 남은 자석들을 하나의 문자열로 합침
            if mag[i][idx]: 
                res += str(mag[i][idx])
        res = res.replace('12', 'X') # 교착 상태 표시
        total_res += res.count('X') # 교착 상태 개수 추가
         
    print(f'#{tc} {total_res}')
```

### 구글링 코드2
```python
for tc in range(1, 11):
    n = int(input())
    mag = [list(map(int, input().split())) for _ in range(n)]  # 1: N, 2: S
 
    total_res = 0
    for i in range(n):
        flag = 0
        for j in range(n):
            if mag[j][i] == 1:
                flag = 1
            elif mag[j][i] == 2:
                if flag :
                    total_res += 1
                    flag = 0
 
    print(f'#{tc} {total_res}')
```

- 세상은 넓고 능력자는 많다. 고민하며 문제를 풀고 나서, 다른 사람들의 코드는 어떨까 찾아봤는데, 역시나 배울게 많다. 나도 문제들에 좀 더 통달하면, 좀 더 거시적인 관점에서 문제에 접근할 수 있겠지?