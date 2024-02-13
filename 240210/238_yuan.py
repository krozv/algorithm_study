class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        N = len(nums)
        p = 1
        for i in range(N):
            out.append(p) # 자기자신은 안곱해서 p=1부터 append
            p = p *nums[i] # p는 누적 곱

        # q는 오른쪽부터 곱할 인자
        q = 1
        for j in range(N-1,-1,-1):
            out[j] = out[j] * q # 왼쪽 곱셈결과인 out 에 대해 q를 곱하기
            q = q*nums[j]

        return out



# 시간초과
# N = len(arr)
#
# lst = []
# digit = 1
# i = 0
# while i<N:
#     for j in range(N):
#         if j != i:
#             digit *= arr[j]
#
#     lst.append(digit)
#     i +=1
#     digit = 1
#
# print(lst)