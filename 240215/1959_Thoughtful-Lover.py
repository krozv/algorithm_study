'''
두 개의 숫자열
N개의 길이를 가지는 숫자열과 M개의 길이를 가지는 숫자열 (3 <= N, M <= 20)
두 수열이 서로 마주보는 숫자들을 곱한 뒤 모두 더할 때 최댓값을 구하라
'''


def f(k, l):        # 두 수열을 입력 받음
    m = 0       # 최댓값을 저장할 변수 m 을 정의

    if M >= N:      # 아래의 수열이 위의 수열보다 길 경우
        for i in range(M-N+1):      # 작은 수열이 긴 수열 위를 움직이도록
            cnt = 0     # 곱의 합을 임시로 저장할 변수 cnt
            for j in range(N):      # 작은 수열 만큼 곱셈을 시행
                cnt += k[j] * l[j+i]
            if m < cnt:     # 최대값을 갱신
                m = cnt
    else:       # 수열의 길이가 반대인 경우 나머지는 상동
        for i in range(N-M+1):
            cnt = 0
            for j in range(M):
                cnt += l[j] * k[j+i]
            if m < cnt:
                m = cnt

    return m


T = int(input())
for tc in range (1, T+1):
    N, M = map(int, input().split())        # 수열 A와 B의 길이 N과 M
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    print(f'#{tc} {f(A, B)}')