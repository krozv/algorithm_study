'''
11725. 트리의 부모 찾기

루트 없는 트리
이때 루트가 1일 때 각 노드의 부모를 구하는 프로그램

첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)
둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점
'''


'''처음에 파이참에서 돌려봤을 때, 뒤죽박죽으로 나와서 잘 살펴보니 애초에 루트가 없는 트리에 루트를 1로 지정한 것이었어서
루트가 1일 때 조건을 문제에 적용시키어 결과값을 출력하는게 중요 !'''

'''
# 1차시도_틀렸습니다.
# 그러니까 루트 노드에서의 거리가 정의되지 않은 상태에서 연결된 두 정점이 주어지면 무조건 앞-부모 뒤-자녀로 받게 됨
import sys

N = int(sys.stdin.readline())
# 트리의 깊이를 저장하는 d
d = [-1] * (N+1)
# 루트를 1이라고 하기로 했으므로 0 을 지정
d[1] = 0
# 조상 노드를 저장해 줄 anc
anc = [0] * (N+1)
for i in range(N-1):
    # 조상을 p, 자식을 c
    p, c = map(int, sys.stdin.readline().split())
    # 만약 깊이가 더 낮은게 p 로 되어 있으면 자리를 바꿔준다.
    if d[p] < d[c]:
        p,c = c, p

    anc[c] = p
    d[c] = d[p] + 1

# for j in range()

for k in range(2, N+1):
    print(anc[k])'''

'''
# 2차시도_RecursionError
# 재귀를 쓰지 말아보자?
import sys


# 부모 노드를 찾는 함수 who_is_my_parent 를 정의
def who_is_my_parent(n):
    # link 를 순회하며 깊이를 비교하며 조상을 저장
    for i in link[n]:
        if anc[i] == 0 and d[n] > d[i]:
            anc[i] = n
            d[i] = d[n] + 1

            who_is_my_parent(i)


N = int(sys.stdin.readline())
# 트리의 깊이를 저장하는 d
d = [-1] * (N+1)
# 루트를 1이라고 하기로 했으므로 0 을 지정
d[1] = 0
# 연결된 정점을 저장하는 link
link = [[] for _ in range(N+1)]
# 조상 노드를 저장해 줄 anc
anc = [0] * (N+1)
for j in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    link[a].append(b)
    link[b].append(a)

who_is_my_parent(1)

for k in range(2, N+1):
    print(anc[k])'''

'''import sys

N = int(sys.stdin.readline())
# 트리의 깊이를 저장하는 d
d = [N] * (N+1)
# 루트를 1이라고 하기로 했으므로 0 을 지정
d[1] = 0
# 조상 노드를 저장해 줄 anc
anc = [0] * (N+1)
for i in range(N-1):
    # 조상을 p, 자식을 c
    p, c = map(int, sys.stdin.readline().split())
    # 만약 깊이가 더 깊은게 p 로 되어 있으면 자리를 바꿔준다.
    if d[p] > d[c]:
        p,c = c, p

    anc[c] = p
    d[c] = d[p] + 1

for k in range(2, N+1):
    print(anc[k])'''


'''import sys
# 4차시도_시간초과
N = int(sys.stdin.readline())
# 트리의 깊이를 저장하는 d
d = [N] * (N+1)
# 루트를 1이라고 하기로 했으므로 0 을 지정
d[1] = 0
# 조상 노드를 저장해 줄 anc
anc = [0] * (N+1)

wait = []

for i in range(N-1):
    # 조상을 p, 자식을 c
    p, c = map(int, sys.stdin.readline().split())

    # 입력 받은 두 정점의 상하 관계 여부를 파악할 수 없으면 일단 지나감
    if d[p] == d[c]:
        wait.append([p, c])
        continue

    # 만약 깊이가 더 낮은게 p 로 되어 있으면 자리를 바꿔준다.
    elif d[p] > d[c]:
        p, c = c, p

    anc[c] = p
    d[c] = d[p] + 1

while wait:
    for i in wait:
        wp = i[0]
        wc = i[1]
        if d[wp] < d[wc]:
            anc[wc] = wp
        elif d[wp] > d[wc]:
            anc[wp] = wc

for k in range(2, N+1):
    print(anc[k])'''

'''import sys
from collections import deque


# 부모 노드를 찾는 함수 who_is_my_parent 를 정의
def who_is_my_parent(n):
    # link 를 순회하며 깊이를 비교하며 조상을 저장
    for i in link[n]:
        p = n
        c = i

        if d[p] > d[c]:
            p, c = c, p

        if anc[c] <= 0:
            anc[c] = p
            d[c] = d[p] + 1

        who_is_my_parent(c)


N = int(sys.stdin.readline())
# 트리의 깊이를 저장하는 d
d = [N] * (N+1)
# 루트를 1이라고 하기로 했으므로 0 을 지정
d[1] = 0
# 연결된 정점을 저장하는 link
link = deque([[] for _ in range(N+1)])
# 조상 노드를 저장해 줄 anc
anc = [0] * (N+1)
# 위 식에서 1에 걸리지 않기 위해
anc[1] = -1
for j in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    link[a].append(b)

who_is_my_parent(1)

for k in range(2, N+1):
    print(anc[k])'''

'''import sys
from collections import deque

N = int(sys.stdin.readline())
# 트리의 깊이를 저장하는 d
d = [N] * (N+1)
# 루트를 1이라고 하기로 했으므로 0 을 지정
d[1] = 0
# 조상 노드를 저장해 줄 anc
anc = [0] * (N+1)

wait = deque()

for i in range(N-1):
    # 조상을 p, 자식을 c
    p, c = map(int, sys.stdin.readline().split())

    # 입력 받은 두 정점의 상하 관계 여부를 파악할 수 없으면 일단 지나감
    if d[p] == d[c]:
        wait.append([p, c])
        continue

    # 만약 깊이가 더 낮은게 p 로 되어 있으면 자리를 바꿔준다.
    elif d[p] > d[c]:
        p, c = c, p

    anc[c] = p
    d[c] = d[p] + 1

while wait:
    wp = wait[0][0]
    wc = wait[0][1]
    if d[wp] < d[wc]:
        anc[wc] = wp
    elif d[wp] > d[wc]:
        anc[wp] = wc
    wait.popleft()

for k in range(2, N+1):
    print(anc[k])'''

'''import sys

N = int(sys.stdin.readline())
# 트리의 깊이를 저장하는 d
d = [N] * (N+1)
# 루트를 1이라고 하기로 했으므로 0 을 지정
d[1] = 0
# 조상 노드를 저장해 줄 anc
anc = [0] * (N+1)
anc[1] = -1
wait = []
for i in range(N-1):
    # 조상을 p, 자식을 c
    p, c = map(int, sys.stdin.readline().split())

    if d[p] == d[c]:
        wait.append([p,c])
        continue

    # 만약 깊이가 더 낮은게 p 로 되어 있으면 자리를 바꿔준다.
    if d[p] > d[c]:
        p,c = c, p

    anc[c] = p
    d[c] = d[p] + 1

for j in wait:
    j[0] = p
    j[1] = c

    if d[p] == d[c]:
        wait.append([p, c])
        continue

    if d[p] > d[c]:
        p, c = c, p

    anc[c] = p
    d[c] = d[p] + 1

for k in range(2, N+1):
    print(anc[k])'''

'''
몇 번을 다시 푼지 기억도 안난다. 아이디어는 비슷했는데 재귀 안 쓰고 풀려다가 호준이 형 코드 보고
아 맞다 이렇게 하는거지 하고 풀어버렸으ㅓㅁ
'''
import sys
from collections import deque


# 부모 노드를 찾는 함수 who_is_my_parent 를 정의
def who_is_my_parent(n):
    q = deque()
    q.append(n)

    while q:
        p = q.pop()
        # p 와 연결된 것들을 탐색하며 방문 안했다면 방문하고, anc 에 추가
        for i in link[p]:
            if checked[i] == 0:
                anc[i] = p
                checked[i] = 1
                q.append(i)


N = int(sys.stdin.readline())
# 이미 조상을 확인한 곳을 표시하는 checked, 초기값 1을 체크
checked = [0] * (N+1)
checked[1] = 1
# 연결된 정점을 저장하는 link
link = [[] for _ in range(N+1)]
# 조상 노드를 저장해 줄 anc
anc = [0] * (N+1)
# 1은 조상이 없으므로 미리 -1을 체크
anc[1] = -1
for j in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    # 어느게 부모고 어느게 자식인지 족보가 꼬였다.
    link[a].append(b)
    link[b].append(a)

who_is_my_parent(1)

for k in range(2, N+1):
    print(anc[k])
