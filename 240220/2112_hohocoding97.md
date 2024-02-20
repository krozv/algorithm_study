# 2112.보호필름
### DFS로 풀이


시간초과... 45/50
```python
from copy import deepcopy

def test(arr2):
    for j in range(W):
        cnt = 1
        pre_data = arr2[0][j]
        for i in range(1,D):
            if arr2[i][j] == pre_data:
                cnt += 1
            else:
                cnt = 1
                if pre_data:
                    pre_data = 0
                else:
                    pre_data = 1
            if cnt == K:
                break
        else:
            return False
    return True

def dfs(col, inject_cnt, arr):#col은 행, inject_cnt:투입횟수,arr:셀 상태
    global min_injection
    if inject_cnt == min_injection: 
        return
    elif test(arr):
        min_injection = min(min_injection, inject_cnt)
        return
    elif col == D:
        return
    new_arr = deepcopy(arr)
    dfs(col+1, inject_cnt, new_arr)
    new_arr[col] = [0]*W
    dfs(col+1, inject_cnt+1, new_arr)
    new_arr[col] = [1]*W
    dfs(col+1, inject_cnt+1, new_arr)

T = int(input())
for tc in range(1, T+1):
    D,W,K = map(int, input().split())
    data = [list(map(int,input().split())) for _ in range(D)]
    min_injection = D
    dfs(0,0,data)
    print(f'#{tc} {min_injection}')
```