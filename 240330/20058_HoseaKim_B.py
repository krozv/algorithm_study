# 마법사 상어와 파이어스톰 (골드3)
from collections import deque
from pprint import pprint

# N: 2~6 / Q: 1~1000 (총 시전)
N, Q = map(int, input().split())
# 0~100
arr = [list(map(int, input().split())) for _ in range(2**N)]
# 매 시전 단계 1~N (2**L * 2**L 격자 90도 회전)
L = list(map(int, input().split()))

# def rotate(x, y, k):
#     for i in range(i, i+)
#     for d in range(4):
#         i, j = i + dx[d]*(2**(k-1)), j + dy[d]*(2**(k-1))
#         arr[i][j], temp = temp, arr[i][j]

def melt():
    # 얼음 녹이기
    melting = []
    for i in range(2**N):
        for j in range(2**N):
            if arr[i][j]:
                cnt = 0
                for d in range(4):
                    ni, nj = i + dx[d], j + dy[d]
                    if 0 <= ni < 2**N and 0 <= nj < 2**N and arr[ni][nj]:
                        cnt += 1
                if cnt < 3:
                    melting.append([i, j])
    for x, y in melting:
        arr[x][y] -= 1

def bfs(i, j):
    global max_cnt
    dq = deque([[i, j]])
    arr[i][j] = 0
    cnt = 1
    while dq:
        t = dq.popleft()
        for d in range(4):
            ni, nj = t[0] + dx[d], t[1] + dy[d]
            if 0 <= ni < 2**N and 0 <= nj < 2**N and arr[ni][nj]:
                dq.append([ni, nj])
                arr[ni][nj] = 0
                cnt += 1
    max_cnt = max(max_cnt, cnt)

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

# 각 마법 시전하기 (돌리기)
for q in range(Q):
    # print()
    # print(L[q])
    if L[q]:
        new_arr = [[0] * 2**N for _ in range(2**N)]
        # 각 구역들 순회
        for i in range(0, 2**N-1, 2**L[q]):
            for j in range(0, 2**N-1, 2**L[q]):
                # 한 구역 돌리기
                for x in range(2**L[q]):
                    for y in range(2**L[q]):
                        new_arr[i+y][j+(2**L[q]-1)-x] = arr[i+x][j+y]
                        # rotate(x, y, L[q])
                # pprint(new_arr)
        arr = new_arr
    # for i in range(2**N):
    #     print(*arr[i])
    melt()
    # print()
    # for i in range(2**N):
    #     print(*arr[i])
# 1. 남은 얼음의 합
print(sum(map(sum, arr)))

# 2. 가장 큰 덩어리 칸 수
max_cnt = 0
for i in range(2**N-1):
    for j in range(2**N-1):
        if arr[i][j]:
            bfs(i, j)
print(max_cnt)