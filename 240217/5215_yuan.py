'''
T = int(input())
for tc in range(1,T+1):

    n, lmt = map(int,input().split())
    hamst = []
    for _ in range(n):
        tas, cal = map(int,input().split())
        hamst.append([tas,cal])

    # 비트 연산자

    mx_tas = 0
    n = len(hamst)
    for i in range(1<<n):
        sum_tas = 0
        sum_cal = 0
        for j in range(n):
            if i & (1<<j):
                sum_tas += hamst[j][0]
                sum_cal += hamst[j][1]

        if sum_cal <= lmt:
            if mx_tas < sum_tas:
                mx_tas = sum_tas

    print(f'#{tc} {mx_tas}')
'''

#백트래킹 # 호준
def f(i, cal_s, score): # 인덱스, 직전까지 칼로리합, 직전까지 점수 합
    global max_score
    if cal_s > max_score:
        max_score = cal_s
    if i==n:
        return # n번까지 다하면 끝

    else:
        if cal_s + data[i][1] <= lmt: # 총칼로리보다 작을때 백트래킹
            f(i+1, cal_s+data[i][1], score+data[i][0])
        f(i+1,cal_s,score) # 클때 cal_에 포함안하고 다음꺼 data[i+1] 찾으러 감


n, lmt = 5, 1000 #총 재료수, 칼로리 한계
data = [list() for _ in range(n)] # 여러줄 이차원 리스트로 받기
max_score = 0
f(0,0,max_score) # 시작인덱스0/칼로리누적0/max넣기
print(max_score)


# 비트 + 백트래킹 # 주연
# 전제 부분집합 구하기 , 점수와 칼로리 계산해서 점수는 높, 칼로리 낮
def f(i,cal_s,max_score):
    if cal_s > lmt: # 중간이라도 칼로리 넘치면 return(백트래킹)
        return
    if i == n: # 인덱스 끝까지 왔을떄
        score = 0
        for j in range(n):
            score += data[j][0]  # 점수 총합 구하기
        if score > max_score:
            max_score = score

    # 비트 만들기
    else:
        bit[i] = 0
        f(i+1, cal_s, max_score)

        bit[i] = 1
        f(i+1, cal_s+data[i][1], max_score) # 백트래킹

n, lmt = 5, 1000 #총 재료수, 칼로리 한계
data = [list() for _ in range(n)] # 여러줄 이차원 리스트로 받기
bit = [0] * N
max_score =  0
f(0,0,max_score) # 시작인덱스0/칼로리누적0/max넣기
print(max_score)
