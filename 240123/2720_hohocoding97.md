# 2720. 세탁소 사장 동혁

```python
import sys
T = int(input())
for _ in range(T):
    C = int(sys.stdin.readline()) #거스름돈
    coin_value = (25,10,5,1)#쿼터,다임,니켈,페니의 가치
    coin_count= []
    for v in coin_value:
        coin_count.append(C // v)
        C = C % v

    list(map((lambda i : print(coin_count[i], end=' ')), list(range(4))))
    print()
```
