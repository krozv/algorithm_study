# 1. Two Sum

### 코드
1700ms ...
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
```
버블정렬 쓰는 것처럼 했음
시간복잡도 O(n^2)


### LeetCode Solution1 (One-pass Hash Table)
51ms
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i

        return []  # No solution found
```
딕셔너리 만들어서 값을 key로 인덱스를 value로 넣었음
그리고 원하는 값을 딕셔너리로 빠르게 찾음