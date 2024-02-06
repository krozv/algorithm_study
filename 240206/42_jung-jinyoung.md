### try 1 (길어도 읽어줘잉..)
> 목표 : 요철 모양을 찾아서 면적을 계산한 후, 범위 안에 있는 높이들의 합을 뺀값 = 더해 줄 물의 양

```py
class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0  # 누적된 물의 양을 저장할 변수를 초기화합니다.

        # 현재 위치(i)보다 높은 위치를 찾는 조건
        for i in range(1, len(height)):
            left = 0
            right = 0
            left_idx = 0
            right_idx = 0

            # 왼쪽 높은 값 찾기
            max_height = height[i]
            for j in range(i-1,-1,-1):
                if height[j] > max_height:
                    max_height = height[j]
                    left = max_height
                    left_idx = j
                elif height[j]<max_height:
                    break
            # 오른쪽 높은 값 찾기
            max_height = height[i]
            for k in range(i+1,len(height)):
                if height[k] > max_height:
                    max_height = height[k]
                    right = max_height
                    right_idx = k
                elif height[k] < max_height:
                    break


            # 누적된 물의 양을 계산하여 total_water에 추가
            min_height = min(left, right)
            if min_height > height[i]:
                total_water += (right_idx - left_idx-1) * min_height - sum(height[left_idx+1:right_idx])

        return total_water
```
case 1의 경우만 정답
`case 1 : height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]`  

case 2 오답
`case2 : height =  [4,2,0,3,2,5]`
`output = 5`
`expected = 9`  

> 분석
> - 양쪽 끝이 높을 경우 생각하지 않은 코드  
> - 최고 높이를 계산할 때 자기 자신을 포함하지 않았어서 마지막 if문을 추가 ,,


### try2

선생님 찬스 .. 
위치를 계속 이동한다.   
-> 높은 위치가 있을경우 멈춘다. (다음 위치 : 높은 위치 이후 )
-> 물의 양을 계속 더한다.

> 이동할 경우를 구현하는게 어려웠다.
> try 1과 함께 생각해서 현재의 위치를 봤을 때의 물의 양을 구할 수 있음을 알았다.
> 따라서 현재의 위치에 따른 최대 높이들을 모두 저장하고, 비교해서 물의 양을 더하는 함수를 작성했다. 

```py
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [0] * n  # 각 위치에서 왼쪽으로의 최대 높이를 저장
        right_max = [0] * n  # 각 위치에서 오른쪽으로의 최대 높이를 저장

        left_max[0] = height[0]
        for i in range(1, n):  # 각 위치에서 왼쪽으로의 최대 높이 (자신 (i) 포함 X)
            left_max[i] = max(left_max[i - 1], height[i])

        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):  # 각 위치에서 오른쪽으로의 최대 높이 (자신 (i) 포함 X)
            right_max[i] = max(right_max[i + 1], height[i])

        total_water = 0
        for i in range(n):
            water_level = min(left_max[i], right_max[i])
            if water_level > height[i]:
                total_water += water_level - height[i]
            # 자신이 가장 클 경우 left/right max가 없을 경우는 넘어감
        return total_water
```