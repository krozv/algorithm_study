# 121.Best Time to Buy and Sell Stock
### 브루트 포스로 풀이
198/212 시간초과..
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        max_profit = 0
        for i in range(N-1):
            for j in range(i+1, N):
                profit = prices[j] - prices[i]
                if max_profit < profit:
                    max_profit = profit
        return max_profit
```

### 두번째 시도
200/212
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        max_profit = 0
        for i, price in enumerate(prices):
            if i < N-1:
                profit = max(prices[i+1:]) - price 
                if max_profit < profit:
                    max_profit = profit
        return max_profit
```
### 세번째 시도
198/212 또 시간초과
```python
class Solution:
    def maxProfit(self, prices):
        N = len(prices)
        max_profit = 0
        prices_dict = dict(zip(prices,[[] for _ in range(N)]))
        for date, price in enumerate(prices):
            prices_dict[price].append(date)
        sorted_prices = sorted(prices)  #오름차순으로 가격 정렬
        for idx, buy_price in enumerate(sorted_prices): #날짜와 가격 순회
            buy_date = prices_dict[buy_price][0]
            for sell_price in sorted_prices[N-1:idx:-1]:
                if prices_dict[sell_price][-1] > buy_date:
                    profit = sell_price - buy_price
                    if max_profit < profit:
                        max_profit = profit
        return max_profit
```

### 또 시간초과
198/212
```python
class Solution:
    def maxProfit(self, prices: list):
        prices_only1 = sorted(list(set(prices)))
        P = len(prices_only1)
        profit_set = set()
        for i in range(P - 1):
            for j in range(i + 1, P):
                profit_set.add(prices_only1[j] - prices_only1[i])
        sorted_profit = sorted(list(profit_set), reverse=True)  # 내림차순 정렬
        for profit in sorted_profit:  # 최대 이득부터 찾아보기
            for buy_price in prices_only1:
                buy_date = prices.index(buy_price)
                if profit+buy_price in prices[buy_date+1:]:
                    return profit
        return 0
```

### 그냥 답지 풀이

```python
class Solution:
    def maxProfit(self, prices: list):
        profit = 0
        min_price = prices[0]
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price-min_price)
        return profit
```