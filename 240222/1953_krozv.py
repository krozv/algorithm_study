# 1953. 탈주범 검거
"""
구조물 타입 정리 + bfs
인접 제약조건을 처리해야 함
맞은편에 지나갈 수 있는 통로를 어떻게 저장?
(1 + 3) % 4
(0 + 2) % 4
"""
from collections import deque


def bfs(x, y):
    q = deque()
    q.append([x, y])
    v[x][y] = 1
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    cnt = 1
    while q:

        if v[q[0][0]][q[0][1]] == L:
            break

        direction = st[tunnel[q[0][0]][q[0][1]]]

        for k in direction:
            ni = q[0][0] + di[k]
            nj = q[0][1] + dj[k]
            if 0<=ni<N and 0<=nj<M and v[ni][nj] == 0 and tunnel[ni][nj] != 0:
                if ((k + 2) % 4) in st[tunnel[ni][nj]]:
                    q.append([ni, nj])
                    v[ni][nj] = v[q[0][0]][q[0][1]] + 1
                    if v[ni][nj] <= L:
                        cnt += 1
        q.popleft()
    return cnt


# 구조물 타입 정리
st = {1: [0, 1, 2, 3],
      2: [0, 2],
      3: [1, 3],
      4: [0, 1],
      5: [1, 2],
      6: [2, 3],
      7: [0, 3]}

T = int(input())
for t in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    v = [[0] * M for _ in range(N)]
    print(f'#{t} {bfs(R, C)}')
