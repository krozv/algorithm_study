N = list(map(int, input()))

# 0있는지 판별
if not N.count(0):
    print(-1)
# 3의 배수가 있는 지 판별
elif sum(N) % 3:
    print(-1)
# 가장 큰 30의 배수가 되도록
# 가장 뒤 0
else:
    N.sort(reverse=True)
    print(''.join(map(str, N)))