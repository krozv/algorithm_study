# 1978. 소수찾기

시간 : 40ms
```python
N = int(input())
nums = list(map(int,input().split()))

prime_count = 0 #소수개수 count
for num in nums:
    a = 2 #num이 소수인지 확인하도록 도와줄 녀석
    while num >= a:
        if num == a:
            prime_count += 1
        elif  num%a == 0:
            break
        a = a +1
print(prime_count)
```
### 해결 방법

```python
a = 2 #num이 소수인지 확인하도록 도와줄 녀석
    while num >= a:
        if num == a:
            prime_count += 1
        elif  num%a == 0:
            break
        a = a +1
```
num이 1과 자신이 아닌 다른 수에 나눠지면 소수가 아니므로 while문으로 a가 num과 같아지면 prime_count를 올림

자기자신이 아닌 다른 수에 나눠지면 break