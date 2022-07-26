N = int(input())
# N = 8

for i in range(N):

    climb_list = list(map(int, input().split()))
    # climb_list = [12, 20, 1, 3, 4, 4, 11, 1]   
    start_point = 0
    end_point = 0
    height_list = []
    cnt = 0 

    for i in range(1, len(climb_list)):

        if i == 0:
            continue

        if climb_list[i] > climb_list[i-1]:
            
            while(cnt < 1):
                start_point = climb_list[i-1]
                cnt += 1
            end_point = climb_list[i]

            result = end_point - start_point
            height_list.append(result)
        else:
            cnt = 0

# print(height_list)
print(max(height_list))