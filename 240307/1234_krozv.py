# 비밀번호
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

import sys
sys.stdin = open('input.txt', 'r')
T = 10
for t in range(1, T+1):
    N, num_list = input().split()
    head = None
    node = head
    # 연결리스트로 저장
    for num in num_list:
        if head is None:
            head = Node(num)
            node = head
        else:
            node.next = Node(num)
            node = node.next

    while True:
        test = False
        node = head
        prev = None
        while node.next:
            k = head
            if node.data == node.next.data:
                # prev 있고 node.next.next도 있을 때
                if prev and node.next.next:
                    test = True
                    node = node.next.next
                    prev.next = node
                # node.next.next가 없을 때
                elif prev and not node.next.next:
                    test = True
                    prev.next = None
                    break
                # prev가 없을때(처음 시작하자마자 동일값인 경우)
                elif node.next.next:
                    test = True
                    head = node.next.next
                    node = head
                    # 여기 수정해야함
            else:
                prev = node
                node = node.next
            # res = 'Head'
            # while k is not None:
            #     res += ' -> ' + str(k.data)
            #     k = k.next
            # print(res)
        if test is False:
            break
    print(f'#{t}', end=' ')
    while head:
        print(head.data, end='')
        head = head.next
    print()
