# 동서남북, > < v ^
# 시계방향으로
dk = [(-1,0),(0,1),(1,0),(0,-1)] # 위, 우, 하, 좌
dict = {0:'^', 1:'>', 2:'v', 3:'<' }
def f(i,j,d): # 시작좌표 방향
    global now_len,res_lst
    start_i,start_j = i,j
    dir = d #처음 좌표
    q = []
    q.append((i,j))
    visit = [[0]*M for _ in range(N)]
    visit[i][j] = 1
    res = ''
    while q:
        i,j = q.pop(0)
        for k in range(4):
            ni,nj = i+dk[k][0], j+dk[k][1]
            if 0<= ni<N and 0<=nj<M and not visit[ni][nj] and arr[ni][nj] =='#':
                if d==k:
                    res+='A'
                    visit[ni][nj] = 1
                    visit[ni+dk[d][0]][nj+dk[d][1]] = 1
                    q.append((ni+dk[d][0],nj+dk[d][1]))

                elif dk[k] == dk[(d-1)%4]:
                    res+='L'
                    d = k
                    q.append((i,j))
                elif dk[k] ==dk[(d+1)%4]:
                    res+='R'
                    d= k
                    q.append((i,j))
                else:
                    return
    if len(res) < now_len:
        now_len = len(res)
        res_lst[0] = start_i+1
        res_lst[1] = start_j+1
        res_lst[2] = dict[dir]
        res_lst[3] = res
    return



N, M = map(int,input().split())
arr = [list(input())for _ in range(N)]
start=[]

for i in range(N):
    for j in range(M):
        cnt = 0
        for k in range(4):
            ni, nj = i+dk[k][0],j+dk[k][1]
            if 0<=ni<N and 0<=nj<M:
                if arr[ni][nj] == arr[i][j] =='#':
                    cnt+=1
        if cnt == 1:
            start.append((i,j))
# print(start)
now_len = N*M
res_lst = [0]*4
for d in range(4):
    f(start[0][0], start[0][1],d)
    f(start[1][0], start[1][1],d)

# print(res_lst)
print(res_lst[0], end=' ')
print(res_lst[1])
print(res_lst[2])
print(res_lst[3])