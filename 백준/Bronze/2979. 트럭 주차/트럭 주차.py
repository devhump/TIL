A, B, C = map(int, input().split())

trucks = []
parking = [0] * 101 
# todo 입력되는 시간의 최댓값이 100이므로 
# todo 101짜리 0으로 채워진 리스트를 선언한다 [idx+1]

for _ in range(3):
    trucks.append(list(map(int, input().split()))) 
    # * 각 트럭의 도착, 출발시간을 받아서 

for i in range(3):
    for j  in range(trucks[i][0], (trucks[i][1])):
        parking[j] += 1
        # todo 주차장에 시간대별 현재 주차되어 있는 차량 대수를 기록한다


result = 0
result += (parking.count(1)) * A
result += (parking.count(2)) * B * 2 # * 주차차량 2대
result += (parking.count(3)) * C * 3 # * 주차차량 3대
print(result)
