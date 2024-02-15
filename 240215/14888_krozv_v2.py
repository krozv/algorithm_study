# 14888. 연산자 끼워넣기
import itertools # 시간 초과 해결
import sys
input = sys.stdin.readline
"""
조건
1. 나눗셈은 정수 나눗셈으로 몫만 취함
2. 음수를 양수로 나눌 때에는 음수를 양수로 변경한 뒤, 몫만 음수로 다시 변경
결과
1. 첫째 줄에 만들 수 있는 식의 최댓값
2. 둘째 줄에 만들 수 있는 식의 최솟값
"""
def calculator(op, num_list):
    stk = [num_list[0]]
    for i in range(len(op)):
        if op[i] == '+':
            stk[0] = stk[0] + num_list[i+1]
        elif op[i] == '-':
            stk[0] -= num_list[i+1]
        elif op[i] == '*':
            stk[0] *= num_list[i+1]
        elif op[i] == '/':
            if stk[0] < 0:
                stk[0] = -(-stk[0] // num_list[i+1])
            else:
                stk[0] //= num_list[i+1]
    return stk[0]


N = int(input())
num_list = list(map(int, input().split()))
operator = list(map(int, input().split()))  # +, -, *, // 개수
# operator로 순열 만든 후, num_list에 차례대로 끼워넣어서 계산.
# operator 문자열로 변경
oper_list = ['+', '-', '*', '/']
op = []
for i in range(len(operator)):
    if operator[i] != 0:
        op += operator[i] * [oper_list[i]]

# 최댓값 최솟값은 초기값으로 설정할 예정
max_val = -1e9
min_val = 1e9

for operator in list(itertools.permutations(op)):
    val = calculator(operator, num_list)
    max_val = max(max_val, val)
    min_val = min(min_val, val)
# 43% 오류 해결 -> int로 변형
print(int(max_val), int(min_val), sep='\n')