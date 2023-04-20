# BOJ_9455_google


import sys
sys.stdin = open("BOJ_9455_input.txt", "r")

##case1

# for _ in range(int(input())):
#     m, n = map(int, input().split())
#     b = []
#     # * 하나의 리스트로 받아서 
#     for i in range(m):
#         l = list(map(int, input().split()))
#         b.insert(0, l)
#     arr = []
#     # * 여기서 회전된 배열을 만든다. 
#     for j in range(n):
#         tmp = []
#         for k in range(m):
#             tmp.append(b[k][j])
#         arr.append(tmp)
#     cnt = 0
#     for a in arr:
#         t = 0
#         print()
#         print(a)
#         for idx, num in enumerate(a):
#             if num == 1:
#                 cnt += idx - t
#                 t += 1
#     print(cnt)

# # 최종 정렬된 리스트(arr)를 반복 순환하며 
# # ‘1’이 나올 때마다 cnt에 추가한다. 
# # 1의 인덱스 값에서 앞선 1의 숫자만큼을 빼준다. 
# # (그게 움직인 거리니까.)


# case2

for _ in range(int(input())):
    n, m = map(int,input().split())
    box = [input().split() for _ in range(n)] # 전체 리스트 생성
    print(box)
    ans = 0
    for j in range(m):
        cnt = 0
        for i in range(n-1,-1,-1): # 맨 뒤 리스트부터 거꾸로 탐색
            if box[i][j] == '1':
                ans += cnt
            else:
                cnt += 1 
                # 인덱스 값을 찾는 대신, 
                # 0이 나올 때마다 1씩 
                # 임시 카운트 값(cnt)을 추가해주면 된다.
    print(ans)