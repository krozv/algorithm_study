import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
arr = [list(map(int,input().split())) for _ in range(N)]

k = int(input())
for _ in range(k):
    p,q,r,s = list(map(int,input().split()))

    p -=1
    q -=1
    r -=1
    s -=1
    total = 0
    for i in range(N):
        for j in range(M):
            if p<=i<=r and q<=j<=s:
                total += arr[i][j]
    print(total)
