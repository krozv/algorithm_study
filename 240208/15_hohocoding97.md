# 15. 3Sum

### 첫 시도
308/312 시간초과
```python
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        new_list = [] 
        for i in range(N-2):
            for j in range(i+1, N-1):
                for k in range(j+1, N):
                    if nums[i]+nums[j]+nums[k] == 0:
                        if not sorted([nums[i],nums[j],nums[k]]) in new_list:
                            new_list.append(sorted([nums[i],nums[j],nums[k]]))
        return new_list
```