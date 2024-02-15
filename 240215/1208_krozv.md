### 1st

```python
# Flatten
for t in range(1, 11):
    dump = int(input())
    num_list = list(map(int, input().split()))
    for _ in range(dump):
        max_idx = num_list.index(max(num_list))
        min_idx = num_list.index(min(num_list))
        num_list[max_idx] -= 1
        num_list[min_idx] += 1
    max_idx = num_list.index(max(num_list))
    min_idx = num_list.index(min(num_list))
    print(f'#{t} {num_list[max_idx]-num_list[min_idx]}')
```

### 2nd

```python
# Flatten
import sys
sys.stdin = open('input.txt', 'r')

for t in range(1, 11):
    dump = int(input())
    num_list = list(map(int, input().split()))
    for _ in range(dump):
        max_idx = num_list.index(max(num_list))
        min_idx = num_list.index(min(num_list))
        num_list[max_idx] -= 1
        num_list[min_idx] += 1
    print(f'#{t} {max(num_list)-min(num_list)}')
```