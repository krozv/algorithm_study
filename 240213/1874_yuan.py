def push(x):
    global top
    top += 1
    st[top] = x
    rlt.append('+')

def pop():
    global top
    if top == -1:
        return 'underflow'
    else:
        top -=1
        rlt.append('-')
        return st[top+1]

N = int(input())

#input 리스트
ipt_list = [int(input()) for _ in range(N)]

#+ 또는 - 저장할 rlt 리스트
rlt = []

#큰수 이후에는 모두 내림차순이어야함 -> 해당 경우 no 부터 찾기
max_idx = ipt_list.index(N)

sort_list = sorted(ipt_list[max_idx:], reverse=True)
if sort_list != ipt_list[max_idx:]:
    print('NO')

#큰수 이후 모두 내림차순인 경우 판단
else:
    top = -1
    st = [0] * (N+1)

    i = 1
    j = 0 # j는 ipt_list의 인덱스
    while i < N+1:
        if i <= ipt_list[j]:
            push(i)
            i +=1
        else:
            if pop() != ipt_list[j]: #중간에 다른 경우 break
                break
            else:
                j +=1

    #i = N+1이 되었을때만 내림차순으로 전부 뱉기
    if i == N+1:
        while top != -1:
            pop()
        for x in rlt:
            print(x)
    else:
        print('NO')