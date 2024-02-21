def preorder(i):
    if i.isalpha():
        print(i, end= '')
        preorder(tree[i][0])
        preorder(tree[i][1])

def inorder(i):
    if i.isalpha():
        inorder(tree[i][0])
        print(i, end= '')
        inorder(tree[i][1])

def postorder(i):
    if i.isalpha():
        postorder(tree[i][0])
        postorder(tree[i][1])
        print(i, end= '')


N = int(input())
tree = {}   # 문자는 딕셔너리로 넣고 딕셔너리로 빽기

for i in range(N):
    x = input().split()
    p, l, r = x[0], x[1], x[2]
    tree[p] = [l,r]

preorder('A')
print()
inorder('A')
print()
postorder('A')