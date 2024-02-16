# 햄버거 다이어트

### 백트래킹 사용한 코드
654ms
```python
#i는 현재 재료 번호
#cal은 i-1번째까지의 택한 재료의 칼로리합
#score는 i-1번째 재료까지 택한 재료의 점수 합
def f(i, cal, score): 
    global max_score
    if max_score < score:
        max_score = score
    if i == N:      #N-1번까지의 재료들에 대해서 넣을지 말지 정했으므로 되돌아간다.
        return
    else:
        #현재까지의 칼로리에서 i번째 칼로리를 더한게 L보다 크지 않은 경우
        if cal + data[i][1] <= L: 
            f(i+1, cal+data[i][1], score+data[i][0])  #i번째 재료를 택해서 칼로리와 점수를 더해줌. i+1번째 재료를 택할지 정하러 간다.
        f(i+1,cal,score)    #i번째 재료를 택하지 않고 i+1번째 재료를 어떻게 할지 정하러 간다.


T = int(input())
for tc in range(1, 1+T):
    N, L = map(int, input().split()) #N : 총 재료 수,  L: 최대 칼로리 한계
    data = [list(map(int, input().split())) for _ in range(N)] #[[맛점수, 칼로리] for _ in range(N)]
    max_score = 0
    f(0,0,max_score) #f(재료번호, 전까지 택한 재료들의 칼로리합, 전까지 택한 재료들의 점수 합)
    print(f'#{tc} {max_score}')
```