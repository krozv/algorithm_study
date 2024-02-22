'''
1953. [모의 SW 역량테스트] 탈주범 검거

탈주범은 한시간 뒤 맨홀 뚜껑으로 들어감 시간당 한 칸씩
탈주범이 있을 수 있는 위치의 개수

터널 구조물 7가지
1: 상하좌우
2: 상하
3: 좌우
4: 상우
5: 하우
6: 하좌
7: 상좌
'''


'''
# 초안_다른건 짰으나 출력 결과가 안 맞음
# 반대편 파이프에서 받을 수 있을지를 확인해봐야 함
from collections import deque


def where_is(n, m, t):
    if t == L:
        return

    t += 1
    global v_cnt
    visited[n][m] = 1
    recently_visited.append(n)
    recently_visited.append(m)
    v_cnt += 1

    if ut[n][m] == 1:
        for di, dj in [0, 1], [1, 0], [0, -1], [-1, 0]:
            ni = n + di
            nj = m + dj
            if 0<=ni<N and 0<=nj<M and ut[ni][nj] != 0 and visited[ni][nj] != 1:
                where_is(ni, nj, t)
    elif ut[n][m] == 2:
        for di, dj in [1, 0], [-1, 0]:
            ni = n + di
            nj = m + dj
            if 0<=ni<N and 0<=nj<M and ut[ni][nj] != 0 and visited[ni][nj] != 1:
                where_is(ni, nj, t)
    elif ut[n][m] == 3:
        for di, dj in [0, 1], [0, -1]:
            ni = n + di
            nj = m + dj
            if 0<=ni<N and 0<=nj<M and ut[ni][nj] != 0 and visited[ni][nj] != 1:
                where_is(ni, nj, t)
    elif ut[n][m] == 4:
        for di, dj in [0, 1], [-1, 0]:
            ni = n + di
            nj = m + dj
            if 0<=ni<N and 0<=nj<M and ut[ni][nj] != 0 and visited[ni][nj] != 1:
                where_is(ni, nj, t)
    elif ut[n][m] == 5:
        for di, dj in [0, 1], [1, 0]:
            ni = n + di
            nj = m + dj
            if 0<=ni<N and 0<=nj<M and ut[ni][nj] != 0 and visited[ni][nj] != 1:
                where_is(ni, nj, t)
    elif ut[n][m] == 6:
        for di, dj in [1, 0], [0, -1]:
            ni = n + di
            nj = m + dj
            if 0<=ni<N and 0<=nj<M and ut[ni][nj] != 0 and visited[ni][nj] != 1:
                where_is(ni, nj, t)
    elif ut[n][m] == 7:
        for di, dj in [0, -1], [-1, 0]:
            ni = n + di
            nj = m + dj
            if 0<=ni<N and 0<=nj<M and ut[ni][nj] != 0 and visited[ni][nj] != 1:
                where_is(ni, nj, t)


T = int(input())
for x in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    ut = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    v_cnt = 0
    recently_visited = deque()

    where_is(R, C, 0)

    print(f'#{x} {v_cnt}')'''


# 수정안_저런식으로 인덱스에다가 이동을 저장 해서 해보려고 한다.
# 그래도 자석 문제 어떤건지 읽어는 봐야 하니까 일단 넘어간다..
# 아니 나 진짜 더더 열심히 할거다 믿어주라
def where_is(n, m, t):
    if t == L:
        return

    t += 1
    global v_cnt
    visited[n][m] = 1
    v_cnt += 1
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    pipe = [[-1], [0, 1, 2, 3], [1, 3], [0, 2], [0, 3], [0, 1], [1, 2], [2, 3]]
    if ut[n][m] == 1:
        for di, dj in [0, 1], [1, 0], [0, -1], [-1, 0]:
            ni = n + di
            nj = m + dj
            if 0<=ni<N and 0<=nj<M and ut[ni][nj] != 0 and visited[ni][nj] != 1:
                where_is(ni, nj, t)
    elif ut[n][m] == 2:
        for di, dj in [1, 0], [-1, 0]:
            ni = n + di
            nj = m + dj
            if 0<=ni<N and 0<=nj<M and ut[ni][nj] != 0 and visited[ni][nj] != 1:
                where_is(ni, nj, t)
    elif ut[n][m] == 3:
        for di, dj in [0, 1], [0, -1]:
            ni = n + di
            nj = m + dj
            if 0<=ni<N and 0<=nj<M and ut[ni][nj] != 0 and visited[ni][nj] != 1:
                where_is(ni, nj, t)
    elif ut[n][m] == 4:
        for di, dj in [0, 1], [-1, 0]:
            ni = n + di
            nj = m + dj
            if 0<=ni<N and 0<=nj<M and ut[ni][nj] != 0 and visited[ni][nj] != 1:
                where_is(ni, nj, t)
    elif ut[n][m] == 5:
        for di, dj in [0, 1], [1, 0]:
            ni = n + di
            nj = m + dj
            if 0<=ni<N and 0<=nj<M and ut[ni][nj] != 0 and visited[ni][nj] != 1:
                where_is(ni, nj, t)
    elif ut[n][m] == 6:
        for di, dj in [1, 0], [0, -1]:
            ni = n + di
            nj = m + dj
            if 0<=ni<N and 0<=nj<M and ut[ni][nj] != 0 and visited[ni][nj] != 1:
                where_is(ni, nj, t)
    elif ut[n][m] == 7:
        for di, dj in [0, -1], [-1, 0]:
            ni = n + di
            nj = m + dj
            if 0<=ni<N and 0<=nj<M and ut[ni][nj] != 0 and visited[ni][nj] != 1:
                where_is(ni, nj, t)


T = int(input())
for x in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    ut = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    v_cnt = 0
    # recently_visited = deque()

    where_is(R, C, 0)

    print(f'#{x} {v_cnt}')

