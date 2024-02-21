# bfs 로 풀생각을 못함..
# 이전지점 재탐색 안해서 시간 줄임

from collections import deque
import sys
input = sys.stdin.readline

def bfs(E, v, visited): # 노드연결정보,시작점,vis
    q= deque([v])
    visited[v] = True
    while q:
        x = q.popleft()
        for i in E[x]: #pop 값과 이어진 경로-> 자식 노드
            if not visited[i]:
                P[i] = x # P는 자식노드로 부모 저장
                q.append(i)
                visited[i] = True


N = int(input())
visited = [0]* (N+1)
P = [0]* (N+1)
E = [[] for _ in range(N+1)]
for i in range(N-1):
    n1, n2 = map(int,input().split())
    E[n1].append(n2)
    E[n2].append(n1)

bfs(E,1,visited)
print(*P[2:], sep= '\n')
# bfs



''' 53% 시간초과코드
import sys
input = sys.stdin.readline


N = int(input())

P = [0]* (N+1) # 부모 노드 저장
visit = [0] * (N+1)
visit[1] = 1
arr = [list(map(int, input().split())) for _ in range(N-1)]

#arr의 숫자들을 꼬리물기 하듯이 넣음, 넣고나서 0으로 바꿔주기
#모든 좌표값이 0 으로 바뀔때까지 진행

while visit.count(0) !=1:
    for i in range(N-1):
        n1, n2 = arr[i][0], arr[i][1]
        if n1 == 0:
            continue

        elif visit[n1]:
            visit[n2] = 1
            P[n2] = n1
            arr[i] = [0, 0]

        elif visit[n2]:
            visit[n1] = 1
            P[n1] = n2
            arr[i] = [0, 0]

print(*P[2:], sep = '\n')

'''