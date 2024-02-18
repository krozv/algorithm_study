# 7465. 창용 마을 무리의 개수

bfs로 풀이함

```python
# 7465. 창용 마을 ~
"""
N명의 사람 살고 있음
몇 개의 무리 존재
bfs 사용하면 금방 풀듯?
"""
def bfs(start):
    v[start] = 1
    q = [start]
    global cnt
    cnt += 1
    while q:
        for i in adj[q[0]]:
            if v[i] == 0:
                q.append(i)
                v[i] = 1
                cnt += 1
        q.pop(0)


import sys
sys.stdin = open('s_input.txt', 'r')
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    adj = [[] for _ in range(N+1)]
    v = [0] * (N+1)
    for _ in range(M):
        n1, n2 = map(int, input().split())
        adj[n1].append(n2)
        adj[n2].append(n1)
    group = 0
    cnt = 0
    while cnt < N:
        for i in range(1, N+1):
            if v[i] == 0:
                bfs(i)
                group += 1
    print(f'#{t} {group}')
```