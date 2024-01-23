alpha, num = input().split()
num = int(num)

num_list = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

alpha = alpha[::-1]

result = 0

for i in range(len(alpha)):
    sum = num_list.index(alpha[i]) * (num ** i)
    result = result + sum
    
    
print(result)