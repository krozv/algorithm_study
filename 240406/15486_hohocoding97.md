# 15486.퇴사
### 코드
pypy-948ms
```python
import sys
input = sys.stdin.readline

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)] # [T, P]

# 일단 0~N까지 N+1개 리스트 만들기
dp = [0]*(N+1)
i = 0
for t, p in data:
    i += 1
    dp[i] = max(dp[i], dp[i-1]) #i일에 얻을 수 있는 이익은 그 전날 얻을 수 이익보다는 크거나 같을 것이므로
    fin_date = i + t -1
    if fin_date <= N: #마지막 끝나는 날이 퇴사하는 전날이거나 당일인 경우
        dp[fin_date] = max(dp[fin_date], dp[i-1] +p)
        # 상담 끝나는 날의 이익은 오늘전까지의 (최대이익과+P)와 (기존 상담 끝나는 날의 이익) 중 큰 값으로 초기화 
print(dp[-1]) #마지막 날 얻을 수 있는 이익 출력
```