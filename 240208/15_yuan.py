

# 빠른 풀이
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        nums.sort()
        result = []

        # i 중복값 제거
        for i in range(N-1):
            if i >0 and nums[i]==nums[i-1]:
                continue

            # sum함수 안쓰기
            left = i+1
            right = N-1
            while left<right:
                if nums[i] + nums[right] + nums[left] > 0:
                    right = right -1
                elif nums[i] + nums[right] + nums[left] < 0:
                    left = left +1
                else:
                    result.append([nums[i],nums[left],nums[right]])

                    # 중복값에 대해 포인터 한개만 이동시 더 적은 연산함
                    left +=1
                    while left <right and nums[left]==nums[left - 1]:
                        left += 1
        return result



# 답지 참고한 투포인터 풀이
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#
#         N = len(nums)
#         nums.sort()
#         result = []
#
#
#         for i in range(N-2):
#             # 반복 최대한 줄이기위해 겹치는 수 있으면 패스
#             if i> 0 and nums[i] == nums[i-1]:
#                 continue
#
#             # 투포인터 인덱스 설정
#             left, right = i + 1, N-1
#
#             while left < right:
#                 lst = [nums[left], nums[i], nums[right]]
#
#                 #sum 이 0보다 작으면 left 인덱스, 크면 right 인덱스 수정
#                 if sum(lst) < 0:
#                     left += 1
#                 elif sum(lst) > 0:
#                     right -= 1
#                 else:
#                     result.append(lst)
#
#                     # sort 안할거면 이걸로 중복값 처리 다시 해줘야함
#                     while left < right and nums[left] == nums[left+1]:
#                         left += 1
#                     while left < right and nums[right] == nums[right -1]:
#                         right -= 1
#
#
#                     left += 1
#                     right -= 1
#         return result







# 답지 참고한 브루트 포스 풀이
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         N = len(nums)
#         # 브루트 포스로 풀때 시간 단축위해 정렬하기
#         nums.sort()
#         result = []
#         for x in range(N-2):
#             # 시간단축위해
#             if x>0 and nums[x] == nums[x-1]:
#                 continue
#             for y in range(x+1,N-1):
#                 if y> x+1 and nums[y] == nums[y-1]:
#                     continue
#                 for z in range(y+1,N):
#                     if z> y+1 and nums[z] == nums[z-1]:
#                         continue
#                     if nums[x]+nums[y]+nums[z]==0:
#                         result.append([nums[x],nums[y],nums[z]])
#         return result


# 시간초과
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#
#         rlt = []
#         N = len(nums)
#         for i in range(1<<N):
#             s = []
#             for j in range(N):
#                 if i & (1<<j):
#                     s.append(nums[j])
#             if sum(s) ==0 and len(s) == 3:
#                 s.sort()
#                 if s not in rlt:
#                     rlt.append(s)
#         return rlt