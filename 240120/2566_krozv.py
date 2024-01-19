# 2566 1차 풀이
import sys

data1 = []
for i in range(9):
    data1.append(list(map(int, sys.stdin.readline().split())))

data2 = []
for i in range(9):
    for j in range(9):
        data2.append(data1[i][j])
print(max(data2))
max_index = data2.index(max(data2))
print(max_index//9 + 1, max_index % 9 + 1)

# 2566 2차 풀이
# 메모리 31120 KB / 시간 40 ms
import sys

# input 값 리스트로 받음
input_list = []
for _ in range(9):
    input_list.append(list(map(int, sys.stdin.readline().split())))

# 최댓값을 찾기 위해 리스트 탐색
max_list = []
for row in input_list:
    i = input_list.index(row)
    max_list.append(max(row))
print(max(max_list))

# 최댓값의 위치를 찾기 위해 중첩 리스트 사용
for row in input_list:
    for elem in row:
        if max(max_list) == elem:
            print(input_list.index(row)+1, row.index(elem)+1)