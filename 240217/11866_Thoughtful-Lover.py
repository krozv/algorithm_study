'''
class BAEKJOON
11866. 요세푸스 문제 0

1~N, N명의 사람이 원을 이루며 앉아 있음
양의 정수 K(<=N)
순서대로 K번째 사람을 삭제
이 순열을 출력
'''


from collections import deque   # deque 를 활용


def josephus(n, k):
    # 1~N까지 숫자가 들어간 큐를 정의
    q = deque([i for i in range(1, n+1)])

    while q:
        for j in range(k-1):    # 그 이전은 넘기고
            q.append(q.popleft())
        print(q.popleft(), end='')  # k번째 되는 사람만 빼서 출력
        if q:   # 출력 조건인 , 를 포함
            print(',', end=' ')


N, K = map(int, input().split())

print('<', end='')
josephus(N, K)
print('>')
print()