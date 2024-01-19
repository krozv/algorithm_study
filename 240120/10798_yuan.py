# 15*5의 * 으로된 행렬 만들기
grid_star = [['*'] * 15 for _ in range(5)]

#input 그리드 만들기
grid_input = [list(map(str, input())) for _ in range (5)]
print(grid_input)

#리스트 안의 리스트의 길이 각각 구하기

len_list = []
for innerlist in grid_input:
    x = len(innerlist)
    len_list.append(x)
len_list_int = list(map(int, len_list))
print(len_list_int)

##5개행의 길이 담은 len_list 활용해서 0행렬에 input 덮어씌우기
for i in range(5):
    for j in range(len_list_int[i]):
        grid_star[i][j] = grid_input[i][j]

print(grid_star)

# *아닌것만 세로로 읽기
words_columns = []
for j in range(15):
    for i in range(5):
        if grid_star[i][j] != '*':
            print(grid_star[i][j], end='')