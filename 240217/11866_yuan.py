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

