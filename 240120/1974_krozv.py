# 1974_스도쿠 검증
T = int(input())
num = list(range(1,10))

for t in range(T):
    puzzle = True
    sudoku = []
    output = []
# sudoku 만듦
    for _ in range(9):
        sudoku.append(list(map(int, input().split())))
    check = []
    # 3x3 칸 확인
    for x in range(0, 7, 3):
        for y in range(0, 7, 3):
            if not puzzle:
                break
            for i in range(x, x+3):
                for j in range(y, y+3):
                    check.append(sudoku[i][j])
            check.sort()
            if check != num:
                puzzle = False
                check = []
                break
            else:
                puzzle = True
                check = []
    # 가로 확인
    if puzzle:
        width = []
        for i in range(9):
            width.append(sudoku[i])
            a = sorted(width[i])
            if num != a:
                puzzle = False
                break
            else:
                puzzle = True
    # 세로 확인
    if puzzle:
        length = []
        for i in range(9):
            for j in range(9):
                length.append(sudoku[j][i])
            length.sort()
            if length != num:
                puzzle = False
                break
            else:
                puzzle = True
            length = []
    if puzzle:
        print(f'#{t+1} 1')
    else:
        print(f'#{t+1} 0')