# 2750. 수 정렬하기

bubble sort 사용

```python
N = int(input())
num_list = []
for _ in range(N):
    num_list.append(int(input()))
for i in range(N-1):
    for j in range(i+1, N):
        if num_list[i] > num_list[j]:
            num_list[i], num_list[j] = num_list[j], num_list[i]
print(*num_list, sep='\n')
```