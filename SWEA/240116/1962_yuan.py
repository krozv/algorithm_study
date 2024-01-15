T = int(input())

def rotation(bf_arr,N):
    new_arr = [[0]* N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):  
            new_arr[N-1-j][i] = bf_arr[i][j]
    return new_arr

for tc in range (1,T+1):
    N = int(input())
    arr = [ list(map(str, input().split())) for _ in range(N)]

    rot_90 = rotation(arr, N)
    rot_180 = rotation(rot_90, N)
    rot_270 = rotation(rot_180, N)

    print('#{}'.format(tc))
    for i in range (N):
        print("".join(map(str, rot_90[i])), end=" ")
        print("".join(map(str, rot_180[i])), end=" ")
        print("".join(map(str, rot_270[i])), end=" ")
        print()