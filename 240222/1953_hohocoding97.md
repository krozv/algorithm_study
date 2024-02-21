# 1953. 탈주범 검거
### 내코드
278ms
```python
from collections import deque
#구조물에 따른 이동 가능한 방향
dir = {1:[[0,1],[1,0],[-1,0],[0,-1]],
       2:[[1,0],[-1,0]],
       3:[[0,1],[0,-1]],
       4:[[-1,0],[0,1]],
       5:[[1,0],[0,1]],
       6:[[1,0],[0,-1]],
       7:[[-1,0],[0,-1]]}
 
def bfs():
    q = deque()
    q.append([R,C]) #초기 위치를 큐에 추가해 주기
    visited[R][C] = 1
    cnt = 1
    while q:#큐가 차있고 시간이 L이하일 때까지
        i, j = q.popleft()          #q에서 위치 정보 빼오기
        now_struct = data[i][j]     #현재 구조물
        for x, y in dir[now_struct]:#현재구조물에서 갈수있는 방향 가져옴
            ni, nj = i+x, j+y
            #현재 위치의 방문기록이 L보다 작고, N*M구역 안에 있고, 구조물이 있고, 방문한 적이 없으면
            if visited[i][j] < L and 0<=ni<N and 0<=nj<M and data[ni][nj] !=0 and visited[ni][nj] == 0:
                # 움직여서 위치한 곳에 움직일 수 있는 위치정보 중 [-x,-y]가 있으면
                if [-x, -y] in dir[data[ni][nj]]:
                    q.append([ni, nj]) #갈 수 있다고 판단하고 q에 추가
                    visited[ni][nj] = visited[i][j]+1
                    cnt += 1
    return cnt
 
T = int(input())
for tc in range(1, T+1):
    # N:세로크기, M:가로크기,맨홀뚜껑위치 : (R,C), L:소요시간
    N, M, R, C, L = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]  #터널 데이터
    visited = [[0]*M for _ in range(N)]                         #방문기록
    print(f'#{tc} {bfs()}')
```