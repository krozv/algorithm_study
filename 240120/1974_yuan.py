TestCase = int(input())

def rows(user_input):
    for i in range(9):
        row = user_input[i]
        set_row = set(row)
        if len(set_row) == 9:
            continue
        else:
            return False
    return True

def squares(user_input):
    for i in range(0, 9, 3):
        square1 = user_input[i][0:3] + user_input[i + 1][0:3] + user_input[i + 2][0:3]
        square2 = user_input[i][3:6] + user_input[i + 1][3:6] + user_input[i + 2][3:6]
        square3 = user_input[i][6:9] + user_input[i + 1][6:9] + user_input[i + 2][6:9]

        if len(set(square1)) == 9 and len(set(square2)) == 9 and len(set(square3)) == 9:
            continue
        else:
            return False
    return True

def columns(user_input):
    for i in range(9):
        column = [user_input[j][i] for j in range(9)]
        set_column = set(column)

        if len(set_column) == 9:
            continue
        else:
            return False
    return True

for i in range(1, TestCase + 1):
    user_input = [list(map(str, input().split())) for _ in range(9)]

    if rows(user_input) and squares(user_input) and columns(user_input):
        print(f'#{i} 1')
    else:
        print(f'#{i} 0')
