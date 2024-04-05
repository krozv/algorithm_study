'''
17144. 미세먼지 안녕!

미세먼지를 제거하기 위해 구사과는 공기청정기를 설치
공기청정기의 성능을 테스트하기 위해 집을 R*C인 격자판으로 나타냄
각 칸 (r, c)에 있는 미세먼지의 양을 실시간으로 모니터링
(r, c) => r행 c열

공기청정기는 1번 열에 설치되어 있고 두 행을 차지

1. 미세먼지 작동
(r, c)에 있는 미세먼지는 인접한 네 방향으로 확산
인접한 방향에 공기청정기가 있거나 칸이 없으면 그 방향으로는 확산하지 않음
확산되는 양은 Arc/5 소수점은 버린다.
(r,c)에 남은 미세 먼지의 양은 Arc=Arc/5*(확산된 방향의 개수

2. 공기청정기 작동
위쪽 공기청정기의 바람은 반시계 방향으로 순환
아래쪽 공기청정기의 바람은 시계방향으로 순환
바람이 불면 바람의 방향대로 미세먼지가 모두 한 칸씩 이동
공기청정기로 들어간 미세먼지는 모두 정화된다
'''


# 미세먼지를 확산 시키는 함수 fine_dust_sum
# 매개변수로 행과 열의 길이를 받음
def fine_dust(row, column):
    # 미세 먼지의 확산 결과를 저장할 2차원 배열 chamber_changed 를 정의
    chamber_changed = [[0]*column for _ in range(row)]
    # 4방향으로 확산되기 때문에 델타를 이용
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]

    # 2차원 배열 전체를 순회
    for r in range(row):
        for c in range(column):
            # 만약 공기 청정기의 위치를 만나면 해당 공기 청정기의 위치만 저장해주고 넘어감
            if chamber[r][c] == -1:
                chamber_changed[r][c] = -1
                continue
            # 만약 미세먼지가 있으면
            if chamber[r][c]:
                # 변수 diffusion에 한 방향으로 확산될 수 있는 값을 저장
                diffusion = chamber[r][c] // 5
                # 4방향으로 가보자
                for k in range(4):
                    ni = r+di[k]
                    nj = c+dj[k]
                    # 만약 해당되는 방향이 2차원 배열 안에 있는 경우
                    if 0<=ni<row and 0<=nj<column:
                        # 만약 해당 위치가 공기 청정기라면 넘어감
                        if chamber[ni][nj] == -1:
                            continue
                        # 그게 아니면 그 방향으로 확산해주고
                        chamber_changed[ni][nj] += diffusion
                        # 원래 위치에서는 미세먼지가 줄어듬
                        chamber[r][c] -= diffusion
                    # 4방향으로 모두 가고 나면 줄어든 미세먼지의 양을 복사
                chamber_changed[r][c] += chamber[r][c]
    return chamber_changed


# 공기 청정기 가동을 구현한 purifier
# 매개변수는 앞에서 확산된 미세먼지 분포의 결과와, 행/열의 길이, 공기 청정기의 위치를 받음
def purifier(chamber_changed, row, column, idx):
    # 시작점 si, sj를 공기청정기 바로 위의 위치로 잡고
    # 공기 청정기로 빨려 들어가는 부분을 역으로 탐색할 예정
    si = idx-1
    sj = 0
    # 만약 시작 위치에 값이 있다면, 해당 위치는 공기청정기로 빨려 들어가므로 0으로 바꿔줌
    if chamber_changed[si][sj]:
        chamber_changed[si][sj] = 0
    # 그리고 매 탐색의 이전 위치 값을 저장해줄 변수 pi, pj
    pi = si
    pj = sj
    # 공기 청정기 가동의 반대방향 상, 우, 하, 좌 순서로 탐색
    for di, dj in [-1, 0], [0, 1], [1, 0], [0, -1]:
        # 현재 탐색하는 위치 ni, nj를 정의
        ni = si+di
        nj = sj+dj
        while True:
            # 만약 ni, nj에 값이 있다면
            if chamber_changed[ni][nj]:
                # 해당 값을 이전 위치의 값으로 옮겨주고
                chamber_changed[pi][pj] = chamber_changed[ni][nj]
                # 현재 위치는 0으로 바꿈
                chamber_changed[ni][nj] = 0
            # 현재 위치를 이전 값으로 저장하고
            pi = ni
            pj = nj
            # 다음 값이 2차원 배열 안에 있다면
            if 0<=ni+di<=idx and 0<=nj+dj<column:
                # 공기 청정기를 만났다면 탐색 종료
                if ni+di == idx and nj+dj == 0:
                    break
                # 현재 위치를 갱신해줌
                ni += di
                nj += dj
                continue
            # 다음 값이 범위를 넘어서면 멈추고
            break
        # 현재 위치를 시작점으로 저장하고 방향을 바꿔줌
        si = ni
        sj = nj


    # 아래쪽 방향으로 공기 청정기를 가동하는 순서 나머지는 상동
    si = idx+2
    sj = 0
    if chamber_changed[si][sj]:
        chamber_changed[si][sj] = 0
    pi = si
    pj = sj
    for di, dj in [1, 0], [0, 1], [-1, 0], [0, -1]:
        ni = si+di
        nj = sj+dj
        while True:
            if chamber_changed[ni][nj]:
                chamber_changed[pi][pj] = chamber_changed[ni][nj]
                chamber_changed[ni][nj] = 0

            pi = ni
            pj = nj
            if idx+1<=ni+di<row and 0<=nj+dj<column:
                if ni + di == idx+1 and nj + dj == 0:
                    break
                ni += di
                nj += dj
                continue
            break
        si = ni
        sj = nj
    return chamber_changed


# 행의 길이 R, 열의 길이 C, 공기 청정기 가동 시간 T
R, C, T = map(int, input().split())
chamber = [list(map(int, input().split())) for _ in range(R)]
# 공기 청정기의 위치를 purifier_idx에 저장
purifier_idx = -1
# 첫 번째 열을 순회하며 -1인 값이 나오면 공기청정기의 위치를 저장
for i in range(R):
    if chamber[i][0] == -1:
        purifier_idx = i
        break

# T초 동안 시행, 미세먼지를 확산시키는 함수 fine_dust와 공기 청정기를 가동하는 purifier
for _ in range(T):
    chamber = purifier(fine_dust(R, C), R, C, purifier_idx)

# 미세먼지의 총량을 저장하는 변수 fine_dust_sum
# 공기 청정기 두 대가 -1이므로 초기 값으로 2를 설정해줌
fine_dust_sum = 2
# 행을 순회하며 열로 이루어진 리스트의 합을 fine_dust_sum에 더해줌
for j in range(R):
    fine_dust_sum += sum(chamber[j])
print(fine_dust_sum)


