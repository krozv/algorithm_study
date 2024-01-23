def 등차수열합(x):
    return x*(x+1) // 2

x = int(input())

numb = 1
while x> 등차수열합(numb):
    numb += 1

i = x - 등차수열합(numb - 1) # 1
j = (numb+1) - i

if numb % 2 != 0:
    i,j = j,i


print(f'{i}/{j}')