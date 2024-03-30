# 18809.Gaaaaaaaaaarden
"""
0: 호수
1: 배양액을 뿌릴 수 없는 땅
2: 배양액을 뿌릴 수 있는 땅
R+G개 이상 10개 이하
"""
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

from itertools import combinations
from copy import deepcopy
N, M, G, R = map(int, input().split())
arr = [list(input().split()) for _ in range(N)]

coordi = []
# 배양액을 뿌릴 수 있는 땅 확인
for i in range(N):
    for j in range(M):
        if arr[i][j] == '2':
            coordi.append((i, j))

# 조합 계산
# 좌표를 넣지 않고, coordi 안의 index를 결정하는 형식으로!
comb = list(combinations(range(len(coordi)), G+R))
# 배양액을 뿌리기로 결정한 땅에 어떤 배양액을 뿌릴지 결정,,,,
# G, R로 표시할테야

green_lst = combinations(comb[0], G)
cnt = 0
max_flower = 0
for green in green_lst:
    cnt += 1
    for num in comb[0]:
        a, b = coordi[num]
        if num in green:
            arr[a][b] = ['G', 0]
        else:
            arr[a][b] = ['R', 0]
    print('---------------')
    print(cnt)
    arr2 = deepcopy(arr)
    flower = 0
    flag = True
    # 배양액 분포
    while flag:
        flag = False
        for i in range(N):
            for j in range(M):
                if arr2[i][j] == ('1' or '2'):
                    flag = True
                if arr2[i][j][0].isalpha() and arr2[i][j] != 'f':
                    for d in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                        ni = i + d[0]
                        nj = j + d[1]
                        if 0<=ni<N and 0<=nj<M and arr2[ni][nj] != '0' and arr2[ni][nj] != 'f':
                            # 배양액 존재할때 (G or R)
                            if arr2[ni][nj][0].isalpha():
                                # 같은 시간대에 뿌릴 경우 -> 꽃으로 변경
                                # print(arr2[ni][nj])
                                if arr2[ni][nj][1] == arr2[i][j][1] + 1 and arr2[ni][nj][0] != arr2[i][j][0]:
                                    arr2[ni][nj] = 'f'
                                    flower += 1
                                # 이미 배양액 존재하는 경우 -> pass
                                elif arr2[ni][nj][1] > arr2[i][j][1] and arr2[ni][nj][0] != arr2[i][j][0]:
                                    liq, t = arr2[i][j]
                                    arr2[ni][nj] = [liq, t + 1]
                            # 배양액 존재하지 않을 때 -> 배양액 뿌려줌
                            else:
                                liq, t = arr2[i][j]
                                arr2[ni][nj] = [liq, t+1]
        # print(flag, arr2)
                print(arr2)
    if max_flower < flower:
        max_flower = flower
print(max_flower)