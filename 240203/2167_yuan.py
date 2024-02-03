import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
arr = [list(map(int,input().split())) for _ in range(N)]

k = int(input())
for _ in range(1,k):
    p,q,r,s = list(map(int,input().split()))

    p -=1
    q -=1
    r -=1
    s -=1

    total_pq = 0
    total_rs = 0

    for i in range(N):
        for j in range(M):
            if i<= p and j<q:
                total_pq += arr[i][j]


            if i<= r and j<= s:
                total_rs += arr[i][j]


    print(total_rs - total_pq)
