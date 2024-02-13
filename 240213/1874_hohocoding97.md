```python
def f(sequence):
    i = 0
    num = 1
    stack = []
    result = []
    while True:
        if sequence[i] in stack:  #가장 최근게 순서상 맞으면 빼
            if sequence[i] == stack[-1]:
                result.append('-')
                stack.pop()
                i += 1          #다음 순서로 
            else:
                return False
        else:
            stack.append(num)
            result.append('+')
            num += 1        #번호 증가
        if i == N and not stack:
            return result
import sys
N = int(input())

sequence = [int(sys.stdin.readline()) for _ in range(N)]
result = f(sequence)
if result :
    for i in range(len(result)):
        print(result[i])
else:
    print('NO')
```