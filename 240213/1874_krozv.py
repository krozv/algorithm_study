# 1874. 스택 수열
"""
1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음 -> 하나의 수열 만듦
스택에 push하는 순서는 반드시 오름차순
임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는 지 확인~~
있으면 어떤 순서로 push 및 pop해야 하는 지~~
"""
"""
문제 이해
while seq != new_seq
방향성
num_list에서 num을 꺼낸 후 sequence와 일치하면 new_seq에 append할 계획임

1. num_list에서 num을 하나 꺼낸다
2. stack이 비어 있는 지 확인
    2-1. stack이 비어있을 경우 (top == -1)
        num을 stack에 append한다.
    2-2. stack이 비어있지 않을 경우 (top != -1)
        2-2-1. stack[top] == seq[:
                elem = pop
                elem을 new_seq에 append
        2-2-2. stack[top] != elem:
                2-2-2-1. elem in stack:
                            pop
                2-2-2-2. elem in num_list:
                            push
                2-2-2-3. elem not in stack and num_list:
                            print(No)
    return output
시간초과 나옴 -> 어떻게 줄일까?                                  
"""
n = int(input())
seq = [int(input()) for _ in range(n)]   # 수열 sequence
num_list = list(range(n, 0, -1))

stack = []
output = []
new_seq = []
while seq:
    if not stack:
        if not num_list:
            output = None
            break
        num = num_list.pop()
        stack.append(num)
        output.append('+')
    # stack에 요소 존재
    else:
        if seq[0] in stack:
            while stack[-1] != seq[0]:
                elem = stack.pop()
                output.append('-')
            stack.pop()
            output.append('-')
            seq.pop(0)
        elif seq[0] in num_list:
            while stack[-1] != seq[0]:
                num = num_list.pop()
                stack.append(num)
                output.append('+')
            stack.pop()
            output.append('-')
            seq.pop(0)
        else:
            output = None
            break
if output:
    for elem in output:
        print(elem)
else:
    print('NO')