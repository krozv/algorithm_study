# import sys
#
# sys.stdin = open('input.txt', 'r')


from copy import deepcopy

N = input()
data = []
number = int(deepcopy(N))

while number>0:
    k = number % 10
    data.append(k)
    number//= 10

print(data)

for i in range(len(N)):
    for j in range(len(N)-1):
        if data[j] < data[j+1]:
            data[j], data[j+1] = data[j+1], data[j]


for i in data:
    print(i, end='')