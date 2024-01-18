T = int(input())


for t in range(T):
  A = list(map(int,input().split()))
  B = list(map(int,input().split()))

  N=len(A)
  M=len(B)
  sum_list=[]
  if N < M:
    for i in range(M-N+1):
        mul_sum = 0
        for j in range(N):
            mul_sum += A[j] * B[i+j]
        sum_list.append(mul_sum)
      
    print(f'# {t+1} {max(sum_list)}')
  else :
    for i in range(N-M+1):
        mul_sum = 0
        for j in range(M):
            mul_sum += A[i+j] * B[j]
        sum_list.append(mul_sum)
    print(f'# {t+1} {max(sum_list)}') 