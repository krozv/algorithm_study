N, K = map(int,input().split())
i = 1
count = 0
while True:
    
    if i > N:
        i = 0 #K번째 값이 존재하지 않을 경우 i = 0
        break

    if N % i ==0:
        count += 1
    
    if count == K:
        break
    i += 1
print(i)