# 5639. 이진 검색 트리
"""
왼쪽: 최대힙
오른쪽: 최소힙
전위 순회한 결과를 후위 순회로 변환
"""
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
num = [0]
while True:
    try:
        num.append(int(input()))
    except:
        break
# 전위 순회한 결과
N = 100

right = [0] * (N+1)
left = [0] * (N+1)
par = [0] * (N+1)   # 자식 노드의 인덱스를 인덱스로 부모 노드의 인덱스를 저장한 것

# 노드를 그대로 저장
for i in range(1, len(num)-1):
    if num[i] > num[i+1]:
        par[num[i+1]] = num[i]
        left[num[i]] = num[i+1]
    else:
        if num[i] in left:
            par[num[i+1]] = par[num[i]]
            right[par[num[i]]] = num[i+1]
        else:
            r = par[num[i]]
            p = par[r]
            par[num[i+1]] = p
    print(par)
    print(left)
    print(right)
    print('------')

'''
for i in range(1, len(num)-1):
    print(num[i], num[i+1])
    if num[i] < num[i+1]:
        if num[i] in left:
            print('num[i] in left')
            p = par[i]
            print(num[p])
            left[p] = i
            right[p] = i+1
            par[i+1] = par[i]
        else:
            print('?')
            p = par[i]
            print(num[p])
            par[i+1] = p
            right[p] = i+1
    if num[i] > num[i+1]:
        print('')
        par[i+1] = i    # i+1 노드의 부모는 i
        left[i] = i+1
    print(num)
    print(par)
    print(left)
    print(right)

'''