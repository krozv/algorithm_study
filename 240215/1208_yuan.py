T = 10
for tc in range(1, T + 1):
    cnt = int(input())
    lst = list(map(int, input().split()))

    while cnt > 0:
        # 큰값 작은값구하기
        mn_num = min(lst)
        mx_num = max(lst)

        # 큰값인덱스 작은값인덱스 구하기
        mn_idx = [idx for idx, num in enumerate(lst) if num == mn_num]
        mx_idx = [idx for idx, num in enumerate(lst) if num == mx_num]

        # 여러개일경우 아무거나 한개
        mn_idx = mn_idx[0]
        mx_idx = mx_idx[0]

        # 덤프
        lst[mn_idx] += 1
        lst[mx_idx] -= 1

        cnt -= 1

    print(f'#{tc} {max(lst) - min(lst)}')