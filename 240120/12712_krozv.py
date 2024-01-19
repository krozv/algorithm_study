# 파리퇴치 3
T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    flies = []
    for _ in range(N):
        flies.append(list(map(int, input().split())))
        # print(flies)

    catched_flies = []
    catched_flies_plus = 0
    catched_flies_x = 0
    for x in range(N):
        for y in range(N):
            for i in range(-M+1, M):
                # +로 뿌릴 경우
                if x-i < 0 or x-i > N-1:
                    catched_flies_plus += 0
                else:
                    catched_flies_plus += flies[x-i][y]

                if y-i < 0 or y-i > N-1:
                    catched_flies_plus += 0
                else:
                    catched_flies_plus += flies[x][y-i]
                # x로 뿌릴 경우
                if x-i < 0 or x-i > N-1:
                    catched_flies_x += 0
                elif y-i < 0 or y-i > N-1:
                    catched_flies_x += 0
                else:
                    catched_flies_x += flies[x-i][y-i]

                if x-i < 0 or x-i > N-1:
                    catched_flies_x += 0
                elif y+i < 0 or y+i > N-1:
                    catched_flies_x += 0
                else:
                    catched_flies_x += flies[x-i][y+i]
            # 가운데 중복값 제외
            catched_flies_plus -= flies[x][y]
            catched_flies_x -= flies[x][y]
            # x방향, +방향 중 더 많이 잡은 파리 수 세기
            catched_flies.append(max(catched_flies_x, catched_flies_plus))
            # for문이므로 변수 reset
            catched_flies_x = 0
            catched_flies_plus = 0
    print(f'#{t+1} {max(catched_flies)}')