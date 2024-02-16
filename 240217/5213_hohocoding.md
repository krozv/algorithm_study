# 5213. 거듭 제곱
### 처음 푼 방법
149ms
```python
def f(num, b, e): #b는 밑, e는 지수
    if e == 0:
        return num
    return f(num*b, b, e-1)

for _ in range(10):
    tc = int(input())
    base, exponent = map(int, input().split())
    print(f'#{tc} {f(1,base,exponent)}')
```

### 두번째 푼 방법
157ms
```python
def f(b, e): #b는 밑, e는 지수
    global num
    if e == 0:
        return
    num *= b
    f(b, e-1)
     
for _ in range(10):
    tc = int(input())
    base, exponent = map(int, input().split())
    num = 1
    f(base,exponent)
    print(f'#{tc} {num}')
```