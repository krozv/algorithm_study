n, k = map(int,input().split())#사람수, 제거인덱스


q = [0] * (n)
rear=front = 0-1
for i in range(1,n+1):
    rear = (rear+1) % n
    q[rear] = i

idx = k-1 #2
num = [] # 제거 숫자 넣기, # k번쨰 제거
while True:
    try:
        t = q.pop(idx) # 인덱스로 뺌.
        num.append(t)
        idx = (idx + k-1) % len(q) # 제로디비전에러 == len(q) 가 0
    except:
        break

print('<', end = '')
print(*num, sep=", ", end= '')
print('>')

# 호준
N , k = 7, 3
q = [range(1,N+1)]
idx= 0
whlie q:
    idx = (idx+1)% k # 원형큐의 인덱스, k씩 건너뛰기
    num = q. popleft()
    if idx == 0: # 1dx 가 k번쨰인지
        print(num)
    else:
        q.append(num)


