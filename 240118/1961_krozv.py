def degree_90(List):
    l_90 = []
    for i in range(len(List)):
        b = ''
        for j in reversed(range(len(List))):
            a = str(List[j][i])
            b = b + a
        l_90.append(b)
    return l_90


def degree_180(List):
    l_180 = []
    for i in reversed(range(len(List))):
        b = ''
        for j in reversed(range(len(List))):
            a = str(List[i][j])
            b = b + a
        l_180.append(b)
    return l_180


def degree_270(List):
    l_270 = []
    for i in reversed(range(len(List))):
        b = ''
        for j in range(len(List)):
            a = str(List[j][i])
            b = b + a
        l_270.append(b)
    return l_270


T = int(input())
for k in range(T):
    N = int(input())
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))
    output = []
    for i in range(N):
        output.append(degree_90(L)[i])
        output.append(' ')
        output.append(degree_180(L)[i])
        output.append(' ')
        output.append(degree_270(L)[i])
        if i != N - 1:
            output.append('\n')
    print(f'#{k + 1}')
    print(''.join(output))
