# 10026. 적록색약
적절히 bfs쓰면 될수도?

### 내 코드
python3 - 112ms
```python
# 적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못함.
# 적록색약이 아닌 사람이 봤을 때의 국역의 개수와 적록색약인 사람이 봤을 때의 구역의 수를 공백으로 구분해 출력하시오
import sys
from collections import deque

#적록색약 아닌 사람이 봤을 때의 구역 개수
def count_zone1():
    visited = [[0]*N for _ in range(N)]
    q = deque() #큐 생성
    q.append((0,0))
    zone = 0    #구역번호
    while True:    
        for i in range(N):
            if 0 in visited[i]: 
                j = visited[i].index(0)
                zone += 1
                visited[i][j] = zone
                q.append((i, j))
                break
        else: #방문한곳이 더이상 없으면 while문 나가기
            break
        while q:                #큐가 차있는 동안 반복   
            i, j = q.popleft()  #큐의 왼쪽에서 꺼낸 위치 정보
            c = data[i][j]      #현재 위치의 색깔 정보
            for move in [[1,0],[-1,0],[0,1],[0,-1]]:
                ni, nj = i+move[0], j+move[1]
                if 0<=ni<N and 0<=nj<N and visited[ni][nj] == 0 and data[ni][nj] == c:
                    q.append((ni,nj))
                    visited[ni][nj] = zone
    return zone

#적록색약인 사람이 봤을 때의 구역 개수
def count_zone2():
    visited = [[0]*N for _ in range(N)]
    q = deque() #큐 생성
    q.append((0,0))
    zone = 0    #구역번호
    while True:    
        for i in range(N):
            if 0 in visited[i]: 
                j = visited[i].index(0)
                zone += 1
                visited[i][j] = zone
                q.append((i, j))
                break
        else: #방문한곳이 더이상 없으면 while문 나가기
            break
        while q:                #큐가 차있는 동안 반복   
            i, j = q.popleft()  #큐의 왼쪽에서 꺼낸 위치 정보
            c = data[i][j]      #현재 위치의 색깔 정보
            for move in [[1,0],[-1,0],[0,1],[0,-1]]:
                ni, nj = i+move[0], j+move[1]
                if 0<=ni<N and 0<=nj<N and visited[ni][nj] == 0:
                    if c in ['R','G'] and data[ni][nj] in ['R','G']:
                        q.append((ni,nj))
                        visited[ni][nj] = zone
                    elif c == 'B' and data[ni][nj] == 'B':
                        q.append((ni,nj))
                        visited[ni][nj] = zone
    return zone

N = int(input())
data = [list(sys.stdin.readline()) for _ in range(N)]
print(count_zone1(), count_zone2())
```
