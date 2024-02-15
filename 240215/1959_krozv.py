# 두 개의 숫자열
import sys
sys.stdin = open('input.txt', 'r')


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # 길이 비교. 짧은 리스트 = s, 긴 리스트 = b
    if N <= M:
        s, b = A, B
        sl, bl = N, M
    else:
        s, b = B, A
        sl, bl = M, N
    max_val = 0
    for i in range(bl-sl+1):
        val = 0
        for j in range(sl):
            # 처음 계산한 값을 최댓값으로 지정 후 비교
            if i == 0:
                max_val += s[j] * b[j]
            else:
                val += s[j] * b[j+i]
        if max_val < val:
            max_val = val
    print(f'#{t} {max_val}')

