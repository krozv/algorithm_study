# 7465. 창용 마을 무리의 개수
### 첫 시도. BFS활용
시간초과...0/10
```python
def f():
    relatinonships = [[] for _ in range(N+1)] #relationshiops[i]는 i번째 사람과 관계있는 사람들 정보가 들어감
    for num1, num2 in data:
        relatinonships[num1].append(num2)
        relatinonships[num2].append(num1)
    
    group = [0]*(N+1) #visited같은 역할을 할 리스트
    group[0] = 1
    q = []
    group_num = 0 #각 그룹의 번호
    while 0 in group:   #그룹에 0이란게 없어질때까지
        group_num += 1
        for i in range(1,N):
            if group[i] == 0:
                q.append(i)
                group[i] = group_num
                break
        while q:
            person = q.pop(0)
            for p in relatinonships[person]:
                if group[p] == 0: #p가 아직 그룹에 속하지 않은 경우
                    group[p] = group_num
                    q.append(p)
    return group_num

T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(M)]
    print(f'#{tc} {f()}')
```


### deque 활용
259ms
```python
from collections import deque
def f():
    relatinonships = [[] for _ in range(N+1)] #relationshiops[i]는 i번째 사람과 관계있는 사람들 정보가 들어감
    for num1, num2 in data:
        relatinonships[num1].append(num2)
        relatinonships[num2].append(num1)
    
    group = [0]*(N+1) #visited같은 역할을 할 리스트
    group[0] = 1
    q = deque()
    group_num = 0 #각 그룹의 번호
    while 0 in group:   #그룹에 0이란게 없어질때까지
        group_num += 1
        for i in range(1,N+1): ###여기서 range설정 잘못해서 테스트케이스 7/10 만 통과
            if group[i] == 0:
                q.append(i)
                group[i] = group_num
                break
        while q:
            person = q.popleft()
            for p in relatinonships[person]:
                if group[p] == 0: #p가 아직 그룹에 속하지 않은 경우
                    group[p] = group_num
                    q.append(p)          
    return group_num

T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(M)]
    print(f'#{tc} {f()}')
    
```