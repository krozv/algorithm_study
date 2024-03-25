#델타 상, 우, 하, 좌
d1 = [(-1,0),(0,1),(1,0),(0,-1)]

# 델타 하, 우, 상, 좌
d2 = [(1,0),(0,1),(-1,0),(0,-1)]

def aircon_1(x,y,d):
    #x,y는 공기청정기 첫번째칸-1,d=0에서 시작
    x -=1
    while True:
        nx,ny = x+d1[d][0], y+d1[d][1]
        if 0<= nx <= a1 and 0<= ny < c:
            if arr[nx][ny] == -1:
                return
            else:
                arr[x][y] = arr[nx][ny]#이동전 좌표에 이동한 좌표값 할당
                x,y = nx,ny
        else:
            d+=1



def aircon_2(x,y,d):
    # x,y는 공기청정기 첫번째칸+1,d=0에서 시작
    x += 1
    while True:
        nx, ny = x + d2[d][0], y + d2[d][1]
        if a2 <= nx <r and 0 <= ny < c:
            if arr[nx][ny] == -1:
                return
            else:
                arr[x][y] = arr[nx][ny]  # 이동전 좌표에 이동한 좌표값 할당
                x, y = nx, ny
        else:
            d += 1

def dfs(q): # 현위치 r,c

    while q:
        # 현재좌표, x=좌표의 값 /5
        i, j, x = q.pop(0)
        # 상하좌우 칸
        rc0=rc1=rc2=rc3=0

        # 상하좌우 확인하기
        for k in range(4):
            ni, nj = i+d1[k][0],j+d1[k][1]
            #인접방향확인 + 공기청정기칸은 확산 x
            if 0<= ni < r and 0<= nj < c and arr[ni][nj]!=-1:
                if k==0:
                    rc0 += x
                    arr[ni][nj]+=rc0
                elif k==1:
                    rc1 += x
                    arr[ni][nj]+=rc1
                elif k==2:
                    rc2 += x
                    arr[ni][nj]+=rc2
                elif k==3:
                    rc3 += x
                    arr[ni][nj]+=rc3

        arr[i][j] -=(rc0+rc1+rc2+rc3)
    return


r, c, t = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(r)]

air = []
for i in range(r):
    if arr[i][0]== -1:
        air.append(i)
a1 = air[0]
a2 = air[1]

for _ in range(t):
    # 미세먼지 한번 확산
    q= []
    for i in range(r):
        for j in range(c):
            if arr[i][j]>0:
                # 위치와 나누기 5한값 넣기
                q.append((i,j,arr[i][j]//5))
    dfs(q)

    # 공기청정기 돌리기 공기청정기좌표/ 델타
    aircon_1(a1,0,0)
    # 이동후 공기청정기 첫번째칸 0으로 만들어주기
    arr[a1][1]= 0

    aircon_2(a2,0,0)
    arr[a2][1]= 0

total = 0
for i in range(r):
    for j in range(c):
        if arr[i][j]>0:
            total+=arr[i][j]
print(total)