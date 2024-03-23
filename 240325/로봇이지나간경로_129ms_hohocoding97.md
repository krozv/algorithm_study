# 로봇이 지나간 경로
### 코드
105ms 37.45MB
```python
H, W = map(int, input().split())
data = [input() for _ in range(H)]  # 전체 맵 데이터
start_pos = []
for i in range(H):
    for j in range(W):
        if not start_pos and data[i][j] == '#':
            cnt = 0
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:  # 상하좌우 돌며 #찾기
                ni, nj = i + di, j + dj
                if 0 <= ni < H and 0 <= nj < W and data[ni][nj] == '#' and cnt <= 1:
                    cnt += 1
            if cnt == 1:
                start_pos = [i, j]  # 시작할 위치 찾기
                print(i+1, j+1)

for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
    ni, nj = start_pos[0] + di, start_pos[1] + dj
    if 0 <= ni < H and 0 <= nj < W and data[ni][nj] == '#':
        if di == 1:
            print('v')
        elif di == -1:
            print('^')
        elif dj == 1:
            print('>')
        else:
            print('<')
        d = (di,dj)
        break

i, j = start_pos
di, dj = d
visited = [[0] * W for _ in range(H)]
visited[i][j] = 1
r = ''
while True:
    for k, nd in enumerate([(di, dj), (-dj, di), (dj, -di)]):  # 정면, 좌, 우
        ni, nj = i + nd[0], j + nd[1]
        if 0 <= ni < H and 0 <= nj < W and data[ni][nj] == '#' and visited[ni][nj] == 0:
            if k == 0:
                r += 'A'
            elif k == 1:
                r += 'LA'
            else:
                r += 'RA'
            visited[ni][nj] = 1
            visited[ni + nd[0]][nj + nd[1]] = 1
            i, j = i+2*nd[0], j+2*nd[1]
            di, dj = nd[0], nd[1]
            break
    else:  # 3방향모두 간기록이 없거나 이미 지났던 방향이면 break
        break
print(r)
```