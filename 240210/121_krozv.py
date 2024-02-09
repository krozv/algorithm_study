# 12. 주식을 사고팔기 가장 좋은 시점
"""
1st
exhaustive search -> # 199 에서 Time Limit Exceeded

class Solution:
    def maxProfit(self, prices: [int]) -> int:
        profit = 0
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                if prices[i] < prices[j]:
                    if profit < (prices[j] - prices[i]):
                        profit = prices[j] - prices[i]
        return profit
"""
"""
2nd
-> # 200 에서 Time Limit Exceeded

class Solution:
    def maxProfit(self, prices: [int]) -> int:
        profit = 0
        for i in range(len(prices)-1):
            current = prices[i]
            future = max(prices[i+1:])
            if current < future:
                if profit < (future - current):
                    profit = future - current
        return profit
"""
"""
3rd
stack을 활용해볼까?
top이 올라갈수록 마지막 stack보다 작은 값의 인덱스만 stack에 추가
그 인덱스를 기준으로 최솟값의 차이를 구하기
-> 통과는 했는데 Runtime = 2931ms...ㅎ

class Solution:
    def maxProfit(self, prices: [int]) -> int:
        profit = 0
        min_value = [0]
        if len(prices) == 1:
            return profit
        else:
            for i in range(len(prices)-1):
                if prices[i] < prices[min_value[-1]]:
                    min_value.append(i)
            for idx in min_value:
                current = prices[idx]
                future = max(prices[idx+1:])
                if profit < (future - current):
                    profit = future - current
            return profit
"""
"""
4th
시간 단축 방법 생각해보기..ing

"""
class Solution:
    def maxProfit(self, prices: [int]) -> int:
        profit = 0

        return profit


c = Solution()
prices = [1]
print(c.maxProfit(prices))