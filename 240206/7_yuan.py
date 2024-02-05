
#dic 에 넣어 풀기
class Solution:
    def twoSum(self, nums, target):

        dic = {}
        for idx, num in enumerate(nums):
            dic[idx] = num

        value_list = [value for value in dic.values()]
        N = len(nums)

        key_list = []
        for i in range(N):
            for j in range(i+1,N):
                if value_list[i] + value_list[j] == int(target):
                    return [i,j]

#dic 에 안넣어도 됨
# 하나는 앞에서부터 , 하나는 뒤에서부터 찾기
# 단 중복값이 안되기때문에 두 인덱스의 range 가 겹치지 않아야함
class Solution:
    def twoSum(self, nums, target):
        N = len(nums)
        for i in range(N):
            for j in range(N-1,i,-1):
                print(i,j)

                if nums[i] + nums[j] == int(target):
                    return [i,j]


# target 에서 빼기
#
# class Solution:
    def twoSum(self, nums, target):

        N = len(nums)
        for i in range(N):
            try:
               j = nums.index(target - nums.pop(i))
               return [i,j+(i+1)] # i를 pop 했으니까 j는 pop해준 i(+1)만큼 다시 더해줘야함. ex. i = 0 이면 한개 사라짐

            except:
                continue
#
#
#
# nums = [3,2,4]
# target = 6
# a = Solution()
# print(a.twoSum(nums,target))