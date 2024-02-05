# 2578. 빙고

40ms
```python
def num_of_bingo(A:list):
    row_bingo = [0]*5 
    col_bingo = [0]*5
    cross1_bingo = 0
    cross2_bingo = 0
    bingo_count = 0 # 빙고 수
    #위치 정보를 순회
    for a in A:
        row_bingo[a[0]] += 1
        col_bingo[a[1]] += 1
        if a[0] == a[1]:
            cross1_bingo += 1
        if a[0]+a[1] == 4:
            cross2_bingo += 1
    if cross1_bingo == 5:
        bingo_count += 1
    if cross2_bingo == 5:
        bingo_count += 1
    for i in range(5):
        if row_bingo[i] == 5:
            bingo_count += 1
        if col_bingo[i] == 5:
            bingo_count += 1
    return bingo_count


arr = [list(map(int, input().split())) for _ in range(5)] #빙고 판
game = [list(map(int, input().split())) for _ in range(5)] #사회자가 부른 숫자
positions = [] #사회자가 숫자를 불러주면 위치를 저장할 리스트

count = 0 #사회자가 불러주는 숫자 개수
for i in range(5):
    for j in range(5):
        for x in range(5):
            #arr의 각 열에서 원하는 값이 존재하는지 확인 후 
            #존재할 경우 그 위치를 찾아서 positons에 추가
            if game[i][j] in arr[x]:
                y = arr[x].index(game[i][j])
                positions.append((x,y))
        count += 1
        #3빙고 이상인 경우 count 출력
        if num_of_bingo(positions) >= 3: 
            print(count)
            exit()
```

### 어느 똑똑이의 코드..

```python
board = [list(map(int, input().split())) for _ in range(5)]
ch = [0] * 12
#ch 0~4는 각 행에 해당하는 개수, 5~9는 각 열에 해당하는 수
#ch10은 왼쪽위에서 오른쪽아래 대각선, ch11은 오른쪽위 -왼쪽 아래 대각선에 해당하는 개수
hashmap = {board[r][c] : (r, c) for r in range(5) for c in range(5)}

res = 0
tmp = False
for _ in range(5):
    num_list = list(map(int, input().split()))
    if tmp:
        break
    for num in num_list:
        res += 1
        ch[hashmap[num][0]] += 1
        ch[hashmap[num][1] + 5] += 1
        if hashmap[num][0] ==hashmap[num][1]:
            ch[-2] += 1

        if sum(hashmap[num]) == 4:
            ch[-1] += 1

        if ch.count(5) >= 3:
            print(res)
            tmp = True
            break

```