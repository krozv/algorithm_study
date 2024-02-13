
# 재귀는 recursion error
# def f(N):
#     if N > 2 and memo[N] == 0:
#         memo[N] = f(N-1) + f(N-2)
#     return memo[N]
#
# N = int(input())
# memo = [0] * (N+1)
# memo[1] = 1
# memo[2] = 2
# result = f(N) % 15746
# print(result)


N = int(input())
N_lst = [0] * (N+1)
if N == 1:
    print(1)
elif N == 2:
    print(2)
else:
    N_lst[1] = 1
    N_lst[2] = 2
    for i in range(3,N+1):
        N_lst[i] =  (N_lst[i-1] + N_lst[i-2]) % 15746
    print(N_lst[N])

