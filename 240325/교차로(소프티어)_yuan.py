import sys
sys.stdin = open("input1.txt","r")
from collections import deque

# from copy import deepcopy

dic = {'A':0,'B':1,'C':2,'D':3}
N= int(input())
res = [-1] * N
waiting = [0,0,0,0]

# 각각 a/b/c/d/리스트
q = [deque() for _ in range(4)]
#큐에 인덱스랑 시간 넣기
for i in range(N):
    time, char = input().split()
    #0번쨰 큐에 [번호,타임] -> a큐,b큐,c큐,d큐
    q[dic[char]].append([i,int(time)])

now = 0 # 현재시간
while q[0] or q[1] or q[2] or q[3]:
    mintime = int(1e9)
    for i in range(4):
        # 각 큐의 첫번째차의 첫번쨰 시간이 now일떄
        if q[i]:
            car_time = q[i][0][1]
            mintime = min(car_time,mintime) #최소시간 잡아주기
            if car_time <= now:
                waiting[i] = 1


    if waiting == [1,1,1,1]: # 교착
        break

    if waiting == [0,0,0,0]: # 차 한대도 없음
        # now는 차 있는 시간으로 조정해주기
        now = mintime
        continue

    for i in range(4):
        if waiting[i] and not waiting[(i-1)%4]:
            idx, _ = q[i].popleft() # 어차피 맨 앞줄 확인하는거라 앞에꺼 뺴기
            res[idx] = now # 빠지는 현재시간 res에 저장

    now+=1 # 차가 부분부분있으면 평범하게 +1 해주기
    waiting = [0,0,0,0] # 다 끝나면 waiting 다시 조정

print(*res,sep='\n')