from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        # 왼쪽에서부터 부분곱 계산
        left_mul = 1
        for i in range(1,n):
            left_mul *= nums[i-1]
            result[i] *= left_mul

        # 오른쪽에서부터 부분곱 계산
        right_mul = 1
        for j in range(n-2,-1,-1):
            right_mul *= nums[j+1]
            result[j] *= right_mul

        return result

sol = Solution()
nums = [1,2,3,4]
result = sol.productExceptSelf(nums)
print(result)
