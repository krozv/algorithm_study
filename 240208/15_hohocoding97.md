# 15. 3Sum

### 첫 시도
308/312 시간초과
```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        new_list = [] 
        for i in range(N-2):
            for j in range(i+1, N-1):
                for k in range(j+1, N):
                    if nums[i]+nums[j]+nums[k] == 0:
                        if not sorted([nums[i],nums[j],nums[k]]) in new_list:
                            new_list.append(sorted([nums[i],nums[j],nums[k]]))
        return new_list
```
### 슬쩍 방법보고 재시도
311/312 시간초과
```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        nums.sort()
        new_list = [] 
        i = 0
        while i<N-2:
            left, right = i+1, N-1 #나머지 두 포인터 위치
            while left < right:
                if nums[i]+nums[left]+nums[right] == 0:
                    new_list.append([nums[i],nums[left],nums[right]])
                    #같은 i내에서도 추가적인 해답이 있을 수 있으므로 break안하고 left를 증가시켜서 추가 케이스 찾음
                    while left+1<N and nums[left] == nums[left+1]: 
                        left += 1
                    left += 1
                    right = N-1
                    continue
                if nums[i]+nums[left]+nums[right] >0:
                    while right-1 > 0 and nums[right] == nums[right-1]:
                        right -= 1
                    right -= 1
                else: 
                    while left+1 < N and nums[left] == nums[left+1]: #뒤에 조건만 달 경우 IndexError발생
                        left += 1
                    left += 1
            while i+1 < N and nums[i] == nums[i+1]: #i+1번째 값과 다를때까지 1씩 증가
                i += 1
            i += 1  #1더 증가시켜줌.
        return new_list

```

### 위에 코드 조금 덜 계산하도록 변경
311/312 그래도 시간초과 
```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        nums.sort()
        new_list = [] 
        i = 0
        while i<N-2:
            left, right = i+1, N-1 #나머지 두 포인터 위치
            while left < right:
                I,L,R = nums[i], nums[left], nums[right]
                if I+L+R == 0:
                    new_list.append([I,L,R])
                    while left+1<N and L == nums[left+1]: 
                        left += 1
                    left += 1
                    right = N-1
                    continue
                elif I+L+R >0:
                    while right > 0 and R == nums[right-1]:
                        right -= 1
                    right -= 1
                else: 
                    while left+1 < N and L == nums[left+1]: #뒤에 조건만 달 경우 IndexError발생
                        left += 1
                    left += 1
            while i+1 < N and I == nums[i+1]: #i+1번째 값과 다를때까지 1씩 증가
                i += 1
            i += 1  #1더 증가시켜줌.
        return new_list
```

### 외국 똑똑이분 코드

```python
class Solution:    
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = set()
        #1. Split nums into three lists: negative numbers, positive numbers, and zeros
        n, p, z = [], [], []
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0: 
                n.append(num)
            else:
                z.append(num)

        #2. Create a separate set for negatives and positives for O(1) look-up times
        N, P = set(n), set(p)

        #3. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
        #   i.e. (-3, 0, 3) = 0
        if z:
            for num in P:
                if -1*num in N:
                    res.add((-1*num, 0, num))

        #3. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0
        if len(z) >= 3:
            res.add((0,0,0))

        #4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
        #   exists in the positive number set
        for i in range(len(n)):
            for j in range(i+1,len(n)):
                target = -1*(n[i]+n[j])
                if target in P:
                    res.add(tuple(sorted([n[i],n[j],target])))

        #5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
        #   exists in the negative number set
        for i in range(len(p)):
            for j in range(i+1,len(p)):
                target = -1*(p[i]+p[j])
                if target in N:
                    res.add(tuple(sorted([p[i],p[j],target])))

        return res
```