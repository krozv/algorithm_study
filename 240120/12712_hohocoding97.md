### [12712. 파리퇴치3]([SW Expert Academy](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYyJy6Q6DHADFASu&contestProbId=AXuARWAqDkQDFARa&probBoxId=AYykQLN6u1gDFASu&type=USER&problemBoxTitle=%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98+Track+%28%EB%82%9C%EC%9D%B4%EB%8F%84+%EC%A4%91%29&problemBoxCnt=5))

```python
def catchFly_Plus(N,M,x,y,array): #스프레이를 십자가모양으로 뿌렸을때 잡히는 파리수 구하는 함
    sum_fly = -array[x][y]         
    for i in range(-M+1,+M):      
        if x+i >= 0 and x+i <N:   
            sum_fly += array[x+i][y] 
        if y+i >= 0 and y+i <N:      
            sum_fly += array[x][y+i]
    return(sum_fly)                
def catchFly_X(N,M,x,y,array): #스프레이를 X자모양으로 뿌렸을때 잡히는 파리수
    sum_fly = -array[x][y]
    for i in range(-M+1,M):
        if x+i>=0 and x+i < N:
            if y+i>=0 and y+i <N:
                sum_fly += array[x+i][y+i]
            if y-i>=0 and y-i<N:
                sum_fly += array[x+i][y-i]
    return(sum_fly)

T = int(input())
for test_case in range(1,T+1):
    N, M = map(int, input().split())  
    MMarray = []
    for _ in range(N):
        MMarray.append(list(map(int,input().split())))#배열입력받기
    catchNum = []
    for i in range(N):
        for j in range(N):
            catchNum.append(catchFly_Plus(N,M,i,j,MMarray))
            catchNum.append(catchFly_X(N,M,i,j,MMarray))
    print(f'#{test_case} {max(catchNum)}')
```

### 해결 전략

1. **+영역**으로 분사한 경우와 **X자 영역**으로 분사한 경우를 따로 생각함

    ->catchFly_Plus와 catchFly_X 두개의 함수로 나눔

2. 스프레이를 뿌린 중심 구역을 [x][y]라고 특정해 두고 [x][y]에 분사했을때 잡을 수있는 파리수를 구함.
   
   **+영역으로 잡은 파리수는**  위아래로 잡은 파리수 + 좌우로 잡은 파리수 - 중앙에서 잡은 파리수로 구할 수 있음(아래 그림 참고)

![](C:\Users\mrson\AppData\Roaming\marktext\images\2024-01-12-21-39-21-image.png)

X자 영역으로 잡은 파리수도 같은 방법으로 생각할 수 있음

![](C:\Users\mrson\AppData\Roaming\marktext\images\2024-01-12-21-39-47-image.png)

이때 스프레이 영역이 N*N 배열 밖으로 튀어나올 수 있으므로 **튀어나가지 않는 부분만** 생각해서 각영역의 파리수 더하기

<img title="" src="file:///C:/Users/mrson/AppData/Roaming/marktext/images/2024-01-12-22-19-28-image.png" alt="" width="610">

```python
def catchFly_Plus(N,M,x,y,array): #스프레이를 십자가모양으로 뿌렸을때 잡히는 파리수 구하는 함
    sum_fly = -array[x][y]        #스프레이 가운데 영역의 파리만큼 빼주기 
    for i in range(-M+1,+M):      #i는 -M+1,-M+2,~,0,~,M-1
        if x+i >= 0 and x+i <N:      #배열에서 튀어나가지 않는 부분만 골라서 
            sum_fly += array[x+i][y] #위아래 방향으로 해당부분의 파리 수 더하기
        if y+i >= 0 and y+i <N:      #배열에서 튀어나가지 않는 부분만 골라서
            sum_fly += array[x][y+i] #좌우 방향으로 해당부분의 파리 수 더하기
    return(sum_fly)                  #총 잡은 파리수를 반환 
```

X자 영역도 마찬가지로 진행

<img src="file:///C:/Users/mrson/AppData/Roaming/marktext/images/2024-01-12-22-18-03-image.png" title="" alt="" width="630">

```python
def catchFly_X(N,M,x,y,array): #스프레이를 X자모양으로 뿌렸을때 잡히는 파리수
    sum_fly = -array[x][y]    #스프레이 가운데 영역의 파리만큼 빼주기
    for i in range(-M+1,M):    # i는 -(M-1) ~ (M-1)까
        if x+i>=0 and x+i < N:
            if y+i>=0 and y+i <N:
                sum_fly += array[x+i][y+i]
            if y-i>=0 and y-i<N:
                sum_fly += array[x+i][y-i]
    return(sum_fly)
```

N*N배열의 모든 위치에서 +영역과 X영역으로 뿌려서 잡은 파리수들을 배열에 넣기

```python
for i in range(N):
        for j in range(N):
            catchNum.append(catchFly_Plus(N,M,i,j,MMarray))
            catchNum.append(catchFly_X(N,M,i,j,MMarray))
```

 max함수를 이용해 catchNum에 담긴 수 중에서 가장 큰 값을 출력

```python
print(f'#{test_case} {max(catchNum)}')
```
