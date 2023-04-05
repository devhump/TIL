# BOJ_1764 듣보잡
import sys
sys.stdin = open("BOJ_1764_input.txt", "r")

# * 딕셔너리 스페셜. 
# * 딕셔너리는 리스트 보다 빠르다!!!e
# import sys 
input = sys.stdin.readline

cnt = list(map(int, input().split()))

not_hear = cnt[0]
not_see = cnt[1]

not_hear_dict = {}
for i in range(not_hear):
    temp = input().rstrip()
    not_hear_dict[temp] = 1

not_hear_see = []
for j in range(not_see):
    temp2 = input().rstrip()
    if not_hear_dict.get(temp2, 0):
        not_hear_see.append(temp2)

not_hear_see.sort()

print(len(not_hear_see))
for name in not_hear_see:
    print(name)    
# ! 시간 초과
# not_hear_list = []
# for i in range(not_hear):
#     not_hear_list.append(input())

# not_hear_see = []
# for i in range(not_see):
#     temp = input()
#     if temp in not_hear_list:
#         not_hear_see.append(temp)

# not_hear_see.sort()
# print(len(not_hear_see))
# for name in not_hear_see:
#     print(name, end="")
