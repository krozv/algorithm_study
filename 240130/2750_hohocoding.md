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