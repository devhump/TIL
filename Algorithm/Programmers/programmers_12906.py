# programmers_12906. 같은 숫자는 싫어 / 스택&큐


def solution(arr):
    result = []
    result.append(arr[0])

    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            continue
        else:
            result.append(arr[i])
    return result


arr = [4, 4, 4, 3, 3]

solution(arr)
