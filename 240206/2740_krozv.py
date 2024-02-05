# 2740. 행렬 곱셈
'''
A : N x M
B : M x K
두 행렬을 곱
'''
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
_, K = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(M)]
arr = [[0]*K for _ in range(N)]
for i in range(N):
    for j in range(K):
        for k in range(M):
            arr[i][j] += A[i][k] * B[k][j]
for i in range(N):
    print(*arr[i])