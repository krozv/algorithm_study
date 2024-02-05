
N, M = list(map(int, input().split()))
#NM 행렬
arr_NM = [list(map(int,input().split())) for _ in range(N)]

M, K = list(map(int, input().split()))
#mk 행렬
arr_MK = [list(map(int,input().split())) for _ in range(M)]


#NK행렬
arr_NK = [[0]*K for _ in range(N)]

for x in range(N):
    for y in range(K):
        sum = 0
        for z in range(M):
            sum += arr_NM[x][z] * arr_MK[z][y]
        arr_NK[x][y] = sum


for i in arr_NK:
    print(' '.join(map(str,i)))
