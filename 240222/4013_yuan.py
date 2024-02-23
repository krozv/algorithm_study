
def check(q1,q2,q3,q4):
    ch = [0,0,0,0]
    if q1[2] == q2[6]:
        ch[0] = 1
    if q2[2] == q3[6]:
        ch[1] = 1
    if q3[2] == q4[6]:
        ch[2] = 1

    return ch


def rot(n,d):
    if n == 0:
        if dir == 1:
            t1= q1.popleft()
            q1= t1+ q1

            t2 = q2.pop()
            q2 =

        elif dir == -1:

    if n == 1:
        if dir == 1:

        elif dir == -1:

    if n == 2:
        if dir == 1:

        elif dir == -1:

    if n == 3:
        if dir == 1:

        elif dir == -1:



T = int(input())
rot_k = int(input()) # 회전횟수
q1 = [list(map(int,input().split())) for _ in range(8)]
q2 = [list(map(int,input().split())) for _ in range(8)]
q3 = [list(map(int,input().split())) for _ in range(8)]
q4 = [list(map(int,input().split())) for _ in range(8)]


rot_lst = [list(input().split()) for _ in range((rot_k))]

while rot_lst:
    wheel, dir = rot_lst. popleft()
    ch = check(q1,q2,q3,q4) # ch = [0,1,0,1]
    fal_num = ch.index(0)
    q1,q2,q3,q4 = rot(fal_num,dir)

sum = 0
if q1[0]: sum +=1
if q2[0]: sum +=2
if q3[0]: sum +=4
if q4[0]: sum +=8
print(sum)