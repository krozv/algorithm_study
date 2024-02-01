# 1427 소트인사이드

## bubble sort

시간 44ms

```python
N = input()
digit = 0
for char in N:
    digit += 1
num_list = list(map(int, N))
for i in range(digit-1):
    for j in range(i, digit):
        if num_list[i] < num_list[j]:
            num_list[i], num_list[j] = num_list[j], num_list[i]
print(*num_list, sep='')
```