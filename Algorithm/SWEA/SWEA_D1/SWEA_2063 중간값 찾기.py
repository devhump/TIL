# SWEA_2063 중간값 찾기

n = int(input())
num_list = list(map(int, input().split()))
num_list.sort()
print(num_list[((n+1)//2)-1])