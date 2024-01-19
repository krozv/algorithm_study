## swea 1974. 스도쿠 검증
```python
# 가로로 겹치는 숫자가 있는지 확인하는 함수
    for i in range(9):
def rowProblemCheck(arr): 
        if sorted(arr[i]) == [j for j in range(1,10)]:
            pass
        else:
            return False
    return True

# 세로로 겹치는 숫자있는지 확인하는 함수
def columnProblemCheck(arr):
    for column in range(9):
        columnProblemCheck_list = []
        for row in range(9):
            columnProblemCheck_list.append(arr[row][column]) 
        columnProblemCheck_list.sort()
        if not columnProblemCheck_list == [k for k in range(1,10)]:
            return False
    return True
    
#3*3영역에서 겹치는 숫자 있는지 확인하는 함수
def threethreeProblemCheck(arr): 
    for i in range(9): # 9개의 3*3리스트
        array_33 = []
        for j in range(3): # 3*3리스트의 9개 요소
            array_33.append(arr[(i//3)*3+j][(i%3)*3]) 
            array_33.append(arr[(i//3)*3+j][(i%3)*3+1])
            array_33.append(arr[(i//3)*3+j][(i%3)*3+2])
        if not sorted(array_33) == [k for k in range(1,10)]:
            return False
    return True

T = int(input())
for test_case in range(1,T+1):
    puzzle = []
    for _ in range(9):
        puzzle.append(list(map(int, input().split())))

    #앞에 정의한 3가지 함수가 모두 True인 경우 1프린트
    if rowProblemCheck(puzzle) and columnProblemCheck(puzzle) and threethreeProblemCheck(puzzle): 
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')
```