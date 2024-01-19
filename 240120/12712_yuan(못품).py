# T = int(input())
# n,m 인풋받아야함
N = int(input())
M = int(input())

#N+2M=2 행렬로 만들기
grid_0 = [[0]*(N + 2*M - 2) for _ in range(N + 2*M - 2)]
grid_input = [list(map(int, input().split())) for _ in range(N)]

# print(grid_0)
# print(grid_input)

# grid_0 에 grid_input 넣기
for i in range(N):
    for j in range(N):
        grid_0[i+M-1][j+M-1] = grid_input[i][j]

print(grid_0)


# #십자가
# sum_list = []
# for i in range(N):#빨간박스 가로이동
#     for j in range(N):#빨간박스 세로이동
#         sum = 0
#         for x in range(M, 2*M):
#             sum += grid_0[i+x][j]
#         for x in range(M, 2*M):
#             sum += grid_0[i][j+x]
#
#         sum -= grid_0[i][j]
#         sum_list.append(sum)
#
# print(sum_list)