# 1959. 두 개의 숫자열

### 내 풀이 방법
151ms
```python
T = int(input())
for tc in range(1, 1+T):
    A, B = map(int, input().split())    #각 리스트 길이
    A_list = list(map(int, input().split()))
    B_list = list(map(int, input().split()))
    max_sum = 0
    if A >= B:
        for i in range(A-B+1):
            sum = 0
            for j in range(B):
                sum += A_list[j+i] * B_list[j]
            if max_sum < sum:
                max_sum = sum
    else:
        for i in range(B-A+1):
            sum = 0
            for j in range(A):
                sum += B_list[j+i] * A_list[j]
            if max_sum < sum:
                max_sum = sum
    print(f'#{tc} {max_sum}')
```

### 다른 사람거..
```python
t = int(input())
for test in range(1,t+1):
    n, m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    if n>m:
        n,m = m,n
        a,b = b,a
    max_sum =[]
    while len(b) >= n:
        sum = 0
        for i in range(n):
            sum += a[i]*b[i]
        max_sum.append(sum)
        b.remove(b[0])
    print("#{}".format(test),max(max_sum))
```