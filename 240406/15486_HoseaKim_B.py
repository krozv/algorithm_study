# 백준 15486 퇴사 2 (골드5)
# python : 97108 KB, 2184 ms
# pypy : 122548 KB, 488 ms
import sys
input = sys.stdin.readline

'''
def dfs(i, ss):
    # print(arr[i])
    global max_ss
    if i >= N or i+arr[i][0] > N:
        if max_ss < ss:
            max_ss = ss
        return
    dfs(i+arr[i][0], ss+arr[i][1])
    dfs(i+1, ss)
    return


# 1 ~ 1,500,000
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

max_ss = 0
dfs(0, 0)

print(max_ss)
'''


N = int(input())

dp = [0] * (N+1)

for i in range(N):
    t, p = map(int, input().split())

    dp[i] = max(dp[i], dp[i-1])

    if i+t <= N and dp[i+t] < dp[i] + p:
        dp[i+t] = dp[i] + p

print(max(dp))