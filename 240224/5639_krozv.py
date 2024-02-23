# 5639 test

def re_pre_order(N):
    if N:
        re_pre.append(N)
        re_pre_order(left[N])
        re_pre_order(right[N])

def post_order(N):
    if N:
        post_order(left[N])
        post_order(right[N])
        post.append(N)
'''
a = [1, 2, 3, 4, 5]
left = [0, 2, 4, 0, 0, 0]
right = [0, 3, 5, 0, 0, 0]
'''


import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
num = [0]
while True:
    try:
        num.append(int(input()))
    except:
        break

N = len(num)
left = [0] * (N+1)
right = [0] * (N+1)
par = [0] * (N+1)

for i in range(1, N-1):


post = []
post_order(1)
print(post)