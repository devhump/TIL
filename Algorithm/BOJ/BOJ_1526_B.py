# BOJ_1526 가장 큰 금민수

# 금민수란?
# 해당 문제에서는 문자 4나 7로만 이뤄진 수를 금민수라 한다.

N = int(input())
# N = 474747 

cnt = 0
while True:

    # * 입력받은 수의 자릿수와 카운터를 비교한다.
    if cnt == len(str(N)):
        break

    cnt = 0
    # * 입력받은 수(int)를 문자열로 치환해서(str) 각 자릿수의 수를 확인한다.
    for char in str(N):
        if char == "4" or char == "7":
            cnt += 1 # * 문자 4나 7로 이뤄져 있으면 카운트를 증가 시킨다.
            # todo 10번줄에서 수의 자릿수가 다 4나 7로 이뤄져 있으면 while문을 탈출한다.
        else:
            N -= 1
            # * 금민수가 아니라면 -1 감소 시킨다.
            continue

print(N)