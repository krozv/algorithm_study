# 1991. 트리 순회
"""
이진 트리
- 전위 순회(preorder traversal)
- 중위 순회(inorder traversal)
- 후위 순회(postorder traversal)
"""


def pre_order(T):
    if T:
        print(node[T], end='')
        pre_order(left[T])
        pre_order(right[T])

def in_order(T):
    if T:
        in_order(left[T])
        print(node[T], end='')
        in_order(right[T])

def post_order(T):
    if T:
        post_order(left[T])
        post_order(right[T])
        print(node[T], end='')


import sys
input = sys.stdin.readline

N = int(input())
node = [0] * (N+1)
par = [0] * (N+1)
left = [0] * (N+1)
right = [0] * (N+1)

for i in range(1, N+1):
    p, l, r = input().split()
    node[i] = p
    left[i] = l
    right[i] = r

left = list(map(lambda x: node.index(x) if x != '.' else 0, left))
right = list(map(lambda x: node.index(x) if x != '.' else 0, right))

pre_order(1)
print()
in_order(1)
print()
post_order(1)