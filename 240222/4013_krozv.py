# 4013. 특이한 자석
"""
자석을 1칸씩 K번 회전 -> 1칸 회전할 때 붙어 있는 자석과 자성이 다를 경우 반대 방향으로 1칸 회전
시계방향 1, 반시계 방향 -1
N극 0, S극 1
톱니바퀴 자석 정보는 빨간 화살표 기준 1번
"""
from collections import deque


def clockwise(deq:deque):
    deq.appendleft(deq.pop())


def anticlock(deq):
    deq.append(deq.popleft())


def decision_rot(c, direction):
    l = c - 1
    if l > 0 and rot[l] == 0:
        if arr[l][2] != arr[c][6]:
            rot[l] = 0 - direction
            decision_rot(l, rot[l])
    r = c + 1
    if r < 5 and rot[r] == 0:
        if arr[c][2] != arr[r][6]:
            rot[r] = 0 - direction
            decision_rot(r, rot[r])


T = int(input())
for t in range(1, T+1):
    K = int(input())
    # que or deque로 풀 생각임
    arr = [[] for _ in range(5)]
    for i in range(4):
        arr[i+1] = deque(list(map(int, input().split())))
    info = [list(map(int, input().split())) for _ in range(K)]
    S = 0
    for rotation in info:
        mag, direction = rotation   # 자석 번호, 회전방향
        rot = [0, 0, 0, 0, 0]
        rot[mag] = direction
        decision_rot(mag, rot[mag])
        # 회전 시작
        for i in range(1, 5):
            if rot[i]:
                if rot[i] == 1:
                    clockwise(arr[i])
                else:
                    anticlock(arr[i])
    # 점수 체크
    for i in range(1, 5):
        if arr[i][0] == 1:
            S += 2 ** (i-1)
    print(f'#{t} {S}')
