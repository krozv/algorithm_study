### try1

```py
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) ==  nums.count(0):
            result = [[0,0,0]]
        else:
            result = [] # 총 합이 0인 3개의 값 저장 리스트
            N = len(nums)
            for i in range(N-2):
                request = []
                sum1 = sum(nums[i:i+2])
                other = -sum1

                for item in nums[:i]+nums[i+2:]:
                    if item == other:
                        request.extend(nums[i:i+2])
                        request.append(item)
                        request.sort()
                        result.append(request)
                        break
                if request in result[:-1]:
                    result.pop()
        return result



sol = Solution()
nums = [-1, 0, 1, 2, -1, -4]
# nums =[0,0,0,0]
r = sol.threeSum(nums)
print(r)

"""
Wrong Answer

input 
nums = [0,0,0,0]

output 
[[0,0,0],[0,0,0]]

expected
[[0,0,0]]


"""
```

> 분석
> 1. [0,0,0,0] 일 때의 경우를 생각하지 못함
> 2. 정렬을 하고 나서의 과정을 책으로 공부함
> 3. 중복을 처리하는 방법도 책으로 공부함   


### try2

```py
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # 리스트 정렬
        result = []
        N = len(nums)
        if N == nums.count(0):
            result = [[0, 0, 0]]
        else:
            for i in range(N-2):
                if i >0 and nums[i] == nums[i-1]:
                    continue # 중복된 값 피하기
                left, right = i+1,N-1

                while left < right:
                    sub_sum = nums[i]+nums[left]+nums[right]
                    if sub_sum == 0:
                        result.append([nums[i], nums[left],nums[right]])

                        # 각 진행되는 방향에서 중복된 값 피하기 -> 이동
                        left_num, right_num = nums[left], nums[right]
                        while left < right and nums[left] == left_num :
                            left +=1
                        while left < right and nums[right] == right_num:
                            right -=1

                    elif  sub_sum < 0: # 0보다 작을 경우
                        left +=1 # 작은 값을 오른쪽으로 이동
                    else : # 0보다 클 경우
                        right -=1 # 큰 값은 왼쪽으로

        return result

```

