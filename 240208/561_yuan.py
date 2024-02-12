class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        num_sort = sorted(nums, reverse = True)
        print(num_sort)

        sum = 0
        for x in range(len(num_sort)//2):
            a, b = num_sort[x*2], num_sort[x*2+1]
            sum += min(a,b)

        return sum



# 시간 짧고 최고 간결한 풀이
# 정렬 한 뒤에 짝수번째 == min 값 만 계산
    class Solution:
        def arrayPairSum(self, nums: List[int]) -> int:
            nums = sorted(nums)
            return sum(nums[::2])