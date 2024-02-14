T = int(input())
for tc in range(1, T + 1):

    # a,b 받기
    a, b = map(int, input().split())
    a_lst = list(map(int, input().split()))
    b_lst = list(map(int, input().split()))

    # 작은게 무조건 n 큰게 m
    n = min(a, b)
    m = max(a, b)

    if len(a_lst) < len(b_lst):
        n_lst, m_lst = a_lst, b_lst
    else:
        n_lst, m_lst = b_lst, a_lst

    # 계산
    mx_s = 0
    for j in range(m - n + 1):
        s = 0
        for i in range(n):
            s += n_lst[i] * m_lst[i + j]

        if s > mx_s:
            mx_s = s
    print(f'#{tc} {mx_s}')