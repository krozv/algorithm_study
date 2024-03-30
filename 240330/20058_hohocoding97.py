import sys
from collections import deque
input = sys.stdin.readline

N, Q = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(2**N)]
magics = list(map(int, input().split()))

# 5중 for문 과연 이게 맞나 싶다...
for magic in magics:
    fs = 2**magic #파이어스톰 한변의 길이
    new_area = [[0]*2**N for _ in range(2**N)] 
    for x in range(2**(N-magic)):
        for y in range(2**(N-magic)):
            for i in range(fs):
                for j in range(fs):
                    # print(fs*x + j, fs*y + fs-i-1)
                    new_area[fs*x + j][fs*y + fs-i-1] = area[fs*x + i][fs*y + j]
    
    plus_area = []
    for i in range(2**N):
        for j in range(2**N):
            cnt = 0
            for di, dj in [(0,1),(0,-1),(1,0),(-1,0)]:
                ni, nj = i+di, j+dj
                if 0<=ni<2**N and 0<=nj<2**N and area[i][j] and area[ni][nj]:
                    cnt += 1
            if cnt <=2:
                if new_area[i][j] > 0:
                    new_area[i][j] -= 1
    area = new_area

max_sum = 0
max_cnt = 0
visited = []
for j in range(2**N):
    cnt = 0
    if (0,j) not in visited and area[0][j]:
        q = deque()
        q.append((0,j))
        visited.append((0,j))
        cnt += 1    
        max_sum += area[0][j]
        while q:
            r, c = q.popleft()
            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = r+dr, c+dc
                if 0<=nr<2**N and 0<=nc<2**N and (nr,nc) not in visited and area[nr][nc] >  0:
                    q.append((nr,nc))
                    visited.append((nr,nc))
                    max_sum += area[nr][nc]
                    cnt += 1
        max_cnt = max(cnt, max_cnt)
print(max_sum)
print(max_cnt)

for a in area:
    print(a)

