# 11866. 요세푸스 문제 0
### 내 코드
160ms
```python
from collections import deque
N, K = map(int, input().split()) #원에서 사람들이 제거되는 순서
q = deque(range(1,N+1))

print('<',end='')
i = 0
while q:
    i = (i+1)%K
    num = q.popleft()
    
    if i == 0:
        print(num, end='')
        if q:
            print(', ', end='')
    else:
        q.append(num)
print('>')
```