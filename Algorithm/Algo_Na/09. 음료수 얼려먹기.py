from pprint import pprint 

n, m = map(int, input().split())

ice_form = [[] for _ in range(n)]

for i in range(n):
	temp = input()	
	for char in temp:
		if char == '1':
			ice_form[i].append(1)
		else: 
			ice_form[i].append(0)

pprint(ice_form)

visited = [[False]*m for _ in range(n+1)]

pprint(visited)
