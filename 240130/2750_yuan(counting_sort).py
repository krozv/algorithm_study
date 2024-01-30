N = int(input())
N_list = [int(input()) for _ in range(N)]


#음수 처리. 이후 프린트할때 빼줄 것
if min(N_list) < 0:
    a = 0 - min(N_list)
else:
    a = 0
N_list = [char + a for char in N_list]


# 카운팅 소트 
k= max(N_list)

count = [0] * (k+1)
temp = [0] * N 

for i in N_list:
    count[i] += 1


for j in range(1,k+1): # 1부터 시작, count[0]은 원래 카운트대로
    count[j] = count[j-1] + count[j]  


for x in range(N-1,-1, -1): # -1 말고 N-1 로 쓰면 편함 
    count[N_list[x]] -=1  # 미리 빼주면 n_list에 바로 넣을 수 있음 
    temp[count[N_list[x]]] = N_list[x] 


for i in temp:
    print(i-a)