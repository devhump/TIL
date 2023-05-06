import sys
from collections import deque
input = sys.stdin.readline

#정점 개수 n, 간선 개수 m, 탐색을 시작할 정점 번호 v
n, m, v = map(int,(input().rstrip().rsplit()))
nodes = []
graph = {}


def dfs(graph, start_node):
    visit = []
    stack = []
    
    stack.append(start_node)
    while stack:
        #가장 뒤에 있는 요소 pop
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            if node in graph:
                temp = list(set(graph[node])-set(visit))
                temp.sort(reverse=True)
                stack += temp
    return " ".join(str(i) for i in visit)

def bfs(graph, start_node):
    visit = []
    queue = deque()

    queue.append(start_node)
    while queue:
        #가장 앞에 있는 요소 pop
        node = queue.popleft()
        if node not in visit:
            visit.append(node)
            if node in graph:
                temp = list(set(graph[node])-set(visit))
                temp.sort()
                queue += temp
    return " ".join(str(i) for i in visit)

for i in range(m):
    x,y = map(int,input().rstrip().rsplit())
    nodes.append([x,y])

    if x not in graph:
        graph[x]=[y]
    else:
        graph[x].append(y)

    if y not in graph:
        graph[y]=[x]
    else:
        graph[y].append(x)

print(dfs(graph,v))
print(bfs(graph,v))