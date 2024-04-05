# 백준 1520 내리막 길 (골드3)
# python : 42780 KB, 136 ms
# pypy : 메모리초과
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


def dfs(i, j):
    if i == n-1 and j == m-1:
        return 1

    if dp[i][j] != -1:
        return dp[i][j]

    cnt = 0
    for d in range(4):
        ni, nj = i + dx[d], j + dy[d]
        if 0 <= ni < n and 0 <= nj < m and arr[i][j] > arr[ni][nj]:
            cnt += dfs(ni, nj)

    dp[i][j] = cnt
    return cnt


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
dp = [[-1] * m for _ in range(n)]
 
print(dfs(0, 0))