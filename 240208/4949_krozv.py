# 4949. 균형잡힌 세상
# stack으로 풀기
"""
stack으로 풀 것임
괄호는 [] () 두 종류
균형잡힌 문자열인지 판단
"""
import sys
# sys.stdin = open('test.txt','r')
# input = sys.stdin.readline
while True:
    string = input()
    if string == '.':
        break
    # stack 생성
    stack = []
    for char in string:
        if char in ['[', '(']:
            stack.append(char)
        else:
            if char in [']', ')']:
                if len(stack) == 0:
                    print('no')
                    break
                if [stack[-1], char] in [['[', ']'], ['(', ')']]:
                    stack.pop()
                # 하기 코드 작성 안할 시 틀림
                else:
                    print('no')
                    break
    else:
        if len(stack) == 0:
            print('yes')
        else:
            print('no')





