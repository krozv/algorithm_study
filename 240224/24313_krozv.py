# 24313. 알고리즘 수업 - 점근적 표기 1
"""
f(n) = a1*n + a0
O(g(n)) = f(n) <= c * g(n)
"""
def f(n):
    return a1 * n + a0


def g(n):
    return c * n


a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

if f(n0) <= g(n0):
    if c == a1:
        print(int(a0 < 0))
    else:
        print(int(n0 >= (a0 / (c - a1))))
else:
    print(0)