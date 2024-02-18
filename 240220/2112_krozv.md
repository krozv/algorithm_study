# 2112. 보호필름

```python
# 2112. 보호 필름
"""
두께 D, 가로 W
합격기준 K...
세로로 동일 특성 3개 이상이어야 해당 세로가 통과
약품은 가로로만 적용 가능
약품 투입 횟수를 최소로 하여 성능검사를 통과할 수 있는 방법 찾기
약품 투입하지 않고도 성능검사 통과하면 0
조건
3 <= D <= 13
1 <= W <= 20
1 <= K <= D
특성 A or B
"""
"""
1. 완전탐색 + q + 순열
2. 성능검사 실시
3. q 시작
"""
def injection(i):
    # i만큼 약품 투입 -> 투입할 줄 순열로 선정 -> 0으로 바꿀건지 1로 바꿀건지...ㅎ -> 시간초과 나는 거 아닐까 모르겠넹
    c = list(combinations(list(range(D)), i))
    p = list(product([0, 1], repeat=i))
    for col in c: # [0, 1, 2] 변경할 줄 정보
        col = list(col)
        for spec in p:  # 변경 정보 [0, 0, 0]
            spec = list(spec)
            # 선정된 순열만 특성 변경
            pre_info = []
            for j in range(len(col)):
                pre_info.append(film[col[j]])
                film[col[j]] = [spec[j] for _ in range(W)]
            # 특성 변경 후 성능검사 실시
            if test(film):
                print(f'#{t} {i}')
                return 1
            # 성능검사 완료 후 원상복귀
            for j in range(len(col)):
                film[col[j]] = pre_info[j]
    return 0

def test(arr):
    """
    :param arr: 성능검사
    :return: 테스트 통과하면 1, 아니면 0
    """
    for j in range(W):
        q = deque()
        for i in range(D):
            q.append(arr[i][j])
        # 성능검사
        cnt = 1
        while q:
            c = q[-1]
            q.pop()
            if cnt == K:
                if j == W-1:
                    return 1
                break
            if q:
                if c == q[-1]:
                    cnt += 1
                else:
                    cnt = 1
        else:
            return 0



import sys
from itertools import combinations, product
from collections import deque
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    D, W, K = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(D)]  # D * W
    # 약품 주입이 필요한 경우
    if not test(film):
        for k in range(1, K+1):
            if injection(k):
                break
    # 약품 주입 안해도 되는 경우
    else:
        print(f'#{t} 0')
```