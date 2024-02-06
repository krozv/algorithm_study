
### 행렬의 곱

A 행렬 X B 행렬 = C 행렬  
A 의 행 인덱스 = a  
B 의 열 인덱스 = b  
A[a] * B[.][b] = C[a,b] 
>A 의 행의 인덱스와 B의 열의 인덱스가 C의 좌표가 된다. 
```py
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        N = len(nums) # 문자열 길이
        for i in range(N-1):
            for j in range(i+1,N):
                if nums[i] + nums[j] == target:
                    return [i,j]

```