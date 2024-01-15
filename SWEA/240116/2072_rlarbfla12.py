t = int(input())

for test_case in range(1, t+1):
    data = list(map(int, input(). split()))
    sum = 0
    for i in data:
    	if i % 2 == 1:
            sum += i
            
    print(f"#{test_case} {sum}")