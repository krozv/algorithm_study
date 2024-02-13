'''
문제
정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 다섯 가지이다.

push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
입력
첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다.
주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

출력
출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.
'''


'''
# 1차_시간 초과

def stack_operation(command):       # 입력 받은 스택 연산을 처리하는 함수를 정의
    global top      # global 변수인 top을 호출

    if command[0] == 'push':        # stack 에 정수를 push
        stack.append(int(command[1]))
        top += 1
    elif command[0] == 'pop':       # stack 의 맨 위 수를 제거하고 반환
        if stack:
            print(stack.pop())
            top -= 1
        else:
            print(-1)
    elif command[0] == 'size':      # stack 의 크기를 확인
        print(len(stack))
    elif command[0] == 'empty':     # stack 이 비어 있는지 여부를 출력
        if stack:
            print(0)
        else: print(1)
    elif command[0] == 'top':       # stack 의 top 값을 출력
        if stack:
            print(stack[top])
        else:
            print(-1)


N = int(input())

stack = []
top = -1

for i in range(N):
    com = list(input().split())     # push 명령어가 있으므로, 리스트로 입력 받는다.
    stack_operation(com)
'''


'''
# 2차_시간초과
# 어디서 append가 시간이 오래 걸린다는 이야기를 들어서 stack = [0] * N 으로 정의
def stack_operation(command):       # 입력 받은 스택 연산을 처리하는 함수를 정의
    global top      # global 변수인 top을 호출

    if command[0] == 'push':        # stack 에 정수를 push
        top += 1
        stack[top] = int(command[1])
    elif command[0] == 'pop':       # stack 의 맨 위 수를 제거하고 반환
        if stack[top] == 0:
            print(-1)
        else:
            print(stack.pop(top))
            top -= 1
    elif command[0] == 'size':      # stack 의 크기를 확인
        print(len(stack[:top+1]))
    elif command[0] == 'empty':     # stack 이 비어 있는지 여부를 출력
        if stack[top] == 0:
            print(1)
        else: print(0)
    elif command[0] == 'top':       # stack 의 top 값을 출력
        if stack[top] == 0:
            print(-1)
        else:
            print(stack[top])


N = int(input())

stack = [0] * N
top = -1

for i in range(N):
    com = list(input().split())     # push 명령어가 있으므로, 리스트로 입력 받는다.
    stack_operation(com)
'''


'''
# 3차_시간초과
# 이번에는 이중 if가 문제인가 싶어서 전체를 if, elif로 구성해봤는데 또 시간초과,, 이쯤되면 뭔가 코드를 근본적으로 바꿔야할 것 같은디
def stack_operation(command):       # 입력 받은 스택 연산을 처리하는 함수를 정의
    global top      # global 변수인 top을 호출

    if command[0] == 'push':        # stack 에 정수를 push
        top += 1
        stack[top] = int(command[1])
    elif command[0] == 'pop' and stack[top] == 0:       # stack 의 맨 위 수를 제거하고 반환
        print(-1)
    elif command[0] == 'pop':
            print(stack.pop(top))
            top -= 1
    elif command[0] == 'size':      # stack 의 크기를 확인
        print(len(stack[:top+1]))
    elif command[0] == 'empty' and stack[top] == 0:     # stack 이 비어 있는지 여부를 출력
        print(1)
    elif command[0] == 'empty': print(0)
    elif command[0] == 'top' and stack[top] == 0:       # stack 의 top 값을 출력
        print(-1)
    else:
        print(stack[top])


N = int(input())

stack = [0] * N
top = -1

for i in range(N):
    com = list(input().split())     # push 명령어가 있으므로, 리스트로 입력 받는다.
    stack_operation(com)
'''


def stack_operation(command):       # 입력 받은 스택 연산을 처리하는 함수를 정의
    global top      # global 변수인 top을 호출

    if command[0] == 'push':        # stack 에 정수를 push
        stack.append(int(command[1]))
        top += 1
    elif command[0] == 'pop':       # stack 의 맨 위 수를 제거하고 반환
        if stack:
            print(stack.pop())
            top -= 1
        else:
            print(-1)
    elif command[0] == 'size':      # stack 의 크기를 확인
        print(len(stack))
    elif command[0] == 'empty':     # stack 이 비어 있는지 여부를 출력
        if stack:
            print(0)
        else: print(1)
    elif command[0] == 'top':       # stack 의 top 값을 출력
        if stack:
            print(stack[top])
        else:
            print(-1)


import sys      # 시간초과 문제를 해결하기 위해 sys.stdin.readline()을 이용

N = int(input())

stack = []
top = -1

for i in range(N):
    com = list(sys.stdin.readline().split())     # push 명령어가 있으므로, 리스트로 입력 받는다.
    stack_operation(com)