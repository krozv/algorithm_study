# 쇠막대기 자르기
import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    stick = input()
    stick = stick.replace('()', '0')
    stk = []
    stk_cnt = 0
    for i in range(len(stick)):
        if stick[i] == '(':
            stk.append(i)
        elif stick[i] == ')':
            start = stk.pop()
            stk_cnt += stick[start:i+1].count('0') + 1
    print(f'#{t} {stk_cnt}')