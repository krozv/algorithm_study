num = 9

max_num_list=[] #각 행의 최댓값을 저장할 리스트 
max_row, max_col = 0,0 # 최댓값의 행과 열을 저장할 변수 

for i in range (9):
    row_i = list(map(int,input().split()))
    max_num_i = max(row_i) #해당 행에서의 최댓값 산출
    max_num_list.append(max_num_i) # 입력된 값들 중에서 최댓값을 리스트에 추가

    if max(max_num_list) in row_i :
        max_row = i + 1
        max_col = row_i.index(max_num_i) + 1 #최댓값의 위치를 가져오기

print(max(max_num_list)) # 최댓값 출력
print(max_row, max_col) # 최댓값 위치 출력 

