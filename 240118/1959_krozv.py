T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # A와 B중에 어떤 value의 길이가 긴지 확인
    if len(A) >= len(B):
        big = A
        small = B
    else:
        big = B
        small = A

    multiply_elem = []
    for i in range(len(big) - len(small) + 1):
        output = 0
        for j in range(len(small)):
            output += big[i+j] * small[j]
        multiply_elem.append(output)
    print(f'#{t+1} {max(multiply_elem)}')
