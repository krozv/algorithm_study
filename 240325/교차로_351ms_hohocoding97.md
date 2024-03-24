# 교차로
### 코드
351ms, 58.69 MB
```python
import sys
from collections import deque

r_dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
N = int(input())
result = [-1] * N
car_data = [list(input().split()) for _ in range(N)]
road = [deque() for _ in range(4)]  # 도로에 있는 차량 스택?순서대로 A,B,C,D 길에 쌓인 차량
car_exist = [0, 0, 0, 0]  # 현재 time에 차량이 존재하는지에 대해
time = 0
i = 0
while i < N:
    t, w = car_data[i]
    t = int(t)  # 일단 정수형이였으니까
    for j in range(4):
        if road[j]:
            car_exist[j] = 1
        else:
            car_exist[j] = 0

    if t <= time or sum(car_exist) == 0:
        road[r_dict[w]].append(i)
        time = t
        i += 1
    else:
        sum_now = sum(car_exist)
        if sum_now == 4:
            break
        elif sum_now == 3:
            car_pos = (car_exist.index(0) + 1) % 4  # 0이 있는 곳의 다음곳!
            result[road[car_pos].popleft()] = time
        elif sum_now == 2:
            if road[0] and road[2]:
                result[road[0].popleft()], result[road[2].popleft()] = time, time
            elif road[1] and road[3]:
                result[road[1].popleft()], result[road[3].popleft()] = time, time
            elif road[0]:
                if road[1]:
                    result[road[0].popleft()] = time
                else:  # road[3]
                    result[road[3].popleft()] = time
            elif road[2]:
                if road[3]:
                    result[road[2].popleft()] = time
                else:  # road[1].
                    result[road[1].popleft()] = time
        else:  # sum_now == 1
            car_pos = car_exist.index(1)
            result[road[car_pos].popleft()] = time
        time += 1  # 시간 증가

while True:
    for j in range(4):
        if road[j]:
            car_exist[j] = 1
        else:
            car_exist[j] = 0
    sum_now = sum(car_exist)
    if sum_now == 4:
        break
    elif sum_now == 3:
        car_pos = (car_exist.index(0) + 1) % 4  # 0이 있는 곳의 다음곳!
        result[road[car_pos].popleft()] = time
    elif sum_now == 2:
        if road[0] and road[2]:
            result[road[0].popleft()], result[road[2].popleft()] = time, time
        elif road[1] and road[3]:
            result[road[1].popleft()], result[road[3].popleft()] = time, time
        elif road[0]:
            if road[1]:
                result[road[0].popleft()] = time
            else:  # road[3]
                result[road[3].popleft()] = time
        elif road[2]:
            if road[3]:
                result[road[2].popleft()] = time
            else:  # road[1].
                result[road[1].popleft()] = time
    elif sum_now == 1:  # sum_now == 1
        car_pos = car_exist.index(1)
        result[road[car_pos].popleft()] = time
    else:
        break
    time += 1  # 시간 증가

for k in range(N):
    print(result[k])
```
