
#인풋을 9*9 격자로 바꿈
grid = [list(map(int, input().split())) for _ in range (9)]


#격자판 숫자들 grid_list에 넣기
grid_list = []
for i in range(9):
    for j in range(9):
        x = grid[i][j]
        grid_list.append(x)

 #제일 큰 숫자 max_number 구하고 출력
max_number = max(grid_list)
print(max_number)

# 현재 격자판의 숫자 제일 큰 숫자일때 몇행 몇열인지 출력
for i in range(9):
    for j in range(9):
        if max_number == grid[i][j]:
            print(i+1,j+1)