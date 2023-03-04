# programmers_42586. 기능개발 / 스택&큐

## internet code 2

import math


def solution(progresses, speeds):
    progresses = [math.ceil((100 - a) / b) for a, b in zip(progresses, speeds)]

    answer = []
    front = 0

    for idx in range(len(progresses)):
        if progresses[idx] > progresses[front]:
            answer.append(idx - front)
            front = idx

    answer.append(len(progresses) - front)

    return answer


progresses = [93, 30, 55]
speeds = [1, 30, 5]

print(solution(progresses, speeds))
# [2, 1]


## internet code 1
# def solution(progresses, speeds):

#     answer = []
#     time = 0
#     count = 0

#     while len(progresses) > 0:
#         if (progresses[0] + time * speeds[0]) >= 100:
#             progresses.pop(0)
#             speeds.pop(0)
#             count += 1

#         else:
#             if count > 0:
#                 answer.append(count)
#                 count = 0

#             time += 1

#     answer.append(count)
#     return answer


# progresses = [90, 30, 55]
# speeds = [1, 30, 5]

# print(solution(progresses, speeds))


# # 예시 테스트 케이스는 통과 했지만, 정답 제출은...ㅠㅠ

# def solution(progresses, speeds):
#     answer = []

#     N = len(progresses)
#     develop_days = []
#     for i in range(N):
#         develop_days.append(round((100 - progresses[i]) // speeds[i]))
#     cnt = 1
#     for j in range(N - 1):

#         if develop_days[j] >= develop_days[j + 1]:
#             cnt += 1
#             continue
#         else:
#             answer.append(cnt)
#             cnt = 1
#     answer.append(cnt)

#     return answer


# progresses = [90, 30, 55]
# speeds = [1, 30, 5]

# print(solution(progresses, speeds))
# # [2, 1]
