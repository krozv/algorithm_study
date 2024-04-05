# 미세먼지 안녕
### 코드
```python
from copy import deepcopy
from collections import deque
import sys
input = sys.stdin.readline

R, C, T = map(int,input().split())
dust = [list(map(int, input().split())) for _ in range(R)]

#공기청정기 위치 찾기
for i in range(R):
    if dust[i][0]==-1:
        ac_pos = i #위쪽 공기청정기 위치
        break
air1 = []
air2 = []
# 공기가 회전하는 구역 순서대로 넣기
di, dj = 0, 1 #이동방향 오른쪽으로 이동 시작
ni = ac_pos
nj = 1
while (ni,nj) != (ac_pos,0): # 제자리 돌아오기 전까지
    if 0<=ni+di<R and 0<=nj+dj<C:
        air1.append((ni,nj))
        ni, nj = ni+di, nj+dj
    else:
        di, dj = -dj, di #방향 변경 좌회전

di, dj = 0, 1 #이동방향 오른쪽으로 이동 시작
ni = ac_pos+1
nj = 1
while (ni,nj) != (ac_pos+1,0): # 제자리 돌아오기 전까지
    if 0<=ni+di<R and 0<=nj+dj<C:
        air2.append((ni,nj))
        ni, nj = ni+di, nj+dj
    else:
        di, dj = dj, -di #방향 변경 우회전

################################################일단 여기 위까지는 나옴
for _ in range(T): #T초동안 반복
    dust_pos = []
    # 미세먼지 위치 찾기
    for i in range(R):
        for j in range(C):
            if dust[i][j] > 0:
                dust_pos.append((i,j))

    new_area = [[0]*C for _ in range(R)]
    # 미세먼지 퍼뜨리기
    # print('dust_pos',dust_pos)
    for r,c in dust_pos:
        cnt = 0 #미세먼지 퍼진 횟수
        for nr,nc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
            if 0<=nr<R and 0<=nc<C and dust[nr][nc] != -1:
                new_area[nr][nc] += dust[r][c]//5
                cnt += 1
        new_area[r][c] += dust[r][c] - cnt*(dust[r][c]//5) #현위치에 남은 미세먼지양 계산

    #공기청정기로 먼지 이동
    #일단 위쪽 공기청정기
    air1_dust = deque(new_area[r][c] for r, c in air1)
    air2_dust = deque(new_area[r][c] for r, c in air2)

    air1_dust.rotate(1)
    air2_dust.rotate(1)
    air1_dust[0] = 0
    air2_dust[0] = 0

    for i, d in enumerate(air1_dust):
        r, c = air1[i]
        new_area[r][c] = d
    for i, d in enumerate(air2_dust):
        r, c = air2[i]
        new_area[r][c] = d
    dust = new_area
    dust[ac_pos][0] = -1
    dust[ac_pos+1][0] = -1

result = 0
for d in dust:
    result += sum(d)
print(result + 2)

```