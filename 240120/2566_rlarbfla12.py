table = []
for i in range(9):
    row = list(map(int, input().split()))
    table.append(row)

max_num = 0
max_row = 0
max_column = 0

for row in range(9):
    for column in range(9):
        if max_num <= table[row][column]:
            max_row = row + 1
            max_column = column + 1
            max_num = table[row][column]

print(max_num)
print(max_row, max_column)