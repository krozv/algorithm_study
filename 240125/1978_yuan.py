
N = int(input())
N_list = list(map(int, input().split()))

for i in range(2, 1000):
    for j in N_list:
        if j == 1:
            N_list.remove(j)

        if j != i and j%i ==0:
            N_list.remove(j)


print(len(N_list))
