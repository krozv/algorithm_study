def tile_count(N):
    if N <= 2:
        return N
    else:
        count = [0] * (N+1)
        count[1]= 1
        count[2]= 2
        for i in range(3,N+1):
            count[i] = (count[i-1] + count[i-2]) % 15746
        return count[N]
N = int(input()) # 길이
print(tile_count(N))