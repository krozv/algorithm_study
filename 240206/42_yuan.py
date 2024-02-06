



# 318/322
#
# class Solution:
#     def trap(self, height):
#
#         #height 가 [0,1,2,3,3,2,0] 같은 벽 높이
#         N = len(height)
#         k = max(height)
#
#         #count 는 동일 벽 높이가 몇개있는지 카운트한 리스트
#         count = [0] * (k+1)
#         for i in height:
#             count[i] += 1
#
#         total = 0
#
#         #count의 큰수부터 확인
#         #0층에는 빗물 고이지 않으니까 range(k,0)
#         i = k
#         while i >0:
#
#             if count[i] > 1:
#                 idx_list = []
#                 #height 에서 해당 수의 인덱스 구해서 idx_list만들기
#                 for j in range(N):
#                     if height[j] == i:
#                         idx_list.append(j)
#
#                 # 구한 인덱스 사이의 칸 (== 해당 층의 빗물 고인 칸) 구하기
#                 water = max(idx_list) - 1 - min(idx_list) - (len(idx_list)-2)
#                 total += water
#                 # 1씩 깎아서 다음 층 벽으로 만들어주기
#
#                 for x in idx_list:
#                     height[x] -=1
#                     count[height[x]] +=1
#
#             else:
#                 for j in range(N):
#                     if height[j] == i:
#                         height[j] -= 1
#                         count[height[j]] +=1
#             i -=1
#
#         return total
