'''
창용마을에 사는 N명의 사람
1~N 번까지 번호가 붙어 있는 사람

두 사람이 서로 알거나 몇 사람 거쳐서 알 수 있는 관계라면
하나의 무리

몇 개의 무리가 있는지?
'''


# 서로 아는 사이를 표시하는 crowd 함수를 정의
def crowd(k):
    for i in adjl[k]:
        if know[i] == 0:
            know[i] = 1
            crowd(i)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    # 각 사람에게 인접한 사람을 저장할 adjl, 아는 사람 유무를 체크한 know, 연결된 관계망의 수를 셀 count
    adjl = [[] for _ in range(N+1)]
    know = [0] * (N+1)
    count = 0

    # 서로를 알고 있는 관계망을 adjl 에 저장
    for j in range(M):
        line = list(map(int, input().split()))
        adjl[line[0]].append(line[1])
        adjl[line[1]].append(line[0])

    # 연결 여부를 확인하고 하나의 탐색이 끝나면 count 1 증가
    for k in range(1, N+1):
        if know[k] == 0:
            crowd(k)
            count += 1

    print(f'#{tc} {count}')


