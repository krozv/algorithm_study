'''
임의의 수열을 입력받아,
수를 stack에 넣었다 빼면서 해당 수열을 만들 수 있는지 검증
push는 오름차순으로만 가능

가능한 경우, push를 +, pop을 -로 해서 그 과정을 출력
불가능한 경우 No를 출력
'''

'''
# 1차_틀렸습니다
import sys      # 시간을 줄여 주기 위해

N = int(sys.stdin.readline())

num_array = []      # 입력 받은 수열을 저장할 num_array 정의
stack = []      # 수를 오름차순으로 넣을 stack 생성
top = -1        # stack 의 제일 위의 숫자의 인덱스 top 을 생성
count = 0       # 총 몇 번 숫자까지 push 했는지 count 에 저장
plus_minus = []     # push 와 pop 여부를 저장할 리스트 plus_minus 정의

for i in range(N):
    num = int(sys.stdin.readline())
    num_array.append(num)

for num in num_array:       # 입력한 수열을 순회하며
    if num > count:     # 지금까지 stack에 저장한 적이 없는 수이면
        for j in range(count+1, num+1):     # 해당 수까지 stack 에 오름차 순으로 넣었다가
            stack.append(j)
            plus_minus.append('+')
            top += 1
        count = num

        stack.pop()     # 다시 빼줌
        top -= 1
        plus_minus.append('-')
        continue

    elif stack[top] == num:     # 만약에 이미 넣은 숫자인데 그 수가 제일 위에 있으면 빼줌
        stack.pop()
        top -= 1
        plus_minus.append('-')
        continue

    else:       # 위의 2가지 경우가 아닌 경우에는 수열을 완성할 수 없으므로 'No'를 출력
        print('No')
        break

if count == N and stack == []:      # 주어진 숫자를 모두 stack에 집어 넣었다가 모두 뺐다면
    for k in plus_minus:        # push 와 pop 을 +, - 로 그 순서대로 출력
        print(k)
'''


'''
# 2차_틀렸습니다
# 출력값을 No -> NO 로 바꿔줬는데요...
# 그러고도 3차_틀렸습니다.
import sys      # 시간을 줄여 주기 위해

N = int(sys.stdin.readline())

num_array = []      # 입력 받은 수열을 저장할 num_array 정의
stack = []      # 수를 오름차순으로 넣을 stack 생성
top = -1        # stack 의 제일 위의 숫자의 인덱스 top 을 생성
count = 0       # 총 몇 번 숫자까지 push 했는지 count 에 저장
plus_minus = []     # push 와 pop 여부를 저장할 리스트 plus_minus 정의

for i in range(N):
    num = int(sys.stdin.readline())
    num_array.append(num)

for num in num_array:       # 입력한 수열을 순회하며
    if num > count:     # 지금까지 stack에 저장한 적이 없는 수이면
        for j in range(count+1, num+1):     # 해당 수까지 stack 에 오름차 순으로 넣었다가
            stack.append(j)
            plus_minus.append('+')
            top += 1
        count = num

        stack.pop()     # 다시 빼줌
        top -= 1
        plus_minus.append('-')
        continue

    elif stack[top] == num:     # 만약에 이미 넣은 숫자인데 그 수가 제일 위에 있으면 빼줌
        stack.pop()
        top -= 1
        plus_minus.append('-')
        continue

    else:       # 위의 2가지 경우가 아닌 경우에는 수열을 완성할 수 없으므로 'NO'를 출력
        print('NO')
        break

if len(plus_minus) == N * 2:      # 주어진 숫자를 모두 stack에 집어 넣었다가 모두 뺐다면
    for k in plus_minus:        # push 와 pop 을 +, - 로 하여 시행한 순서대로 출력
        print(k)
'''


# 틀린 원인 파악중
import sys      # 시간을 줄여 주기 위해

N = int(sys.stdin.readline())

num_array = []      # 입력 받은 수열을 저장할 num_array 정의
stack = []      # 수를 오름차순으로 넣을 stack 생성
top = -1        # stack 의 제일 위의 숫자의 인덱스 top 을 생성
count = 0       # 총 몇 번 숫자까지 push 했는지 count 에 저장
plus_minus = []     # push 와 pop 여부를 저장할 리스트 plus_minus 정의

for i in range(N):
    num = int(sys.stdin.readline())
    num_array.append(num)

for num in num_array:       # 입력한 수열을 순회하며
    if num > count:     # 지금까지 stack에 저장한 적이 없는 수이면
        for j in range(count+1, num+1):     # 해당 수까지 stack 에 오름차 순으로 넣었다가
            stack.append(j)
            plus_minus.append('+')
            top += 1
        count = num

        stack.pop()     # 다시 빼줌
        top -= 1
        plus_minus.append('-')
        continue

    elif stack[top] == num:     # 만약에 이미 넣은 숫자인데 그 수가 제일 위에 있으면 빼줌
        stack.pop()
        top -= 1
        plus_minus.append('-')
        continue

    else:       # 위의 2가지 경우가 아닌 경우에는 수열을 완성할 수 없으므로 'NO'를 출력
        print('NO')
        exit()      # break -> exit() 으로 바꾸면 효과가 있을까 ? 효과가 있었다 !

if len(plus_minus) == N * 2:      # 주어진 숫자를 모두 stack에 집어 넣었다가 모두 뺐다면
    for k in plus_minus:        # push 와 pop 을 +, - 로 하여 시행한 순서대로 출력
        print(k)