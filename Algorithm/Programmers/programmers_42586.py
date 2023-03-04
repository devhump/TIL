# programmers_42586. 기능개발 / 스택&큐


def solution(progresses, speeds):
    answer = []

    N = len(progresses)
    develop_days = []
    for i in range(N):
        develop_days.append(round((100 - progresses[i]) // speeds[i]))

    cnt = 1
    for j in range(N - 1):

        if develop_days[j] >= develop_days[j + 1]:
            cnt += 1
        else:
            cnt = 1
            answer.append(cnt)

    return answer


progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

print(solution(progresses, speeds))
# [2, 1]
