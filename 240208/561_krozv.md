# 561. Array Partition I

n개의 페어를 이용한 min(a, b)의 합으로 만들 수 있는 가장 큰 수를 출력하라

### Solution

```python
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        output = 0
        for i in range(len(nums)//2):
            output += min(nums[i*2], nums[i*2+1])
        return output
```

```python
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        output = 0
        for i in range(len(nums)//2):
            output += nums[i*2]
        return output
```

### Answer

```python
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum=0
        nums.sort()
        for i in range(0,len(nums),2):
            sum=sum+nums[i]
        return sum
        
```