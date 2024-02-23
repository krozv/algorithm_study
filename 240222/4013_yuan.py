
def dfs(num, dir): # num = 0,1,2,3

    global visit
    visit[num] = 1 # 중복 방지 위한 방문표시
    # num = 1, 2, 3, 4 , dir 은 1, -1
    # num 이 4보다 작을때 num[2] = num[6]
    if num < 3: # 현재값과 다음 자석 값 비교해서 다음 자석 돌리기, 다음에 방문하려는 좌표 방문여부 확인
        if magnet[num][2] != magnet[num+1][6] and not visit[num+1]:
            dfs(num+1, -dir) # 4->3 or 3->2 등등 방향이 바뀌니까 -dir

    if num > 0: #현재값과 이전자석 비교해서 이전 자석 돌리기
        if magnet[num][6] != magnet[num-1][2] and not visit[num-1]:
            dfs(num-1, -dir)

    if dir == 1:
        # 마그넷은 인덱스 0-3으로 저장해놓음 / 시계방향 이동d은 뒤에꺼 앞에 붙이기
        magnet[num] = [magnet[num].pop()] + magnet[num]

    else:
         # 반시계는 앞에꺼 뒤에 붙이기
        magnet[num] = magnet[num][1:] + [magnet[num][0]]



T = int(input())
for tc in range(1,T+1):
    numk = int(input())
    magnet = [list(map(int,input().split())) for _ in range(4)]


    for _ in range(numk):
        x, y = map(int,input().split()) # 한번 input 받을떄마다 즉시 회전하기
        visit = [0, 0, 0, 0] # visit 위치 주의, 한번 돌릴떄마다 업데이트
        dfs(x-1,y) # 자석 번호, 방향

    sum = 0

    for i in range(4):
        if magnet[i][0]:
            sum += 2 ** i


    print(f'#{tc} {sum}')