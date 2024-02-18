# 알파벳 블록
968ms
```python
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
data = [list(input().split()) for _ in range(N)]
q = deque()
stack = []
for datum in data:
    if datum[0] == '1':
        q.append(datum[1])
        stack.append('r')
    elif datum[0] == '2':
        q.appendleft(datum[1])
        stack.append('l')
    else:
        if q:
            if stack.pop() == 'l':
                q.popleft()
            else:
                q.pop()
if q:
    print(''.join(q))
else:
    print(0)
```