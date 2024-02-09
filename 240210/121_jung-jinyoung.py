from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        min_price = prices[0] # 최소 구매 가격
        max_profit = 0 # 최대 이익 초기화

        for i in range(1, n):
            # 최소 구매 가격 업데이트
            if prices[i] < min_price:
                min_price = prices[i]
            # 최소 구매 가격일 경우 ,최대 이익 업데이트
            else:
                max_profit = max(max_profit, prices[i] - min_price)

        return max_profit
