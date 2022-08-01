# BOJ_2161. 카드1


###############################################
# 풀이1 - 리스트 이용
###############################################

# T = int(input())
# # T = 7

# card_list = []

# for i in range(1,T+1):
#     card_list.append(i)


# changed_card_list = []
# cnt = 0
# while(1 < len(card_list)):
#     cnt += 1
#     changed_card_list.append(card_list.pop(0))
#     card_list.append(card_list.pop(0))

# changed_card_list = changed_card_list + card_list

# for i in range(len(changed_card_list)):
#     print(changed_card_list[i], end=" ")


###############################################
# 풀이2 - deque
###############################################

from collections import deque
import queue

# n = int(input())
n = 7

queue = deque(range(1, n + 1))

while len(queue) > 1:
    print(queue.popleft(), end=" ")
    queue.append(queue.popleft())

print(queue[0])
print(type(queue), len(queue))
print(queue)

# 1 3 5 7 4 2 6
# <class 'collections.deque'> 1
# deque([6])