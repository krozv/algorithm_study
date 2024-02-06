# 42. Trapping Rain Water

### Solution

바닥부터 빈 공간을 채워나간다.

채워진 빈 공간의 개수를 센다.

시간 5807ms로 아주 안좋음 ^^

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        start = 0
        end = len(height)-1
        water = 0
        line = 0
        while start < end:
            # start 지점 선정
            for i in range(start, end+1):
                # len(height) == 1인 경우
                if i == end:
                    start = end
                elif height[i] <= line:
                    continue
                else:
                    start = i
                    break
            # end 지점 선정
            for i in range(end, start-1, -1):
                if height[i] <= line:
                    continue
                else:
                    end = i
                    break
            # 채울 층 수(line)를 찾음
            line = min(height[start], height[end])
            # 물 채움
            for i in range(start, end):
                if height[i] < line:
                    water += line - height[i]
                    height[i] = line
        return water
```