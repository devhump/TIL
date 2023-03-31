# BOJ_2920_음계


nums = list(map(int, input().split()))

visited = []
for i in range(len(nums)-1):

    if nums[i] < nums[i+1]:
        visited.append(1)
    elif nums[i] > nums[i+1]:
        visited.append(-1)
    else:
        visited.append(0)

if sum(visited) == 7:
    print("ascending")
elif sum(visited) == -7:
    print("descending")
else:
    print("mixed")
    