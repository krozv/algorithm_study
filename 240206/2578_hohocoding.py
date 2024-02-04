def num_of_bingo(A:list):
    row_bingo = [0]*5 
    col_bingo = [0]*5
    cross1_bingo = 0
    cross2_bingo = 0
    bingo_count = 0 # 빙고 수
    #위치 정보를 순회
    for a in A:
        row_bingo[a[0]] += 1
        col_bingo[a[1]] += 1
        if a[0] == a[1]:
            cross1_bingo += 1
        if a[0]+a[1] == 4:
            cross2_bingo += 1
    if cross1_bingo == 5:
        bingo_count += 1
    if cross2_bingo == 5:
        bingo_count += 1
    for i in range(5):
        if row_bingo[i] == 5:
            bingo_count += 1
        if col_bingo[i] == 5:
            bingo_count += 1
    return bingo_count


arr = [list(map(int, input().split())) for _ in range(5)] #빙고 판
game = [list(map(int, input().split())) for _ in range(5)] #사회자가 부른 숫자
positions = []

count = 0
for i in range(5):
    for j in range(5):
        for x in range(5):
            #arr의 각 열에서 원하는 값이 존재하는지 확인 후 
            #존재할 경우 그 위치를 찾아서 positons에 추가
            if game[i][j] in arr[x]:
                y = arr[x].index(game[i][j])
                positions.append((x,y))
        count += 1
        if num_of_bingo(positions) >= 3:
            print(count)
            exit()