# BOJ_11000 강의실 배정 / 그리디

# cnt = int(input())
cnt = 3

class_list = []
for i in range(cnt):
    class_list.append(tuple(map(int, input().split())))

# class_list.sort()


visit = [False] * cnt

visit[0] = True
result = 0

while class_list:
    for i in range(cnt):
        if i == 0:
            end = class_list[0][1]
            result += 1
            continue
        elif visit[i] == True:
            continue
        elif class_list[i][0] >= end:
            end = class_list[i][1]
            visit[i] = True

i = 0
while class_list:
    end = class_list[0][1]
    class_list.pop(0)

    if class_list[i][0] >= end:
        class_list.pop(i)
        i = 0
    else:
        i += 1
        