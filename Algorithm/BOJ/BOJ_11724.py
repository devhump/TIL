# BOJ_11724. 연결 요소의 개수

import sys
sys.stdin = open("BOJ_11724_input_2.txt")
#input.txt 일때 2 출력
# sys.stdin = open("BOJ_11724_input_2.txt")
#input_2.txt 일때 1 출력

# def p_print(list):
#     for row in list:
#         print(row)

input = sys.stdin.readline

nodes, edges = map(int, input().split())

adj_list = [[] for i in range(nodes+1)]

for i in range(edges):
    n1, n2 = map(int, input().split())

    adj_list[n1].append(n2)
    adj_list[n2].append(n1)

# p_print(adj_list)

visited = [False] * (nodes+1)
# print(visited)

i = 0
while True:
    if len(adj_list[i]) == 0:
        i += 1 
    else:
        break

stack = []
stack += adj_list[i]
visited[i] = True

# 'stack = adj_list'가 아닌 이유
# stack.append("z")
# print(adj_list[i])
# print(id(stack))
# print(id(adj_list[i]))

visited[0] = True #개수 카운팅을 위해 index[0]를 True
cnt = 1
while sum(visited) != (nodes+1):
    # print(stack)

    while (not stack):
        if not stack: #stack이 비었으면
            i = visited.index(False)
            cnt += 1
            stack += adj_list[i] 
        else:
            break
    
    temp = stack.pop(0)
    

    # for adj in adj_list[temp]:
    #     if not visited[temp]:
    #         visited[temp] = True
    #         stack += adj_list[temp]
    
    if visited[temp] == False:
        visited[temp] = True
        stack += adj_list[temp]
    #     #stack = list(set(stack))

    # print(visited)

print(cnt)


# BOJ_11724. 연결 요소의 개수

import sys
sys.stdin = open("BOJ_11724_input_2.txt")
#input.txt 일때 2 출력
# sys.stdin = open("BOJ_11724_input_2.txt")
#input_2.txt 일때 1 출력

# def p_print(list):
#     for row in list:
#         print(row)

import sys

input = sys.stdin.readline
nodes, edges = map(int, input().split())

adj_list = [[] for i in range(nodes+1)]

for i in range(edges):
    n1, n2 = map(int, input().split())

    adj_list[n1].append(n2)
    adj_list[n2].append(n1)

visited = [False] * (nodes+1)

#어디서 시작하는지 결정하기 위해
i = 0
while True:
    if len(adj_list[i]) == 0:
        i += 1 
    else:
        break

stack = []
stack += adj_list[i]
visited[i] = True

visited[0] = True #개수 카운팅을 위해 index[0]를 True
cnt = 1
while sum(visited) != (nodes+1): 

    while (not stack): 
        # 스택이 비었다? -> 해당 인접요소 연결된 리스트 다 훑어봄 
        if not stack: #stack이 비었으면
            i = visited.index(False)
            cnt += 1
            stack += adj_list[i] 
        else:
            break
    
    temp = stack.pop(0)
    
    if visited[temp] == False:
        visited[temp] = True
        stack += adj_list[temp]

print(cnt)