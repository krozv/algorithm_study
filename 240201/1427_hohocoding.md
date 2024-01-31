# 1427. 소트인사이드

### 코드
44ms
```python
N= str(int(input()))

counts =[0]*10 #0~9 카운팅을 위한 리스트
for num in N:
    counts[int(num)] += 1
for i in range(9,-1,-1):# 큰 수를 앞으로 정렬
    print(str(i)*counts[i], end='')

```