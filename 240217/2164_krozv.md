# 2164. 카드 2

### 1st

메모리 54872 KB

시간 212 ms

import sys하면 더 짧아질 것으로 예상

```python
# 2164. 카드2
"""
N장의 카드
1~N까지 번호
N부터 1순서대로 쌓여있음
맨 위 버리고, 그 아래 밑으로 보내고 * 반복 -> 마지막 남는 카드는?
1 <= N <= 5e6
"""
from collections import deque
N = int(input())
deq = deque(list(range(N, 0, -1)))
while len(deq) != 1:
    deq.pop()
    deq.appendleft(deq.pop())
print(deq[0])
```