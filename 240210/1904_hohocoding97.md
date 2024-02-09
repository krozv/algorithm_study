# 1904. 01타일
### 첫 시도
메모리 초과...
```python
N = int(input())
N_list = [0] *(N+1)             
N_list[0], N_list[1]= 1, 1

for i in range(2, N+1):
    N_list[i] = N_list[i-1]+N_list[i-2]
print(N_list[N]%15746)
```

### 두번째 시도
`(a + b)%n` 과 `a%n + b%n` 가 서로 같은 것을 이용
336ms
```python
N = int(input())
N_list = [0] *(N+2)
N_list[1], N_list[2]= 1, 2

for i in range(3, N+1):
    N_list[i] = (N_list[i-1] +N_list[i-2])%15746
print(N_list[N])
```