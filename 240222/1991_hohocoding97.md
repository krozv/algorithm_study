# 트리 순회
### 내 코드
40ms
```python
import sys
def pre_order(alphabet):
    p = alphabet
    c1 = C1[p]
    c2 = C2[p]
    print(p, end='')
    if c1 != '.':
        pre_order(c1)
    if c2 != '.':
        pre_order(c2)

def in_order(alphabet):
    p = alphabet
    c1 = C1[p]
    c2 = C2[p]
    if c1 != '.':
        in_order(c1)
    print(p, end='')
    if c2 != '.':
        in_order(c2)

def post_order(alphabet):
    p = alphabet
    c1 = C1[p]
    c2 = C2[p]
    if c1 != '.':
        post_order(c1)
    if c2 != '.':
        post_order(c2)
    print(p, end='')

N = int(input())
C1 = {}
C2 = {}
for _ in range(N):
    p, c1, c2 = sys.stdin.readline().split()
    C1[p] = c1
    C2[p] = c2

pre_order('A')
print()
in_order('A')
print()
post_order('A')
```