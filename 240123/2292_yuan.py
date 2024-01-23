
def digit_sum(n):
    return 3*n*(n+1) +1 
# digit = n +1 

x = int(input())

digit = 0
while x > digit_sum(digit):
    digit += 1 
    
print(digit+1)