# BOJ_23253 자료구조는 정말 최고야

# ! 시간초과 코드

 
import sys
sys.stdin = open("BOJ_23253_input.txt", "r")

# import sys 
# input = sys.stdin.readline
data = list(map(int, input().split()))

book_list = [[] for _ in range(data[1])]

# 입력 파트
for i in range(data[1]):
    temp = int(input())
    temp2 = list(map(int, input().split()))
    
    book_list[i].extend(temp2)

k = 1
cnt = 0
i = 0
while True:

    # 책 리스트를 번갈아가면서(swithching)
    if book_list[i]:
        if book_list[i][-1] == k: # 현재 찾는 값이 맞다면 == 순서대로 책을 꺼낼 수 있다면 
            book_list[i].pop(-1) # 책을 뺀다
            k += 1 # 다음책을 찾는다.
            cnt = 0
        else:
            i += 1 # 북 리스트의 인덱스를 조절 1
            if i == (data[1]):
                i = 0
    else:
        i += 1 # 북 리스트의 인덱스를 조절 2
        if i == (data[1]):
            i = 0
    cnt += 1 # 북리스트 순회를 다 해도 책이 순서대로 나오지 않으면 
    if cnt > data[1]: # 종료를 시킨다.
        break

# * 그래서 남은 책 번호의 합을 이용해서 현 상태를 넘겼다.
result = 0
for i in range(len(book_list)):
    result += sum(book_list[i])


# ? 나는 book_list = [[],[]] 일때,
# ? False 값이 나온다고 생각했는데, 아닌가 보다
if result > 0:
    print("No")
else:
    print("Yes")
