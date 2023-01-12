# BOJ_1541 잃어버린 괄호 / 그리디

# 55-50+40

first = input().split("-")
# 처음엔 - 를 기준으로 문자열을 잘라준다
# ["55", "50+40"]

for i in range(len(first)):

    if "+" in first[i]:  # +가 있는 경우, 이를 또 잘라준다
        second = map(int, first[i].split("+"))  # [50, 40]
        first[i] = sum(second)
    else:
        first[i] = int(first[i])

    if i == 0:  # 문자열 최초의 값은 무조건 양수이고,
        result = first[i]
    else:  # 이 다음에 오는 수는 음수이다.
        result -= first[i]

print(result)
