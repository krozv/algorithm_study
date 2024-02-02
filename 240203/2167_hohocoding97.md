# 2167. 2차원 배열의 합

### 첫 시도
시간초과...
```python
N, M = map(int, input().split())#1<= N,M <= 300,N은 행 개수, M은 열 개수
data = [list(map(int, input().split())) for _ in range(N)]#N*M 이차원배열 입력 받음
K = int(input()) #입력받을 부분 수

for _ in range(K):
    i, j, x, y = map(int, input().split())
    array_sum = 0
    for row in range(i-1, x): #i행부터 x행까지
        for col in range(j-1, y): #j행부터 y행까지
            array_sum += data[row][col]
    print(array_sum)

```
문제에서 `배열의 (i, j) 위치는 i행 j열을 나타낸다.`라고 나와 있어서 i, j를 인덱스로 사용 하려면 i-1, j-1로 넣어줘야 한다!


### 성공한 시도
`PyPy3` + `sys.stdin.readline()` 로 간신히 통과

```python
import sys
input = sys.stdin.readline
N, M = map(int, input().split())#1<= N,M <= 300,N은 행개수, M은 열 개수
data = [list(map(int, input().split())) for _ in range(N)]#N*M 이차원배열 입력 받음
K = int(input()) #입력받을 부분 수

for _ in range(K):
    i, j, x, y = map(int, input().split())
    array_sum = 0
    for row in range(i-1, x): #i행부터 x행까지
        for col in range(j-1, y): #j행부터 y행까지
            array_sum += data[row][col]
    print(array_sum)
```
- 간단한 코드상에서는 Python3가 메모리, 속도 측에서 우세함
- 복잡한 코드(반복)을 사용하는 경우에서는 PyPy3가 우세함