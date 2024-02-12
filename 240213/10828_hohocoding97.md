# 10828 스택
### 첫시도
python3 - 시간초과, pypy3 - 시간초과..
```python
N = int(input())
stack = []          
for _ in range(N):
    order = input().split()
    if order[0] == 'push':
        stack.append(order[1])
    elif order[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(stack))
    elif order[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif order[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
```

### 2번째 시도
시간초과...
```python
def push(num):
    global top
    top += 1
    stack[top] = num
    return 
def pop():
    global top
    if top == -1:
        return -1
    else:
        top -= 1
        return stack[top+1]
def empty():
    if top == -1:
        return 1
    else:
        return 0
def Top():
    if top == -1:
        return -1
    else:
        return stack[top]

N = int(input())
stack = [0]*N
top = -1          
for _ in range(N):
    order = input()
    if order == 'pop':
        print(pop())
    elif order == 'size':
        print(top+1)
    elif order == 'empty':
        print(empty())
    elif order == 'top':
        print(Top())
    else:   #push x 인 경우
        split_order = order.split()
        push(split_order[1])
```

참고로 `함수명`이랑 `변수명` 같으면 오류 발생함

`top`이란 변수랑 `top()`이라는 함수 같이 쓰면 안 돼...

### 입력을 한번에 받은 후 출력하는 방식으로 변경
python3 - 412ms
```python
def push(num):
    global top
    top += 1
    stack[top] = num
    return 
def pop():
    global top
    if top == -1:
        return -1
    else:
        top -= 1
        return stack[top+1]
def empty():
    if top == -1:
        return 1
    else:
        return 0
def Top():
    if top == -1:
        return -1
    else:
        return stack[top]

N = int(input())
stack = [0]*N
top = -1          
orders = [input() for _ in range(N)]
for i in range(N):
    if orders[i] == 'pop':
        print(pop())
    elif orders[i] == 'size':
        print(top+1)
    elif orders[i] == 'empty':
        print(empty())
    elif orders[i] == 'top':
        print(Top())
    else:   #push x 인 경우
        split_order = orders[i].split()
        push(split_order[1])
```

### 처음 방법에서 `sys.stdin.readline()`사용
48ms
```python
import sys
N = int(input())
stack = []          
for _ in range(N):
    order = sys.stdin.readline().split()
    if order[0] == 'push':
        stack.append(order[1])
    elif order[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(stack))
    elif order[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif order[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
```
참고로 `sys.stdin.readline()`은 개행문자(\n)가 따라오므로 주의