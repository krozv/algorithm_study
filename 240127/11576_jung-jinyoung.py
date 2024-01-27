A, B = [int(i) for i in input().split()] # A 진법을 B 진법으로
m = int(input()) #자리 개수

A_nums = list(map(int,input().split()))
reverses_A = A_nums[::-1] # 계수 정렬
num10=0

for pos in range(m):
    num10 += reverses_A[pos] * (A ** pos) # A 진법을 10진법으로
    
result=[]

while num10 > 0:
    result.append(num10 % B)
    num10 //=B  #B로 나누었을 때의 나머지를 차례로 구함

print(*result[::-1])  # 역순으로 정렬 후 출력 