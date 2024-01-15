Test_Case = int(input())

y = 1
while y <= Test_Case:
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    C_list = []

    if N<M:
        for q in range(M-N+1):
            sum = 0
            for p in range(N):
                sum += A[p]*B[p+q]
            C_list.append(sum)
        Max_C_list = max(C_list)

    elif N>M:
        for q in range(N-M+1):
            sum = 0
            for p in range(M):
                sum += A[p+q]*B[p]
            C_list.append(sum)
        Max_C_list = max(C_list)

    else:
        for q in range(N):
                sum = A[q]*B[q]
                C_list.append(sum)
        Max_C_list = max(C_list)

    print("#" + str(y) + " " + str(Max_C_list))
    y += 1