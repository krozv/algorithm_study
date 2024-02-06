# 빙고판 작성
square = [list(map(int, input().split())) for _ in range(5)]
# 숫자 부르기
numbers = [list(map(int, input().split())) for _ in range(5)]
###########
# 빙고 확인 리스트 초기화
left_cross = 0 #왼쪽 대각선
right_cross = 0 #오른쪽 대각선
############


# 숫자 위치 확인
positions = [] #숫자 위치 인덱스
bingo = 0 # 빙고 초기화

for i in range(5):
    for j in range(5):
       for k in range(5):
            l = 0
            while l < 5 and square[k][l] != numbers[i][j] :
                    l += 1
            if l < 5:
                square[k][l] = 0
                positions.append([i, j])
                # 대각선 확인
                if k == l:
                    left_cross +=1
                if l == 4-k:
                    right_cross +=1
                # 빙고 확인
                if left_cross == 5 or right_cross == 5:
                    bingo +=1

            # 가로, 세로 빙고 확인
                counts = 0
                for m in range(5):
                    for n in range(5) :
                        # 가로 빙고 확인
                        if square[m][n] == 0:
                            counts +=1
                        if counts == 5 :
                            bingo +=1
                        counts = 0
                        # 세로 빙고 확인
                        if square[n][m] == 0:
                            counts +=1
                        if counts == 5 :
                            bingo +=1
                        counts = 0
                if bingo >= 3:
                    break
       if bingo >= 3:
           break
print(len(positions))