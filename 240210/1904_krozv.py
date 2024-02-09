# 1904 01타일
"""
1 하나만으로 이루어진 타일
00 두 개로 이루어진 타일
N 타일 개수가 주어졌을 때 지원이가 만들 수 있는 모든 가짓수

n = 3
100 001 111
return dp(2) + dp(1) = 3
n = 4
1001 1111 1111 0000 0011
return dp(3) + dp(n-2)
"""

"""
1st 
RecursionError + 시간 초과 + 메모리 초과....

def DP(n):
    if n > 2:
        if memo[n]:
            return memo[n]
        else:
            memo[n] = (DP(n-1) + DP(n-2)) % 15746
    return memo[n]

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())
memo = [0] * (N + 1)
memo[1] = 1
memo[2] = 2
print(DP(N))
"""

"""
2nd
그냥 for문 쓰니까 해결됨
이럴거면 왜 동적계획법..?
"""
import sys
input = sys.stdin.readline
N = int(input())
memo = [0] * (N + 1)
if N >= 1:
    memo[1] = 1
if N >= 2:
    memo[2] = 2
for i in range(3, N+1):
    memo[i] = (memo[i-1] + memo[i-2]) % 15746
print(memo[N])