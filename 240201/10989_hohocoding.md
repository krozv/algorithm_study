# 10989. 수 정렬하기

### 성공 코드
8968ms, 31120KB
```python
import sys
N = int(input()) #주어질 숫자 개수
Num_count =[0]*10001 #0~10,000까지 카운팅할 리스트 생성
for _ in range(N):
    #입력받은 값을 바로 Num_count에서 카운팅
    Num_count[int(sys.stdin.readline())] += 1

for i in range(len(Num_count)):
    if Num_count[i] != 0:
        for _ in range(Num_count[i]):
            print(i)
```
입력과 동시에 Num_count로 카운팅해서 메모리 줄임

---
### 실패 코드 1 (bubble sort)


메모리 초과
```python
import sys                                                  
                                                            
N = int(sys.stdin.readline())                               
N_list = [int(sys.stdin.readline()) for _ in range(N)]      
                                                            
for i in range(N-1):                                        
    for j in range(N-i-1):                                  
        if N_list[j] > N_list[j+1]:                         
            N_list[j], N_list[j+1] = N_list[j+1], N_list[j] 
print(*N_list, sep='\n')

```



### 실패 코드 2 (counting sort)
메모리 초과
```python
N = int(input())
N_list = [int(input()) for _ in range(N)]

counts = [0]*10000
for num in N_list:
    counts[num-1] += 1
for num in range(1,N):
    counts[num] += counts[num-1]
result_list = [0]*N
for num in range(N-1,-1,-1):
    counts[N_list[num]-1] -= 1
    result_list[counts[N_list[num]-1]] = N_list[num]
print(*result_list,sep='\n')
```
성공 코드와는 다르게 (1)리스트를 받고
(2)카운팅 하고, (3)누적하고 ... 등등의 과정이 많이 진행되어 메모리 초과
