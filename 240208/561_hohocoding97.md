# 561. Array Partition

### 내 코드
214ms

정렬해서 짝수번째 index의 값만 더했음
```python
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        for i in range(0, len(nums), 2):
            result += nums[i]
        return result
```