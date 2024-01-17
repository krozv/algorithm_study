T = int(input())

def rotation(arr, N):
    af_list = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            af_list[i][j] = arr[N-1-j][i]
    return af_list


for t in range(1,T+1):
    N = int(input())
    bf_list = [list(map(str, input().split())) for _ in range(N)]
    rot_90 = rotation(bf_list, N)
    rot_180 = rotation(rot_90,N)
    rot_270 = rotation(rot_180, N)

    print(f'#{t}')
    for i in range(N):
        print("".join(map(str, rot_90[i])), end=" ")
        print("".join(map(str, rot_180[i])), end=" ")
        print("".join(map(str, rot_270[i])), end=" ")
        print()
# rot 90,180,270의 첫번째 리스트부터 공백없이 모아 프린트
#rot90 = [1,2,3/,~] rot180=[1,2,3/,~] rot180=[1,2,3/~]
# 123 123 123
