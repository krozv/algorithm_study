def f(a, k):
    a = a * N
    if k == M - 1:
        return a
    else:
        return f(a, k + 1)


T = 10
for tc in range(1, T + 1):
    tc = int(input())

    N, M = map(int, (input().split()))
    print(f'#{tc} {f(N, 1)}')


# def cantor(a,M,k):
#     global N
#     if k == M:
#         return N
#     else:
#         a*N
#         cantor(a*N,M,k+1)
#

#
#
#
# cantor(N,M,0)
# print(N)
#
#     # print(f'#{tc} {res}')