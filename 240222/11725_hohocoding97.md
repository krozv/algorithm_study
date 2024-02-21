#1953. 트리의 부모 찾기
### 내 코드
352ms
```python
#트리의 루트를 1이라 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오
import sys
from collections import deque

def bfs():
    q = deque()                 #큐 생성
    q.append(1)                 #루트인 1을 삽입    
    parents[1] = -1             #parents에 기록
    while q:                    #q가 빌때까지 반복
        p = q.popleft()     
        for i in adjl[p]:       #p의 경로 순회
            if parents[i] == 0: #방문하지 않았다면..
                q.append(i)     #q추가
                parents[i] = p  #부모노드를 기록
    return

N = int(input())
adjl = [[] for _ in range(N+1)] #경로를 저장할 리스트 생성
parents = [0]*(N+1)             #어떤 녀석의 부모를 저장해 줄 리스트
for _ in range(N-1):            #N-1개의 경로에 대해 
    num1, num2 = map(int, sys.stdin.readline().split())
    adjl[num1].append(num2)     #경로 저장해주기
    adjl[num2].append(num1)

bfs()
for num in parents[2:]:         #2번부터 N번까지의 부모를 출력하기
    print(num)
```