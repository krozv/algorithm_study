# from collections import deque
#
# N = int(input())
# lst = [i for i in range(1,N+1)]
# lst = deque(lst)
#
# while len(lst)> 1:
#     lst.popleft()
#     t = lst.popleft()
#     lst.append(t)
#
# print(*lst)

# 틀린 코드
# 길이 건드리는 반복이 돌아가는 과정에서 문제 생길 수 있음?
from collections import deque

N = int(input())
lst = [i for i in range(1,N+1)]
lst = deque(lst)

while True:
    lst.popleft()
    if len(lst) == 1: # n =1인경우에 0되면서 문제. while True 가아닌 while len(q) 로 해줘야햠.
        break
    t = lst.popleft()
    lst.append(t)

print(*lst)