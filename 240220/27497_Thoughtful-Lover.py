'''
알파벳 블록을 일렬로 조립하여 문자열을 만드는 게임

1 c : 문자열 맨 뒤에 c가 적힌 블록 추가
2 c : 문자열 맨 앞에 c가 적힌 블록 추가
3 : 문자열을 구성하는 블록 중 가장 나중에 추가된 블록 제거
'''


''' # 1차_시간초과
from collections import deque

# 명령에 따라 문자열을 담을 array 를 선언
array = deque()
# 마지막으로 블록을 추가한 위치를 담을 last 를 선언
last = deque()  # 이건 스택이라고 할 수 있음

N = int(input())
# 입력받은 N만큼 명령어를 입력 받음
for i in range(N):
    com = list(input().split())

    # 명령어의 앞이 1이면 알파벳을 뒤로 입력받고, 0 을 last 에 배정
    if com[0] == '1':
        array.append(com[1])
        last.append(0)

    # 명령어의 앞이 2이면 알파벳을 앞으로 입력받고, 1 을 last 에 배정
    elif com[0] == '2':
        array.appendleft(com[1])
        last.append(1)

    else:
        # array 에 알파벳이 있는 경우에만 pop
        # last 에 최근에 담긴 것이 뒤쪽 것이면 뒤쪽 것을 pop, 앞쪽이면 앞쪽 것을 pop
        if array:
            if last.pop() == 0:
                array.pop()
            else:
                array.popleft()

# array 에 남은 알파벳이 있으면 나란히 출력
if array:
    for j in array:
        print(j, end='')
    print()
# 없는 경우 0을 출력
else: print(0)'''

# 2차_성공
## sys로 바꿈
## 입력값이 많은 것 같아 pypy로 바꿈
import sys
from collections import deque

# 명령에 따라 문자열을 담을 array 를 선언
array = deque()
# 마지막으로 블록을 추가한 위치를 담을 last 를 선언
last = deque()  # 이건 스택이라고 할 수 있음

N = int(sys.stdin.readline())
# 입력받은 N만큼 명령어를 입력 받음
for i in range(N):
    com = list(sys.stdin.readline().split())

    # 명령어의 앞이 1이면 알파벳을 뒤로 입력받고, 0 을 last 에 배정
    if com[0] == '1':
        array.append(com[1])
        last.append(0)

    # 명령어의 앞이 2이면 알파벳을 앞으로 입력받고, 1 을 last 에 배정
    elif com[0] == '2':
        array.appendleft(com[1])
        last.append(1)

    else:
        # array 에 알파벳이 있는 경우에만 pop
        # last 에 최근에 담긴 것이 뒤쪽 것이면 뒤쪽 것을 pop, 앞쪽이면 앞쪽 것을 pop
        if array:
            if last.pop() == 0:
                array.pop()
            else:
                array.popleft()

# array 에 남은 알파벳이 있으면 나란히 출력
if array:
    for j in array:
        print(j, end='')
    print()
# 없는 경우 0을 출력
else: print(0)

