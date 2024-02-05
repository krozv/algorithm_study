# 2578. 빙고
"""
선이 세 개 이상 그어지는 순간 빙고
사회자가 몇 번째 수를 부른 후 철수가 빙고를 외치rp 되는 지 출력
"""
def 힝..

def find_bingo(arr: [], bingo: int) -> int:
#########여기 다시 #######################
    return bingo


import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
arr = [list(map(int, input().split())) for _ in range(5)]
num_list = [list(map(int, input().split())) for _ in range(5)]
bingo = 0
# 입력 받은 숫자를 0으로 변환
while bingo < 3:
    for num in num_list:
        for i in range(5):
            for j in range(5):
                if arr[i][j] == num:
                    arr[i][j] = 0
                    bingo = find_bingo(arr, bingo)
                    if bingo == 3:
                        print(i+j+1)
                        break
                print(arr)
# 가로 세로 대각선에 0으로만 채워진 배열 개수 count

# count = 3 되는 순간 종료


