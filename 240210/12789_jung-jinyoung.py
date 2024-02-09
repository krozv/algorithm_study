N = int(input())  # 앞에 서 있는 학생들의 수
stack = []  # 추가 대기 라인
snack = []  # 간식 받은 순번
waiting = list(map(int, input().split()))  # 현재 대기 라인
i = 1
j = 0

"""
logic 
: 추가 라인에 append -> 확인 -> 순번에 맞으면 pop, 아니면 j+=1
"""

while stack or j < N:
    # 추가 대기 라인에 순번이 있을 경우
    if stack and stack[-1] == i:
        snack.append(stack.pop())
        i += 1
    # 추가 라인에 없을 경우 추가
    elif j < N:
        stack.append(waiting[j])
        j += 1
    # 현재 대기 라인에 사람이 없을 경우 확인
    # stack 마지막 순번이 현재 필요한 순번과 다를 경우
    elif stack[-1] != i:
        break


if len(snack) == N:
    # 모두 순번 대로 간식을 받았을 경우
    print('Nice')
else:
    print('Sad')
