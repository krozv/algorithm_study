def best_time_for_stock(price_list):
    min = price_list[0]
    max = price_list[0]
    profit = 0
    N = len(price_list)

        for i in range(1, N-1):
            if max < price_list[i]:
                max = price_list[i]
                # ....? 알아서 잘 해보기..!
            if min > price_list[i] # min값 구해야 함
            
            if profit < max - min:
                profit = max - min



prices = list(map(int, input().split()))       # 입력을 prices = [1, 2, 3, 4] 이런 식으로 받던데..?
best_time_for_stock(prices)
