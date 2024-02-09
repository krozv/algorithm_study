# 12789. 도키도키 간식드리미
# 내 코드
44ms
```python
N = int(input()) #사람 수
array = list(map(int,input().split()))
array.reverse()         #array를 stack으로 잘 활용하려고 뒤집음
s = 1                   #간식받을 사람 순서
stack = []              #아래쪽에 순서대로 넣을 공간
while s <= N:
    if stack and stack[-1]==s:  #스택에 최근 넣은게 s와 같으면 꺼내서 왼쪽에 넣는 느낌
        stack.pop()
        s += 1
        continue
    if array:
        num = array.pop()   #array의 top에서 하나 꺼내기
        if num == s:        #넣을 순서랑 같으면 왼쪽에 넣는 느낌
            s += 1
        else:
            stack.append(num)   #스택
    else:
        print('Sad')
        exit()
print('Nice')
```