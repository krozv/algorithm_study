

import copy
import sys

sys.stdin.readline
from collections import deque
d = [(1,0),(-1,0),(0,1),(0,-1)]

def find(arr):
    for i in range(M):
        for j in range(M):
            if arr[i][j]!=0:
                x = (i,j)
                return x

def final(copy_arr):
    final_arr = copy.deepcopy(copy_arr)
    for i in range(M):
        for j in range(M):
            cnt = 0
            for k in range(4):
                ni,nj = i+d[k][0],j+d[k][1]
                if 0<=ni<M and 0<= nj<M and copy_arr[ni][nj]>0:
                    cnt+=1
            if cnt <3 and copy_arr[i][j]>0:
                final_arr[i][j] = copy_arr[i][j]-1

    return final_arr

def rotate(i,j,N): # 시작좌표, 열 너비 기준 90도 돌린 배열 꺼냄
    for x in range(N):
        for y in range(N):
            ni,nj = y+i, N-1-x+j
            copy_arr[ni][nj] = arr[x+i][y+j]

# 2의지수, 파이어스톰 횟수
power, Q = map(int,input().split())
M = 2**power
arr = [list(map(int,input().split())) for _ in range(M)]

lv_lst = list(map(int,input().split()))
for lv in lv_lst:
    N = 2**lv
    copy_arr = copy.deepcopy(arr)
    for i in range(0,M,N):
        for j in range(0,M,N):
            rotate(i,j,N)

    final_arr = final(copy_arr)
    arr = final_arr

s = 0
for i in arr:
    s+=sum(i)

print(s)
visit = [[0]*M for _ in range(M)]
maxnum = 0
for i in range(M):
    for j in range(M):
        if not visit[i][j] and arr[i][j] != 0:
            q= deque()
            q.append((i,j))
            visit[i][j] = num= 1
            while q:
                (i,j) = q.popleft()
                for k in range(4):
                    ni, nj = i + d[k][0], j + d[k][1]
                    if 0<=ni<M and 0<=nj<M and not visit[ni][nj] and arr[ni][nj]!=0:
                        num+=1
                        visit[ni][nj]=num
                        q.append((ni,nj))

            maxnum=max(num,maxnum)
print(maxnum)