# 2750. 수 정렬하기

### sort()사용한 쉬운 방법
44ms
```python
import sys

def sorting(N_list):
    N_list.sort()
    for num in N_list:
        print(num)

N_list = []
for _ in range(int(sys.stdin.readline())):
    N_list.append(int(sys.stdin.readline()))

num_list_only1 = list(set(N_list))
sorting(num_list_only1)
```

### 버블정렬 사용
80ms
```python
import sys
def bubble_sort(N_list):
    list_count = 0
    for _ in N_list:
        list_count += 1
    for i in range(list_count-1):
        for j in range(list_count-i-1):
            if N_list[j] > N_list[j+1]:
                N_list[j], N_list[j+1] = N_list[j+1], N_list[j]
    return N_list

N_list = []
for _ in range(int(sys.stdin.readline())):
    N_list.append(int(sys.stdin.readline()))

num_list_only1 = list(set(N_list))
sorted_list = bubble_sort(num_list_only1)
[print(i) for i in sorted_list]
```

### counting 정렬 사용
44ms
```python
import sys
N = int(sys.stdin.readline())
N_list = []
counts= [0] * 2001 #-1000~1000
for _ in range(N):
    N_list.append(int(sys.stdin.readline()))
for num in N_list:
    counts[num+1000] += 1 #num이 -1000일때 counts의 0번째 이므로
    
for i in range(1,2001):
    counts[i] = counts[i] + counts[i-1]

result_list =[0]*N
for i in range(N-1,-1,-1):
    counts[N_list[i]+1000] -= 1
    result_list[counts[N_list[i]+1000]] = N_list[i]

[print(i) for i in result_list]

```