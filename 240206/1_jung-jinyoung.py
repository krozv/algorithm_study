from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        N = len(nums) # 문자열 길이
        for i in range(N-1):
            for j in range(i+1,N):
                if nums[i] + nums[j] == target:
                    return [i,j]

