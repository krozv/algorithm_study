N = int(input())
N_list = list(input().split())

M = int(input())
M_list = list(input().split())

set_N = set(N_list)
set_M = set(M_list)

set_x = set_M - set_N 

for i in range(len(M_list)):
    if M_list[i] in set_x:
        M_list[i] = 0
    else:
        M_list[i] = 1

print(*M_list)
