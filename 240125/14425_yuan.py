N, M = map(int,input().split())

N_set = list(input().splitlines() for _ in range(N))
M_list = list(input().splitlines() for _ in range(M))

count = 0
for i in M_list:
    if i in N_set:
        count +=1

print(count)