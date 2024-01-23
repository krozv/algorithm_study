
N = int(input())

def func(k):
    return int(k * (k + 1) / 2) # k번째 줄 가장 끝 수의 순번 함수 

n = 1
while N > func(n):
    n += 1

if n % 2 == 1:
    num_1 = func(n) - N + 1
    num_2 = n - num_1 + 1 # num_1 + num_2 = n+1
else:
    num_2 = func(n) - N + 1
    num_1 = n - num_2 + 1

print(f'{num_1}/{num_2}')


