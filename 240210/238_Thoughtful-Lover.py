def multiple_except(num_list):
    multiple_list = []
    N = len(num_list)

    for i in range(N):
        multiple = 1

        if i+1 < N:
            j = i+1
            for j in range(N):
                multiple *= num_list[j]

        if i > 0:
            for k in range(i):
                multiple *= num_list[k]

        multiple_list.append(multiple)

    print(multiple_list)


nums = list(map(int, input().split()))       # 입력을 num = [1, 2, 3, 4] 이런 식으로 받던데..?
multiple_except(arr)
