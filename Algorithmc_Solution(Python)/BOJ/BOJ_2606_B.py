# BOJ_2606.바이러스

import sys
sys.stdin = open("BOJ_2606_input.txt")

# 이쁜 출력을 위해
def pprint(list):
    for row in list:
        print(row)


import sys

com_num = int(sys.stdin.readline())
edges = int(sys.stdin.readline())
# print(com_num, edges)

com_list = [[]*(com_num + 1) for i in range(com_num + 1)]

# 인접 리스트 생성
for i in range(edges):
    v1, v2 = map(int, input().split())
    com_list[v1].append(v2)
    com_list[v2].append(v1)
# pprint(com_list)

# 최초 감염 컴퓨터 리스트
virus_visited = [False] * (com_num+1)

# print(virus_visited)

virus_1st = []
virus_1st += com_list[1]
virus_visited[1] = True # 자기 자신(1번 컴)을 우선 방문처리

# 연결된 컴퓨터들 확인
while virus_1st:
    # print(virus_1st)
    temp = virus_1st.pop(0)  

    if virus_visited[temp] == True:
        continue
    
    if virus_visited[temp] == False: # 중복 방지를 위해
        virus_visited[temp] = True
        virus_1st += com_list[temp] # 연결된 리스트 연쇄 확인
        virus_1st = list(set(virus_1st)) 
        # set 처리 안 한게 근소하게 더 빠름

# print(virus_visited)
# print(virus_visited.count(True)-1) # 자기 자신은 제외
print(sum(virus_visited)-1)