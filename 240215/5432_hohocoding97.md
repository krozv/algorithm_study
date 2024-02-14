# 5432. 쇠막대기 자르기

### 첫 시도
시간초과... 5/20
```python
T = int(input())
for tc in range(1,1+T):
    data = input()
    N = len(data)   #총 길이
    stack = []      #여는 괄호를 만나면 넣어둘 stack
    metal_stick = []  #쇠막대기의 위치 정보를 담을 리스트 내부 요소들은 다음과 같을 거임 (left, right) 
    laser = []      #레이저의 위치를 담을 리스트
    #레이저와 쇠막대기에 대한 정보를 찾기
    for i in range(N):
        if data[i] == '(':          #i번째 데이터가 여는 괄호면
            stack.append(i)         #stack에 추가
        else:                       #i번째 데이터가 닫는 괄호면
            if stack:               #여는 괄호가 있었다면
                left = stack.pop()  #스택에서 빼라
                if i == left + 1:               #닫는괄호와 여는괄호의 위치차가 1뿐이라면
                    laser.append(left)          #laser에 왼쪽 정보를 넣어라
                else:                           #위치차가 2이상이면
                    metal_stick.append((left, i)) #metal_stick에 막대기의 왼쪽과 오른쪽 정보를 넣어라
 
    num_metal_stick = len(metal_stick)      #쇠막대의 개수 초기화(전혀 안잘렸다면 metal_stick개수만큼일 거니까)
    for left, right in metal_stick:
        for i in laser:             
            if left < i < right:    #레이저 위치가 left와 right사이면 막대기 개수 추가
                num_metal_stick +=1
     
    print(f'#{tc} {num_metal_stick}')
```
### 두번째 시도
시간초과... 9/20 그나마 조금더 풀렸음..
```python
T = int(input())
for tc in range(1,1+T):
    data = input()
    N = len(data)   #총 길이
    stack = []      #여는 괄호를 만나면 넣어둘 stack
    metal_stick = []  #쇠막대기의 위치 정보를 담을 리스트 내부 요소들은 다음과 같을 거임 (left, right) 
    laser = []      #레이저의 위치를 담을 리스트
    #레이저와 쇠막대기에 대한 정보를 찾기
    for i in range(N):
        if data[i] == '(':          #i번째 데이터가 여는 괄호면
            stack.append(i)         #stack에 추가
        else:                       #i번째 데이터가 닫는 괄호면
            if stack:               #여는 괄호가 있었다면
                left = stack.pop()  #스택에서 빼라
                if i == left + 1:               #닫는괄호와 여는괄호의 위치차가 1뿐이라면
                    laser.append(left)          #laser에 왼쪽 정보를 넣어라
                else:                           #위치차가 2이상이면
                    metal_stick.append((left, i)) #metal_stick에 막대기의 왼쪽과 오른쪽 정보를 넣어라
            else:
                metal_stick.append((-1,i))       #stack쌓인게 없이 닫힌괄호만 나오면 left=-1, right=i 인 쇠막대기라 생각
    while stack:
        left = stack.pop()
        metal_stick.append(left, N) #left부터 N까지 가는 막대라 생각하고 추가해 주기

    num_metal_stick = len(metal_stick)      #쇠막대의 개수 초기화(전혀 안잘렸다면 metal_stick개수만큼일 거니까)
    for left, right in metal_stick:
        for i in laser:
            if i > right:
                break       
            else:
                if left < i:
                    num_metal_stick +=1       

    print(f'#{tc} {metal_stick}')
```

### 세번째 시도
append할때 시간이 걸릴까봐 일단 적절하게 stack과 metal_stick과 laser를 [0]*N으로 만들어주고 했었음

시간초과 7/20 

시간 더 걸린듯....
```python
T = int(input())
for tc in range(1,1+T):
    data = input()
    N = len(data)   #총 길이
    top = -1
    stack = [0]*N      #여는 괄호를 만나면 넣어둘 stack
    stick_pos = 0
    metal_stick = [0]*N  #쇠막대기의 위치 정보를 담을 리스트 내부 요소들은 다음과 같을 거임 (left, right) 
    laser_pos = 0
    laser = [0]*N      #레이저의 위치를 담을 리스트
    #레이저와 쇠막대기에 대한 정보를 찾기
    for i in range(N):
        if data[i] == '(':          #i번째 데이터가 여는 괄호면
            top += 1
            stack[top] = i          #stack에 추가
        else:                       #i번째 데이터가 닫는 괄호면
            if top != -1:               #여는 괄호가 있었다면
                top -= 1
                left = stack[top+1]     #스택에서 빼라
                if i == left + 1:               #닫는괄호와 여는괄호의 위치차가 1뿐이라면
                    laser[laser_pos] = left
                    laser_pos += 1
                else:                           #위치차가 2이상이면
                    metal_stick[stick_pos] = ((left,i))
                    stick_pos += 1
            else:
                metal_stick[stick_pos] = ((left,i))
                stick_pos += 1

    num_metal_stick = stick_pos      #쇠막대의 개수 초기화(전혀 안잘렸다면 metal_stick개수만큼일 거니까)
    for j in range(stick_pos):
        left, right = metal_stick[j]
        for i in range(laser_pos):
            if laser[i] > right:
                break       
            else:
                if left < laser[i]:
                    num_metal_stick +=1       
    print(f'#{tc} {num_metal_stick}')

```

### ..
