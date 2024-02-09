# 12789. 도키도키 간식드리미
"""
N: 앞에 서 있는 학생들의 수
num_list: 앞에 서 있는 모든 학생들의 번호표
"""
N = int(input())
num_list = list(map(int, input().split()))
stack = []
leave = 1   # 번호표 순서
top = -1

for num in num_list:
    # stack안에 대기자 존재
    if len(stack):
        # stack 내에서 나갈 번호표 순서가 일치하면 pop
        while stack[top] == leave:
            leave += 1
            stack.pop()
            top -= 1
            # stack 안에 대기자 없으면 while문 종료
            if not len(stack):
                break
    # 번호표가 일치
    if leave == num:
        leave += 1
    # 번호표 불일치의 경우
    else:
        # stack 안에 들어갈 번호표 = 대기
        stack.append(num)
        top += 1
# 번호표 순서가 도달하지 않아서 stack 안에서 대기 중인 사람들 꺼냄
if len(stack):
    for _ in range(len(stack)):
        # 번호표 순서가 일치할 경우 pop
        if stack[top] == leave:
            leave += 1
            stack.pop()
            top -= 1
    else:
        # stack 안에 대기자 존재할 경우
        if len(stack):
            print("Sad")
        # stack 안에 대기자 없음
        else:
            print("Nice")
# stack 안에 대기자 없음
else:
    print("Nice")
"""
반례 모음
10
5 4 3 2 1 6 7 8 9 10
nice
10
5 4 3 2 1 10 9 8 7 6
nice
"""
