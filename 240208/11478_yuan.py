

#3520ms

a = input()
N = len(a)

cnt = 0
for k in range(1,N+1):
    stack = []
    for i in range(N):
        if 0 <= i + k <=N:
            if stack:
                if stack[-1] != a[i:i+k]:
                    if a[i:i + k] not in stack: # stack에 아예 없을때만 append
                        stack.append(a[i:i+k])
                else:
                    pass # 직전거랑 같으면 안넣기
            else:
                stack.append(a[i:i+k])
    cnt+= len(stack)
print(cnt)

