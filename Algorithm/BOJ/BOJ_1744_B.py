# BOJ_1744 수묶기 / 그리디
# 양수와(positive) 음수(negative) 및 0, 그리고 1.
# 세가지 경우로 나눠 생각한다.

N = int(input())

positives = []
negatives = []
result = 0
for i in range(N):
    temp = int(input())

    if temp > 1:
        positives.append(temp)
    elif temp <= 0:
        negatives.append(temp)
    else:
        result += temp  # temp가 1일 때
        # 1은 무조건 더하는게 커지는 방법이다.

positives.sort()
negatives.sort(reverse=True)

pos_cnt = len(positives)
neg_cnt = len(negatives)

# 양수 처리
while pos_cnt > 1:
    temp1 = positives.pop()
    temp2 = positives.pop()

    result += temp1 * temp2
    pos_cnt -= 2

if pos_cnt == 1:
    result += positives[0]

# 음수 처리
while neg_cnt > 1:
    temp1 = negatives.pop()
    temp2 = negatives.pop()

    result += temp1 * temp2
    neg_cnt -= 2

if neg_cnt == 1:
    result += negatives[0]

print(result)
