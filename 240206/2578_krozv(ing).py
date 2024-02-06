# 2740. 행렬 곱셈

# 2578. 빙고
"""
선이 세 개 이상 그어지는 순간 빙고
사회자가 몇 번째 수를 부른 후 철수가 언제 빙고?
코드에 지성이 없음ㅠ -> 수정할 것!
"""
def print_bingo(arr:[], num_list: []):
    for num in num_list:
        for i in range(5):
            for j in range(5):
                if arr[i][j] == num:
                    arr[i][j] = 0
                    bingo = find_bingo(arr)
                    if bingo >= 3:
                        return num_list.index(num) + 1

##########여기 수정해라###########
def find_bingo(arr: []) -> int:
    bingo = 0
    for i in range(5):
        if arr[i] == [0, 0, 0, 0, 0]:
            bingo += 1
        if arr[0][i] == 0 and arr[1][i] == 0 and arr[2][i] == 0 and arr[3][i] == 0 and arr[4][i] == 0:
            bingo += 1
    if arr[0][4] == 0 and arr[1][3] == 0 and arr[2][2] == 0 and arr[3][1] == 0 and arr[4][0] == 0:
        bingo += 1
    if arr[0][0] == 0 and arr[1][1] == 0 and arr[2][2] == 0 and arr[3][3] == 0 and arr[4][4] == 0:
        bingo += 1
    return bingo


import sys
input = sys.stdin.readline
arr = [list(map(int, input().split())) for _ in range(5)]
num_list = []

for _ in range(5):
    num_list += list(map(int, input().split()))

print(print_bingo(arr, num_list))