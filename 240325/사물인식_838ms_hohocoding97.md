# 사물인식 최소 면적 산출 프로그램
### 코드
838ms, 52.53MB
```python
import sys

def dfs(i,x1, x2, y1, y2):
    global min_area

    if (x2-x1)*(y2-y1) >= min_area: #백트래킹
        return
    if i == K:
        min_area = min((x2-x1)*(y2-y1), min_area)
        return

    for x, y in data[i]:
        dfs(i+1, min(x1,x),max(x2,x),min(y1,y),max(y2,y))

    
N, K = map(int, input().split())
data = [[] for _ in range(K)]
for _ in range(N):
    x, y, c = map(int, input().split())
    data[c-1].append((x,y))

min_area = int(1e9)

for x, y in data[0]:
    dfs(1,x,x,y,y)
print(min_area)
```