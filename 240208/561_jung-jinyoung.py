class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort() # 정렬
        min_num_list = []
        N = len(nums)
        for i in range(0,N,2): # 2개씩 페어일수록 합의 최댓값이 가능
            request = min(nums[i], nums[i+1])
            min_num_list.append(request)

        return sum(min_num_list)


