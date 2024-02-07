#닫는 괄호의 짝꿍
pair = {')' : '(',  ']' : '['}
while True:
    S = input()
    stack = []
    #'.'입력되면 종료!
    if S == '.':
        exit()
    for c in S:
        if c in '([':
            stack.append(c)
        elif c in ')]':
            if stack:
                if stack[-1] == pair[c]:    #최근게 짝꿍이면 pop
                    stack.pop()
                else:                       #최근게 짝꿍 아니면 'no'
                    print('no')
                    break
            else:
                print('no')
                break                                   
    else:                                   #break없이 잘 돌았으면
        if stack:                           #stack이 차있으면 'no'
            print('no')
        else:                               #stack이 비어있으면 'yes'
            print('yes')