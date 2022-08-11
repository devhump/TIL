# BOJ_4963. 섬의 개수

# w -> c 
# h -> r

def p_print(list):
    for row in list:
        print(row)

import sys
sys.stdin = open("BOJ_4963_input.txt")

def DFS(a,b):
    global cnt
    stack = [(a,b)]
    visited_array[a][b] = True
        
    while stack:
        cur = stack.pop()
        p_print(visited_array)
        print()
        for adj in adj_list[cur[0]]:
            if not visited_array[cur[0]][adj]:
                visited_array[cur[0]][adj] = True
                stack.append((cur[0],adj))
    
    if not stack:
        cnt += 1
            

case_num = 0
while True:
    cnt = 0
    case_num += 1
    # w, h
    c, r = map(int, input().split())

    # 탈출 코드
    if c == 0 and r == 0:
        break

    island_map = []

    for i in range(r):
        island_map.append(list(map(int, input().split())))

    print(f"#{case_num}")
    p_print(island_map)

    adj_list = [[] for i in range(r)]
    # p_print(adj_list)

    visited_array = [[False] * c for i in range(r)]
    # p_print(visited_array)

    for i in range(r):
        for j in range(c):
            if island_map[i][j] == 1: #
                adj_list[i].append(j)
            else:
                visited_array[i][j] = True # 바다(a.k.a 0)는 초기에 True 처리
    p_print(adj_list)


    for i in range(r):
        for j in range(c):
            DFS(i,j)
                
    # p_print(visited_array)
    
    #print(adj_list)
    print(cnt)
