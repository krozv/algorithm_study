# 소프티어 교차로 (Lv.3)
# 실행 시간 459 ms
# 메모리 66.52 MB

from collections import deque


def f():
    pos = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
    stack = [deque(), deque(), deque(), deque()]
    stack_null = [deque(), deque(), deque(), deque()]
    pre_t = int(arr[0][0])
    for i in range(N):
        t, w = arr[i]
        t = int(t)

        while pre_t < t and stack != stack_null:
            flag = 0
            out = [0] * 4
            for j in range(4):
                if stack[j] and not stack[j-1]:
                    out[j] = 1
                    flag = 1
            if flag == 0:
                return
            for j in range(4):
                if out[j]:
                    car_num = stack[j].popleft()
                    out_time[car_num] = pre_t
            pre_t += 1
        pre_t = t
        stack[pos[w]].append(i)

    while True:
        flag = 0
        out = [0] * 4
        for j in range(4):
            if stack[j] and not stack[j-1]:
                out[j] = 1
                flag = 1
        if flag == 0:
            return
        for j in range(4):
            if out[j]:
                car_num = stack[j].popleft()
                out_time[car_num] = pre_t
        pre_t += 1


N = int(input())
arr = list(input().split() for _ in range(N))

out_time = [-1] * N
f()

print(*out_time, sep='\n')