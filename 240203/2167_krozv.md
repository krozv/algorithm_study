```python
# 2167. 2차원 배열의 합
"""
2차원 배열 주어짐
(i, j) -> (x, y) 위치까지 수들의 합 구하기
N, M (1<=N, M <= 300)
수의 절댓값 10,000보다 작거나 같은 정수! (음수 있음 유의할 것)
K 합을 구할 부분의 개수 1 <= K <= 10,000
"""
# 입력 받음
import sys

# 가장 시간 많이 걸림
N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
K = int(sys.stdin.readline())
cnt = [[0] for _ in range(K)]

for k in range(K):
    i, j, x, y = map(int, sys.stdin.readline().split())
    for r in range(i-1, x):
        for c in range(j-1, y):
            cnt[k][0] += arr[r][c]

for k in range(K):
    print(cnt[k][0])
```