#2072번 홀수만 더하기
#정진영

t = int(input())

for i in range(1, t+1):
    arr = list(map(int,input().split(' ')))

    odd_sum = 0
    for num in arr:
        if num % 2 !=0:
            odd_sum += num
            
    print(f'#{i} {odd_sum}')