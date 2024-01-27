# 1929. 소수 구하기

M이상 N이하의 소수를 모두 출력

소수는 하나 이상 있는 입력

```python
import sys
import math


def check_prime_num(num):
    for divisor in range(2, math.ceil(num**0.5+1)):
        if num % divisor == 0:
            return False
    return True


M, N = map(int, sys.stdin.readline().split())
check = True
for num in range(M, N+1):
    if num == 1:
        continue
    elif num == 2:
        print(2)
    else:
        check = check_prime_num(num)
        if check:
            print(num)
```