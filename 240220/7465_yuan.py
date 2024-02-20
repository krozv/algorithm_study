def bfs(s):
    q = []
    vit[s] = 1
    q.append(s)
    while q:
        i = q.pop(0) # 현재 위치 i
        for x in adjl[i]:
            if not vit[x]:
                vit[x] = 1
                q.append(x)

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split()) # M 이 관계 수
    adjl= [[]*N for _ in range(N+1)]
    for _ in range(M):
        ni, nj = map(int, input().split())
        adjl[ni].append(nj)
        adjl[nj].append(ni)

    vit = [0] * (N + 1)  # vit 는 초기화되면 안되니까 함수 밖
    total = 0
    # print(bfs(1))
    while vit.count(0) != 1: # 전부 방문 했을때
        for k in range(len(vit)):
            if k != 0 and not vit[k]:
                bfs(k)
                total += 1
    print(f'#{tc} {total}')

