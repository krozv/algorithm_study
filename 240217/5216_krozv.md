# 5216. 거듭 제곱

```python
"""
두 개의 숫자 N, M이 주어질 때, N의 M 거듭제곱 값을 구하는 프로그램
재귀호출 이용할 것
결과 값 int
"""
def f(i, j):
    """
    :param i: 밑
    :param j: 지수
    :return: 계산값
    """
    if j == M:
        return i
    else:
        return f(i*N, j+1)

T = 10
for t in range(1, T+1):
    _ = input()
    N, M = map(int, input().split())
    print(f'#{t} {f(N, 1)}')
```