class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        N = len(prices)
        i = 0
        buy_cost = prices[i]
        rev = prices[i] - buy_cost

        while i < N:
            if prices[i] < buy_cost:
                buy_cost = prices[i]
            if rev < prices[i] - buy_cost:
                rev = prices[i] - buy_cost
            i += 1
        return rev