
#input 리스트로 받아서 한번에 출력 
def push(x):
    global top
    top += 1
    st[top] = x

def pop():
    global top
    if top == -1:
        return -1
    else:
        top -=1
        return st[top+1]

inputs = []
N = int(input())
top = -1
st = [0] * (N+1)

for _ in range(N):
    inputs.append(input())

for n in inputs:
    if 'push' in n:
        x = n.split()[1]
        push(x)

    elif n == 'top':
        if top != -1:
            print(st[top])
        else:
            print(-1)

    elif n == 'size':
        print(top+1)

    elif n == 'empty':
        if top ==-1:
            print(1)
        else:
            print(0)

    elif n == 'pop':
        print(pop())



