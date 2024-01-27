# 1929. 소수 구하기

### 시도1

시간초과..
```python
def is_prime_num(num):
    i = 2 #num이 소수인지 확인하도록 도와줄 인자
    while num//2 >= i: 
        if num % i == 0:
            return False
        else:
            i += 1 #i로 나눠지지 않으면 1증가
    return True

M,N = map(int, input().split())
for num in range(M,N+1):#M에서 N까지의 수 순회
    if is_prime_num(num): #함수에서 소수라 판단한 경우
        print(num)
```

### 시도2
시간초과...

```python
M,N = map(int, input().split())
for num in range(M,N+1):#M에서 N까지의 수 순회
    i = 2
    while True:
        if num == 2:
            print(2)
            break
        if num**0.5 < i:
            print(num)
            break
        elif num % i == 0:
            break
        else:
            i += 1

```