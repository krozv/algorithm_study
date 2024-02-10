def best_time_for_stock(price_list):
    min = price_list[0]
    max = price_list[0]
    profit = 0
    N = len(price_list)

        for i in range(1, N):
            if max < price_list[i]:
                max = price_list[i]
            elif i < N-1:
                if profit < max - min:
                    profit = max - min
                min = price_list[i]
                max = price_list[i]

            else:
                if profit < max - min:
                    profit = max - min


prices = list(map(int, input().split()))       # 입력을 prices = [1, 2, 3, 4] 이런 식으로 받던데..?
best_time_for_stock(prices)