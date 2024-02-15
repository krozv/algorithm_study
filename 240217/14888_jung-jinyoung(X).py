def cal(nums, order):
    stack = []
    postfix = 0
    priority = {'*': 2, '/': 2, '+': 1, '-': 1}


N = int(input())
nums = sorted(list(map(int, input().split()))) # 오름차순
cals = list(map(int, input().split())) # +-*%

# 최댓값 연산 순서
max_order =[0]*4 #'-%+*'
for i in range(4):
    if i == 0 :
        max_order[i] = cals[1]
    elif i == 1 :
        max_order[i] = cals[3]
    elif i == 2:
        max_order[i] = cals[0]
    elif i == 3:
        max_order[i] = cals[2]

# 최솟값 연산 순서
min_order =[0]*4 #'+%-*'
for i in range(4):
    if i == 0 :
        max_order[i] = cals[0]
    elif i == 1 :
        max_order[i] = cals[3]
    elif i == 2:
        max_order[i] = cals[1]
    elif i == 3:
        max_order[i] = cals[2]

my_max = 0
my_min = 0

# 휴 . . .