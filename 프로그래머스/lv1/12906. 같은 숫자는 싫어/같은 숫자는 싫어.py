def solution(arr):
    result = []
    result.append(arr[0])

    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            continue
        else:
            result.append(arr[i])
    return result