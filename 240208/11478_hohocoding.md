# 11478. 서로 다른 부분 문자열의 개수

### 첫 풀이
`append()`가 시간 많이 걸린다고 하여 미리 list를 일정개수 만들고 시작

python3-1376ms, pypy3-892ms
```python
S = input()
N = len(S)
subset = [0]*(N**2)             #최대가능한 부분집합 수 
i = 0
for l in range(1, N+1):         #l은 자를 문자열 길이
    for idx in range(N-l+1):    #idx는 문자열 시작 위치
        subset[i] = S[idx:idx+l] #subset의 i번 index에 부분문자열을 넣어줌
        i += 1
print(len(set(subset))-1)       #집합으로 변경해 겹치는 걸 제거후 0도 제거
```


### 마지막에 -1 안하고 풀려면
pypy3-688ms
```python
S = input()
N = len(S)
subset = [0]*(((N+1)*(N))//2)   #문제에 적합한 부분문자열을 만들 수 있는 최대 개수
i = 0
for l in range(1, N+1):         #l은 자를 문자열 길이
    for idx in range(N-l+1):    #idx는 문자열 시작 위치
        subset[i] = S[idx:idx+l] #subset의 i번 index에 부분문자열을 넣어줌
        i += 1
print(len(set(subset)))       
```