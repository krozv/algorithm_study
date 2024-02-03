N = int(input()) #5십만 이하
arr = [int(input()) for _ in range(N)]

#1 산술평균
total = 0
for i in range(N):
    total += arr[i]
print(round(total/N))

# #2 중앙값
sort_arr = sorted(arr)
print(sort_arr[int((N-1)/2)])

#3 최빈값

# 최대값
arr0 = [0] * 8001

#원래값 +4천인 인덱스에 넣기
for i in arr:
    arr0[i+4000] += 1

maxidx = 0
for index in arr0:
    if index > maxidx:
        maxidx = index # 중복가장많이된게 몇번인지

indexlist= []
if arr0.count(maxidx) >1: #중복있을때
    for idx in range(8001): # 인덱스 레인지는 0~ 8천
        if arr0[idx] == maxidx:
            indexlist.append(idx)

    print(int(indexlist[1]) - 4000) # 최빈값중 두번쨰 작은 값
else:
    maxnum = arr0.index(maxidx)
    print(int(maxnum)-4000) # 중복없으면 maxidx 에 4천만 뺴서 프린트

'''
frq = 0 # 자주 나온 넘버 
frq_n = 0 #나온 횟수 세기
if arr0.count(maxidx) >0:
    for idx in range(800):
    if arr0[idx] == maxidx:
        frq_n +=1
        if frq_n ==2:  # n번째꺼 세는법은 카운트 값으로 하면 편함 
            : print(frq_n) 


'''


# 4. 범위
Max = arr[0]
Min = arr[0]
for numb in arr:
    if numb>Max:
        Max = numb
    elif numb <Min:
        Min = numb
print(Max-Min)