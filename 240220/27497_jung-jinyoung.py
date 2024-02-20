from collections import deque
N = int(input()) # 버튼 누른 횟수
s = deque()
current = deque() # 현재 상황 저장 리스트
for _ in range(N):
    data = input().split()
    if data[0] == '2': # 2이면
        s.appendleft(data[1]) # 앞에 추가
        current.append(0) # 현재 상황 저장 (앞 == 0)
    elif data[0] == '1': # 1이면
        s.append(data[1]) # 뒤에 추가
        current.append(1) # 현재 상황 저장 (뒤 == 1)
    else:
        if current:
            i = current[-1]
            if i == 0: # 이전에 앞에 추가했으면
                s.popleft()
            else: # 뒤에 추가했으면
                s.pop()
            current.pop() # 업데이트

if not s: # 비어있으면
    print(0)
else:
    print(''.join(s))
