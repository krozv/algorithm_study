# 238

### 첫 시도
18/22 시간초과

```python
import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        result = []
        for i in range(N):
            new_nums = nums[:]  #얕은 복사
            new_nums.pop(i)     #i번째 요소 없에기
            result.append(math.prod(new_nums))
        return result
```


### 리트코드의 soltion..
각 자리에 출력된 값은 그 자리의 `왼쪽에 있는 수들의 곱`과 `오른쪽에 있는 수들의 곱`을 곱한 것과 같음


```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        result = [1] *N
        left, right = 1, 1#왼쪽과 오른쪽을 따라 곱해줄 녀석
        #왼쪽 곱해주기
        for i in range(N):
            pre_left = left
            left = left*nums[i]
            result[i] = result[i]*pre_left
        #오른쪽 곱해주기
        for i in range(N-1,-1,-1):#오른쪽부터 오면서 곱해야 하니까
            pre_right = right
            right = right*nums[i]
            result[i] = result[i]*pre_right
        return result
```