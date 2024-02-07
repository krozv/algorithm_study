# 호준 찬스

# 빙고 카운트 함수 작성
def is_bingo(arr):
    rows = [0]*5
    cols = [0]*5
    left_cross = 0
    right_cross = 0
    bingo = 0

    for a in arr :
        rows[a[0]]+=1
        cols[a[1]]+=1
        if a[0] == a[1]:
            left_cross +=1
        if a[1] == 4 - a[0] :
            right_cross +=1
    if left_cross == 5:
        bingo +=1
    if right_cross ==5:
        bingo +=1
    for i in range(5):
        if rows[i] == 5:
            bingo +=1
        if cols[i] == 5:
            bingo +=1
    return bingo

# 빙고판 작성
square = [list(map(int, input().split())) for _ in range(5)]
# 숫자 부르기
numbers = [list(map(int, input().split())) for _ in range(5)]
###########


# 숫자 위치 확인
positions = [] #숫자 위치 인덱스

for i in range(5):
    for j in range(5):
        for k in range(5):
            if numbers[i][j] in square[k]:
                l = square[k].index(numbers[i][j])
                positions.append((k,l))
        if is_bingo(positions) >=3:
            print(len(positions))
            exit()
