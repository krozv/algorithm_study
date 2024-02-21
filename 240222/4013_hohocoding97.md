# 4013.특이한 자석
### 코드
227ms
```python
#8개의 날이 달린 자석이 4개 있음
#N극은 0, S극은 1로 표현
#빨간색 화살표 위치는 0번 인덱스
#왼쪽 자석의 2번 인덱스와 오른쪽 자석의 인덱스의 6번인덱스가 다른 값일 경우 기어는 반대쪽으로 회전
#빨간색 화살표가 S극 일때 자석순서대로 1, 2 ,4 ,8 점 획득. 최종 점수 구해

from collections import deque

# 회전시켜야 할 정보를 이중리스트로 저장해서 반환
def find_rotate(i, r):
    data = []
    data.append([i,r])# (자석 인덱스, 회전 방향) 저장
    copied_r = r
    copied_i = i
    while copied_i-1 >= 0:
        if magnets[copied_i-1][2] == magnets[copied_i][6]:
            break
        else:
            copied_r = -copied_r
            copied_i -= 1
            data.append([copied_i, copied_r])

    while i+1 < 4:
        if magnets[i][2] == magnets[i+1][6]:
            break
        else:
            r = -r
            i += 1
            data.append([i, r])
    return data

# 정보를 받아서 그대로 자석을 회전시키는 함수
def magnet_rotate(data):
    for datum in data:
        i, r = datum #i:자석 인덱스, r:회전방향
        if r == 1:  #시계 방향 회전해야할때
            #오른쪽에서 빼서 왼쪽에 넣기
            magnets[i].appendleft(magnets[i].pop())
        else:       #반시계 방향 회전해야 할때
            #왼쪽에서 빼서 오른쪽에 넣기
            magnets[i].append(magnets[i].popleft())
    return

T = int(input())
for tc in range(1, 1+T):
    K = int(input())
    magnets = [deque(map(int, input().split())) for _ in range(4)]
    changes = [list(map(int, input().split())) for _ in range(K)]

    for change in changes:
        m_num, rotate_dir = change
        rotate_list = find_rotate(m_num-1, rotate_dir) #회전시켜야할 자석과 방향 정보 구하기
        magnet_rotate(rotate_list) #가져온 정보로 자석 회전시키기

    sum = 0
    #점수 더하기
    for i, magnet in enumerate(magnets):
        if magnet[0] == 1: #S극이면 점수 얻음
            sum += 2**i
    print(f'#{tc} {sum}')
```