# 10828. stack
"""
정수를 저장하는 스택 구현
입력으로 주어지는 명령 처리
push X: 정수 X를 스택에 넣는 연산
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력
    만약 스택에 들어있는 정수가 없는 경우 -1 출력
size: 스택에 들어있는 정수의 개수 출력
empty: 스택이 비어있으면 1, 아니면 0 출력
top: 스택의 가장 위에 있는 정수 출력, 스택에 들어있는 정수가 없는 경우 -1 출력
정수의 범위 1 <= X <= 100,000
"""
import sys
input = sys.stdin.readline


def run_command(command):
    global top
    if 'push' in command:
        _, x = command.split()
        x = int(x)
        stack.append(x)
        top += 1
    elif 'pop' in command:
        if top == -1:
            print(-1)
        else:
            x = stack.pop()
            top -= 1
            print(x)
    elif 'size' in command:
        print(top+1)
    elif 'empty' in command:
        print(int(top == -1))
    elif 'top' in command:
        if top == -1:
            print(-1)
        else:
            print(stack[top])


N = int(input())     # 전체 명령의 수
stack = []
top = -1
for _ in range(N):
    command = input()
    run_command(command)
