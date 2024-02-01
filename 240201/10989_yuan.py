N = int(input())
data = [int(input()) for _ in range(N)]

for i in range(N):
    for j in range(N-1):
        if data[j] < data[j+1]:
            data[j], data[j+1] = data[j+1], data[j]

print(*data, sep='\n')



# # max 값 구하기
# k = 0
# for i in data:
#     if i> k:
#         k = i

# # count와  temp
# count = [0] * (k+1)
# temp = [0] * N

# # 누적값 count 리스트 구하기
# for i in range(N):
#     count[data[i]] += 1
#
# for j in range(1, k+1):
#     count[j] = count[j-1] + count[j]
#
# # temp 에 넣기
#
# for i in range(N):
#     count[data[i]] -= 1
#     temp[count[data[i]]] = data[i]
#
# print(*temp, sep='\n')