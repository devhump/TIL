def solution(numbers):
    answer = []

    for i in range(len(numbers)):
      
        for j in range(len(numbers)): # 이중 반복을 통해, 매 회차별 모든 수와의 합을 계산
            if i == j: # 이때, 자기 자신은 제외 
                pass
            else:
                answer.append(numbers[i] + numbers[j])

    answer = list(set(answer))
    answer.sort()

    return answer


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))