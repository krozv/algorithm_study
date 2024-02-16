'''
class BAEKJOON
2164. 카드2

1~N까지 번호가 차례대로 붙어 있는 N장의 카드
1번 카드가 제일 위, N번 카드가 제일 아래
제일 위에 있는 카드를 바닥에 버리고 그 다음으로 위에 있는 카드를 제일 아래에 있는 카드 밑으로
'''


from collections import deque   # deque 를 활용


def card2(n):
    # 1~N까지 포함된 데큐 cards 를 정의
    cards = deque([i for i in range(1, N+1)])

    while len(cards) > 1:   # 데큐 내에 하나의 원소만 남기 전까지
        cards.popleft()  # 하나를 버리고
        cards.append(cards.popleft())  # 하나는 맨 밑으로 보냄

    print(cards.pop())  # 히니가 남았을 때 출력


N = int(input())

card2(N)