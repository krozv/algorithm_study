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
누적합을 사용해볼까? -> 통과 but 362 ms나 걸림 ㅠ
"""
class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        N = len(nums)
        cnt = [0] * 61
        output = [1] * N
        for num in nums:
            cnt[num + 30] += 1
        for i in range(N):
            for idx, num in enumerate(cnt):
                if num > 0:
                    # print(idx,  num)
                    if idx-30 == nums[i]:
                        output[i] *= (idx-30) ** (num-1)
                    else:
                        output[i] *= (idx-30) ** num
        return output


c = Solution()
input = [1, 2]
print(c.productExceptSelf(input))