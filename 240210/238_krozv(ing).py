# 11. 자신을 제외한 배열의 곱
"""
조건:
나눗셈 X
O(n)으로 풀이
"""
# dictionary로 풀어볼까?
"""
1st
lambda, filter, reduce 이용 -> 18 testcase 시간초과

from functools import reduce
class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        output = [0] * len(nums)
        for idx, num in enumerate(nums):
            excepted_num = list(map(lambda x: nums[x], list(filter(lambda x: x is not idx, range(len(nums))))))
            if len(excepted_num) == 1:
                output[idx] = excepted_num[0]
            else:
                output[idx] = reduce(lambda x, y: x * y, excepted_num)
        return output
"""

"""
2nd
slicing, reduce 이용 -> 18 testcase 시간초과

from functools import reduce
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        output = [0] * N
        for idx in range(N):
            excepted_num = nums[:idx] + nums[idx+1:]
            if len(excepted_num) == 1:
                output[idx] = excepted_num[0]
            else:
                output[idx] = reduce(lambda x, y: x * y, excepted_num)
        return output
"""

"""
3rd
pop + insert 이용 -> 또 초과

from functools import reduce
class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        N = len(nums)
        output = [0] * N
        for idx in range(N):
            num = nums.pop(idx)
            if len(nums) == 1:
                output[idx] = nums[0]
            else:
                output[idx] = reduce(lambda x, y: x * y, nums)
            nums.insert(idx, num)
        return output
"""

"""
4th
reduce module 사용이 최선인가? 의문.
아 모르겠다...ing
"""
from functools import reduce
class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        N = len(nums)
        output = [0] * N
        new_nums = []
        for idx in range(N):
            new_nums.append(nums.pop(0))
            if len(nums) == 1:
                output[idx] = nums[0]
            else:
                output[idx] *= reduce(lambda x, y: x * y, nums)
                if len(new_nums) > 1:
                    output[idx] *= reduce(lambda x, y: x * y, new_nums[:-1])
        return output


c = Solution()
input = [1, 2, 3]
print(c.productExceptSelf(input))