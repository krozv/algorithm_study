# 1. Two Sum

### 1st

수업시간에 배운 비트연산자 이용해봄

배열 길이 증가하면 Time Limit 문제 발생 ㅠ

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)
        for i in range(1<<N):
            set = []
            for j in range(N):
                if i & (1<<j):
                    set += [nums[j]]
            if len(set) == 2 and sum(set) == target:
                a = nums.index(set[0])
                nums.reverse()
                b = len(nums) - nums.index(set[1]) - 1
                return [a, b]
```

### 2nd

있는 대로 다 더해봄. 이게 brute force인가..?

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)
        for i in range(N-1):
            for j in range(i+1, N):
                if nums[i] + nums[j] == target:
                    return [i, j]
```