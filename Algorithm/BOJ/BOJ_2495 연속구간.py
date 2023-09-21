# BOJ_2495 연속구간
# ! 테케 답은 나오는데 틀림
# * 딕셔너리를 이용해서 풀려했는데 안 되네...
# * 왜 틀렸지...
# * 구글링한 답이 훨씬 간결하고 좋네 ㅎㅎㅎㅎㅎ.....

import sys
sys.stdin = open('BOJ_2495_input.txt', 'r')

for _ in range(3):
    s = input()
    mymax = 1
    cnt = 1
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            cnt+=1
        else:
            mymax=max(cnt,mymax)
            cnt=1
    mymax = max(cnt, mymax)
    print(mymax)



# for _ in range(3):
#     num_str = input()

#     num_dict = {}
#     for i in range(8):

#         if i == 0:
#             num_dict[num_str[i]] = 1
#             continue

#         if num_str[i-1] == num_str[i]:
#             if num_dict.get(num_str[i], 0):
#                 num_dict[num_str[i]] += 1
#             else:
#                 num_dict[num_str[i]] = 1
#         else:
#             if num_dict.get(num_str[i], 0):
#                 num_dict[num_str[i]] = 1
#             else:
#                 num_dict[num_str[i]] = 1

#     temp = (list(num_dict.values()))
#     # temp.sort(key =  lambda x : (x[1]))
#     print(max(temp))
#     # print(temp[-1][1])