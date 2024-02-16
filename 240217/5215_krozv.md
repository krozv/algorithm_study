# 5215. 햄버거 다이어트

```python
# 5215. 햄버거 다이어트
"""
재료에 대한 점수 + 재료에 대한 칼로리
정해진 칼로리 이하의 조합 중 가장 선호하는 햄버거 조합하라
"""
def f(i, n, cl, l):
    """
    :param i: 현재 위치 표시
    :param n: 총 재료 개수
    :param cl: 현재까지 계산된 칼로리
    :param l: 제한 칼로리
    :return: 최대 칼로리
    """
    global max_point
    if cl > l:
        return
    if i == n:
        point = 0
        for j in range(n):
            if bit[j]:
                point += table[j][0]
        if max_point < point:
            max_point = point
    else:
        bit[i] = 0
        f(i+1, n, cl, l)
        bit[i] = 1
        cl += table[i][1]
        f(i+1, n, cl, l)


T = int(input())
for t in range(1, T+1):
    N, L = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(N)]
    bit = [0] * N
    max_point = 0
    f(0, N, 0, L)
    print(f'#{t} {max_point}')
```