# BOJ_1439 뒤집기 / 그리디

digit_list = input()

change_cnt = 0
# 수열의 첫번째 기준점을 설정한다.
start_sym = digit_list[0]
for i in range(1, len(digit_list)):

    # n번째와 n-1 번째 문자가 동일한지 확인한다.
    if digit_list[i] == digit_list[i - 1]:
        continue
    else:
        # 문자가 변경되는 횟수를 카운팅한다.
        change_cnt += 1

if change_cnt >= 2:
    if change_cnt % 2 == 0:
        change_cnt /= 2
    else:
        change_cnt /= 2
        change_cnt += 1

print(int(change_cnt))

# 가령 00110 의 숫자의 경우, 최초 숫자 0에서 2회 바뀌는데 (0 -> 1 -> 0)
# 이처럼 cnt 가 2 이상일 경우, 숫자가 바뀌는 '시작 & 끝' 2회씩 카운팅 하게 된다.
#
# 따라서 cnt 가 짝수일 경우 n*2 / 홀수일 경우 (n*2) + 1 형태로 나오는데,
# 이걸 계산하면 정답은 n 번 / 또는 n+1 이 된다.
