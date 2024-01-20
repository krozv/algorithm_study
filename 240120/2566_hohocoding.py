new_dict ={}
for row in range(1,10):
    temp_list = list(map(int, input().split()))
    max_num = max(temp_list) #각 행의 최댓값
    max_position =(row, 1+temp_list.index(max_num)) #최댓값의 행렬 / 1을 더하는 이유는 1열부터 시작이므로
    new_dict[max_num] = max_position #key가 각행의 최댓값이고 value가 위치인 딕셔너리를 9개 요소 추가

print(max(new_dict))
print(new_dict[max(new_dict)][0], end=' ')
print(new_dict[max(new_dict)][1])