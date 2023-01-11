cnt = int(input())

rope = []
value = []
for i in range(cnt):
    rope.append(int(input()))

rope.sort(reverse=True)

for i in range(cnt):
    value.append(rope[i]*(i+1))
    
print(max(value))