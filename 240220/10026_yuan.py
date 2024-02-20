
# 구역 찾는함수
def f(s,arr): # 시작점 기준으로 한구역 찾기
    global cnt
    q = []
    q.append(s)
    while q:
        # print(q)
        i,j = q.pop()
        vit[i][j] = 1 #방문점 0만들기
        for di,dj in [(0,1),(0,-1),(1,0),(-1,0)]:
            ni = i + di
            nj = j + dj
            if 0<=ni<N and 0<= nj<N and vit[ni][nj] != 1:
                if arr[ni][nj] == arr[i][j]: # 이동알파벳이 현재랑 같을때
                    q.append((ni,nj))
                    vit[ni][nj] = 1

    cnt+=1 # 한구역이 끝나면 +1

import sys
input = sys.stdin.readline

N = int(input())
arr_nom = [list(input()) for _ in range(N)]

vit= [[0]*N for _ in range(N)]
cnt = 0

# 멀쩡사람 구역찾기
while not all(vit[i][j] ==1 for i in range(N) for j in range(N)):
    for i in range(N):
        for j in range(N):
            if not vit[i][j]:
                s = (i,j)
                f(s,arr_nom)
print(cnt, end=' ')

# 적록생맹인경우 r과g 구분안함
for a in range(N):
    for b in range(N):
        if arr_nom[a][b] in 'RG':
            arr_nom[a][b] = 'x'

vit= [[0]*N for _ in range(N)]
cnt = 0

while not all(vit[i][j] ==1 for i in range(N) for j in range(N)):
    for i in range(N):
        for j in range(N):
            if not vit[i][j]:
                s = (i,j)
                f(s,arr_nom)
print(cnt)