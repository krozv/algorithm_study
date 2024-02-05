# 42. 빗물 트래핑

### 풀려고 한 방법
```python 
for i in range(최대높이):
    for j in range(최대길이):
        ...
```
이중 반복문을 이용해서 모든 구역을 돌아보며 빗물을 채워야하는 곳인지 확인 후 결과값을 1씩 증가시키는 방법을 생각했었음

하지만, 아무리 생각해도 이건 아닌 것 같아서 다른 방법을 찾다가 못찾아 답지를 봄

### 투 포인터 이동 방법
100ms
```python
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        volume = 0
        left, right = 0, len(height) - 1
        #left_max와 right_max는 포인터가 각각 왼쪽과 오른쪽을 지나오면서 찾은 최대 높이
        left_max, right_max = height[left], height[right]
        while left < right:
            left_max = max(height[left], left_max)
            right_max = max(height[right], right_max)
            #왼쪽의 최대높이가 더 작거나 같은경우
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            #오른쪽 최대 높이가 더 작은 경우
            else:
                volume += right_max - height[right]
                right -= 1
        return volume
```
