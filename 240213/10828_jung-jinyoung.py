import sys

def push(item):
    global top
    stack.append(item)
    top += 1

def pop():
    global top
    if len(stack):
        top -= 1
        return stack.pop()
    else:
        return -1
def empty(stack):
    if stack: #스택에 들어 있으면
        return 0
    else: # 빈 스택
        return 1

stack = []
top = -1

N = int(sys.stdin.readline())
for _ in range(N):
    order = sys.stdin.readline().split() # '명령', '숫자'
    if order[0] == 'push':
        push(order[1])

    if order[0] == 'pop' :
        print(pop())

    if order[0] == 'size':
        print(top+1)
        # len 함수 사용 X (시간 초과)

    if order[0] == 'empty':
        print(empty(stack))

    if order[0] == 'top':
        if top == -1: # 빈 스택일 경우
            print(top)
        else:
            print(stack[top])