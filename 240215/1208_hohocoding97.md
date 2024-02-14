# 1208. Flatten
### 메서드 봉인해제 코드
177ms 
```python
for tc in range(1,11):
    N = int(input()) #덤프횟수
    data = list(map(int, input().split()))
    for _ in range(N):
        top, bottom = max(data), min(data)
        top_pos, bottom_pos = data.index(top), data.index(bottom)
        data[top_pos] -= 1
        data[bottom_pos] += 1
    print(f'#{tc} {max(data)-min(data)}')
```
