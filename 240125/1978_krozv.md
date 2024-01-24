# 1978. 소수 찾기

## Solution

주어진 수 number를 1부터 number-1까지 나누어서

나누어 떨어질 경우 break

나누어 떨어지지 않을 경우 prime number로 판별

```python
N = int(input())
dividend = list(map(int,input().split()))
prime_number = 0
for i in range(N):
    # divisor 생성
    for divisor in range(2, dividend[i]+1):
        # 소수인지 아닌지 판별
        if divisor == dividend[i]:
            prime_number += 1
        # 나누어떨어질 경우 소수가 아니므로 바로 break
        elif dividend[i] % divisor == 0:
            break
print(prime_number)
```