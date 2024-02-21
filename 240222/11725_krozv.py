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
def find_parent(p):
    parent = p
    if adj[p]:
        for c in adj[p]:
            par[c] = p  # 자식을 인덱스로 부모를 저장함
            adj[c].remove(p)
            p = c
            find_parent(p)
            p = parent


import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
N = int(input())
par = [0] * (N+1)
adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    n1, n2 = map(int, input().split())
    adj[n1].append(n2)
    adj[n2].append(n1)

find_parent(1)
for i in par[2:]:
    print(i)