# 백트래킹

def dfs(idx,l):
    global res
    if l == N//2: # l은 한팀의 사람수
        sum_left = 0
        sum_right = 0
        for i in range(N):
            for j in range(N):
                if ved[i] == 1 and ved[j] == 1: # 둘다 방문했을때 방문시의 인덱스 sum출력
                    sum_left += arr[i][j]
                elif ved[i] == 0 and ved[j] ==0: # 동시에 안방문한 사람들은 다른쪽 팀이 됨
                    sum_right += arr[i][j]

        res = min(abs(sum_left - sum_right), res) # result 는 무조건 더 작은 값
        return # 함수 끝나는지점

    # 순열 만드는 재귀함수 파트
    for i in range(idx,N):
        if ved[i] ==0: #아직 방문안한 i에 대해
            ved[i] = 1
            dfs(idx+1,l+1) # 인덱스와 l에 1씩 더해주기. idx는 이전 방문장소 방문 안하기 위한 포인터 (i range가 idx부터니까)
            ved[i] = 0 # 중복 순열 막기 위해 다시 원래대로 복구해주기


import sys
N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ved = [0] * N #index i 에 방문했는지 #visited
res = float('inf') # 아무거나 큰수

dfs(0,0) # 0,0부터 시작
print(res)




# 순열 함수 import
# from itertools import permutations
# import sys
#
# N = int(input())
# p = [i for i in range(N)]
# arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
#
# min = 1000000
# for i in permutations(p,N):
#     left = i[0:int(N/2)]
#     right = i[int(N/2):]
#
#     # print(left, right)
#
#     left_sum = 0
#     right_sum = 0
#     for i in left:
#         for j in left:
#             left_sum +=arr[i][j]
#     for i in right:
#         for j in right:
#             right_sum +=arr[i][j]
#
#     mn = abs(left_sum - right_sum)
#
#     if mn < min:
#         min = mn
#
# print(min)



# def f2(x,N):
#     global min
#
#     left = x[0:int(N/2)]
#     right = x[int(N/2):]
#     # print(left, right)
#     left_sum = 0
#     right_sum = 0
#     for i in left:
#         for j in left:
#             left_sum +=arr[i][j]
#     for i in right:
#         for j in right:
#             right_sum +=arr[i][j]
#
#     mn = abs(left_sum - right_sum)
#
#     if mn < min:
#         min = mn
#     # print(min)
#     return min
#
# def f1(i,k):
#     if i ==k:
#         # print(p)
#         return f2(p,k)
#     else:
#         for j in range(i,k):
#             p[i], p[j] = p[j], p[i]
#             f1(i+1,k)
#             p[i], p[j] = p[j], p[i]
#
# N = int(input())
# p = [i for i in range(N)]
# arr = [list(map(int, input().split())) for _ in range(N)]
# min = 100000000
#
# f1(0,N)
# print(min)