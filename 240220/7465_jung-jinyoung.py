from collections import deque

def bfs(node,visited,town):
    q = deque([node])
    visited[node] = 1
    while q:
        current_node = q.popleft()
        for neighbor in town[current_node]:
            if not visited[neighbor]:
                visited[neighbor] = 1
                q.append(neighbor)

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    count = 0
    town = [[] for _ in range(N+1)]
    arr = []
    for _ in range(M):
        a,b = map(int,input().split())
        arr.append(a)
        arr.append(b)

    for i in range(M):
        p1 = arr[i*2]
        p2 = arr[i*2 + 1]
        town[p1].append(p2)
        town[p2].append(p1)
    visited = [0] * (N+1)
    for i in range(1, N+1):
        if not visited[i]:
            bfs(i, visited, town)
            count+=1
    print(f'#{tc} {count}')