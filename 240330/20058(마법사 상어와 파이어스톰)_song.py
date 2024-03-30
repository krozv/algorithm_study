# 20058_bj(마법사 상어와 파이어스톰)
'''
https://www.acmicpc.net/problem/20058
'''
from collections import deque
def rotate(l):
    global ice
    arr = [[0] * 2**n for _ in range(2**n)]
    for y in range(0, 2**n, 2**l):
        for x in range(0, 2**n, 2**l):
            for i in range(2**l):
                for j in range(2**l):
                    arr[y+j][x+2**l - i - 1] = ice[y+i][x+j]
    ice = arr

def melt(l):
    rotate(l)
    melt = []
    for y in range(2**n):
        for x in range(2**n):
            cnt = 0
            for d in [1,0], [-1,0], [0,1], [0,-1]:
                mx = x + d[0]
                my = y + d[1]

                if 0 <= mx < 2**n and 0 <= my < 2**n and ice[my][mx]:
                    cnt += 1

            if cnt < 3 and ice[y][x]:
                melt.append([x, y])

    for x, y in melt:
        ice[y][x] -= 1

def bfs():
    global ice_sum, max_cnt
    for y in range(2**n):
        for x in range(2**n):
            cnt = 0
            if not visited[y][x] and ice[y][x]:
                q = deque()
                q.append([x,y])
                visited[y][x] = 1

                while q:
                    sx, sy = q.popleft()
                    cnt += 1
                    ice_sum += ice[sy][sx]

                    for d in [1, 0], [-1, 0], [0, 1], [0, -1]:
                        mx = sx + d[0]
                        my = sy + d[1]
                        if 0 <= mx < 2 ** n and 0 <= my < 2 ** n and ice[my][mx] and not visited[my][mx]:
                            q.append([mx, my])
                            visited[my][mx] = 1

            max_cnt = max(cnt, max_cnt)

n, q = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(2**n)]
level = list(map(int, input().split()))
max_cnt = 0
ice_sum = 0

for l in level:
    melt(l)

visited = [[0]*2**n for _ in range(2**n)]
bfs()

print(ice_sum)
print(max_cnt)