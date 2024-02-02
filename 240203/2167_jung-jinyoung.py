N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
K = int(input()) # 합의 개수
for sum_case in range(K):
    positions= list(map(int, input().split()))
    i, j, x, y = positions #좌표 할당


    sum_total = 0
    for row in range(i-1, x): # 좌표 범위 수정 (1,1) =>(0,0)
        for col in range(j-1, y):
            sum_total += matrix[row][col]
    print(sum_total)

