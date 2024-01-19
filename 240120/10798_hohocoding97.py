import sys
matrix = [[None]*15 for _ in range(5)] #최대행과 최대열이 각 5,15 인 2차원 리스트 생성
for row in range(5):
    temp_str = sys.stdin.readline().strip() #각줄의 입력을 temp_str에 저장

    for col in range(len(temp_str)): 
        matrix[row][col] = temp_str[col]

#세로로 읽기 위해 column이 바깥쪽 for문에 들어감
for column in range(15):
    for row in range(5):
        if not matrix[row][column] == None:
            print(matrix[row][column], end ='')
