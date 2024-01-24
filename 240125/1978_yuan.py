N = int(input())
N_list = list(map(int, input().split()))


number = []

for j in N_list:
    for i in range (2,1000):
        if j / i == 1:
            number.append(j)
            break

print(number)
print(len(number))



