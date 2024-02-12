### try 1
```py
import sys

def push(start, end):
    for i in range(start, end+1):
        stack.append(i)
        result.append('+')


# 현재 스택 길이에서 값이 위치한 자리까지 pop
def pop(n,k):
    for _ in range(n-k):
        pop_nums.append(stack.pop())
        result.append('-')


N = int(sys.stdin.readline())
stack = []
# 요구되는 수열 생성
request = [int(sys.stdin.readline()) for _ in range(N)]


pop_nums = []
result = []

# 첫번째 수열 값
i = 0
push(1, request[i])


print(time.time())
while i < N:
    # 다음 수열 값이 stack에 있을 경우
    if stack and request[i] in stack :
        n = len(stack)
        k = stack.index(request[i])
        pop(n,k)
        i+=1
    # 스택에 없을 경우
    elif request[i] not in stack:
        if request[i] in pop_nums: # 이미 pop 한 경우
            print('NO')
            exit()
        else:
            push(max(pop_nums)+1,request[i]) # push

for cal in result:
    print(cal)

```

> 시간 초과 발생 
> 1. 리스트 너무 많이 생성
> 2. max 등 리스트 함수 사용 많음  

-----

### try2

`필요 없는 리스트 삭제` : `pop_nums`  
`리스트 함수 사용 줄이기` : `max` 사용 X, `current_num`으로 변수 설정   
`push` : `current_num` ~ `현재 수열 값` 까지 
`출력 조건 변경` : `for 문` 사용 X , `.join` 사용 -> 한번에 문자열 합치기 
```py

import sys

def push(start, end):
    for i in range(start, end+1):
        stack.append(i)
        result.append('+')


def pop(n, k):
    for _ in range(n-k):
        result.append('-')


N = int(sys.stdin.readline())
stack = []

# 입력된 수열
request = [int(sys.stdin.readline()) for _ in range(N)]

result = []

i = 0 # request 인덱스 시작
current_num = 1  # push를 위한 현재 값 1 설정

while i < N:
    # 수열 값이 stack에 있을 경우 pop
    if stack and request[i] in stack:
        n = len(stack)
        k = stack.index(request[i])
        pop(n, k)
        i += 1

    # 현재 수열 값 보다 크거나 같으면 push
    elif request[i] >= current_num:
        push(current_num, request[i])
        current_num = request[i] + 1

    # 현재 수열 값보다 작거나 스택에 없을 경우
    else:
        print('NO')
        exit()

print('\n'.join(result))
```

