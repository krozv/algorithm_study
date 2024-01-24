import sys
N, M = [int(i) for i in input().split()]
S = set() # S 집합 

for i in range(N):
    S.add(sys.stdin.readline().strip().lower()) # N줄만큼 입력된 문자 집합에 추가

count = 0
for j in range(M):
    M = sys.stdin.readline().strip().lower()
    if M in S :
        count +=1 # 문자 포함시
    
print(count)
