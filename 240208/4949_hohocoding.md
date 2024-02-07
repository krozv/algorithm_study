# 균형잡힌 세상
### 코드
340ms
```python
pair = {')' : '(',  ']' : '['}              #닫는 괄호와 여는 괄호를 각각 딕셔너리 key와 value로
while True:
    S = input()
    stack = []
    if S == '.':                            #'.'입력되면 종료!
        exit()
    for c in S:                             #입력받은 문자열 순회
        if c in '([':                       #여는 괄호 만나면 stack에 추가
            stack.append(c)
        elif c in ')]':                     
            if stack:                       #닫는 괄호 만났는데 stack이 차있으면
                if stack[-1] == pair[c]:    #최근게 짝꿍이면 pop
                    stack.pop()
                else:                       #최근게 짝꿍 아니면 'no'
                    print('no')
                    break
            else:                           #닫는 괄호 만났는데 stack이 비어있으면 'no'
                print('no')
                break                                   
    else:                                   #break없이 잘 돌았으면
        if stack:                           #stack이 차있으면 'no'
            print('no')
        else:                               #stack이 비어있으면 'yes'
            print('yes')
```