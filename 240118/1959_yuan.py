T = int(input())

for t in range (1,T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N<M:
        sum_list = []
        for i in range(M-N+1):
            sum = 0
            for j in range(N):
                sum += A[j] * B[i+j]
            sum_list.append(sum)
        print(f'#{t} {max(sum_list)}')

    elif N==M:
        for i in range(N):
            sum = 0
            sum += A[i] * B[i]
        print(f'#{t} {max(sum)}')

    elif N>M:
        sum_list = []
        for i in range(N-M+1):
            sum = 0
            for j in range(M):
                sum += A[i+j] * B[j]
            sum_list.append(sum)
        print(f'#{t} {max(sum_list)}')
