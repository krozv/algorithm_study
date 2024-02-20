# 11725. tree fine parent
"""
tree parent fine.
my pycharm is broken
no korean...
why? why?
condition
tree without root
root = 1
who is parent of node?
"""
import sys
input = sys.stdin.readline
N = int(input())
left = [0] * (N+1)
right = [0] * (N+1)
par = [0] * (N+1)
adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    n1, n2 = map(int, input().split())
    adj[n1].append(n2)
    adj[n2].append(n1)
print(adj)