'''
1991. 트리 순회

이진 트리를 입력 받아, 전위 순회, 중위 순회, 후위 순회한 결과를 출력하는 프로그램을 작성

첫째 줄에는 이진 트리의 노드의 개수 N(1 ≤ N ≤ 26)
둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어진다.
노드의 이름은 A부터 차례대로 알파벳 대문자로 매겨지며, 항상 A가 루트 노드가 된다.
자식 노드가 없는 경우에는 .으로 표현
'''


'''
# 1차시도_틀렸습니다.
# '.'을 remove 하니까 index가 하나씩 밀려서, 오른쪽 자식이 왼쪽 자식이 되어버림
import sys


# 노드의 이름이 순서대로 차례대로 주어지므로, 알파벳에 해당하는 노드의 번호를 아스키 코드를 이용해 구현
# 전위 순회
def preorder(n):
    if n:
        print(chr(n+64), end='')
        # 왼쪽 자식 노드 정보가 있다면
        if left[n] != 0:
            preorder(ord(left[n])-64)
        # 오른쪽 자식 노드 정보가 있다면
        if right[n] != 0:
            preorder(ord(right[n])-64)


# 중위 순회
def inorder(n):
    if n:
        if left[n] != 0:
            inorder(ord(left[n])-64)
        print(chr(n+64), end='')
        if right[n] != 0:
            inorder(ord(right[n])-64)


# 후위 순회
def postorder(n):
    if n:
        if left[n] != 0:
            postorder(ord(left[n])-64)
        if right[n] != 0:
            postorder(ord(right[n])-64)
        print(chr(n + 64), end='')


N = int(sys.stdin.readline())
left = [0] * (N+1)
right = [0] * (N+1)

for i in range(1, N+1):
    info = list(sys.stdin.readline().split())
    # '.' 을 제거
    while '.' in info:
        info.remove('.')
    
    # 왼쪽 자식 노드 정보가 있으면 그 정보를 left 에 저장
    if len(info) >= 2:
        left[ord(info[0])-64] = info[1]
    # 오른쪽 자식 노드 정보가 있으면 그 정보를 left 에 저장
    if len(info) == 3:
        right[ord(info[0])-64] = info[2]

preorder(1)
print()
inorder(1)
print()
postorder(1)
'''

import sys


# 노드의 이름이 순서대로 차례대로 주어지므로, 알파벳에 해당하는 노드의 번호를 아스키 코드를 이용해 구현
# 전위 순회
def preorder(n):
    if n <= N:
        print(chr(n+64), end='')
        # 왼쪽 자식 노드 정보가 있다면
        if left[n] != '.':
            preorder(ord(left[n])-64)
        # 오른쪽 자식 노드 정보가 있다면
        if right[n] != '.':
            preorder(ord(right[n])-64)


# 중위 순회
def inorder(n):
    if n <= N:
        if left[n] != '.':
            inorder(ord(left[n])-64)
        print(chr(n+64), end='')
        if right[n] != '.':
            inorder(ord(right[n])-64)


# 후위 순회
def postorder(n):
    if n <= N:
        if left[n] != '.':
            postorder(ord(left[n])-64)
        if right[n] != '.':
            postorder(ord(right[n])-64)
        print(chr(n + 64), end='')


N = int(sys.stdin.readline())
left = [0] * (N+1)
right = [0] * (N+1)

for i in range(1, N+1):
    info = list(sys.stdin.readline().split())

    # 왼쪽 자식 노드 정보를 left 에, 오른쪽 자식 노드 정보를 right 에
    left[ord(info[0])-64] = info[1]
    right[ord(info[0])-64] = info[2]

preorder(1)
print()
inorder(1)
print()
postorder(1)