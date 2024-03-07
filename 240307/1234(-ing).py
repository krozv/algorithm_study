# 다 못 풀었는데 그냥 올렸습니다.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None
        self.length = 0

    def __len__(self):
        return self.length

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = Node(data)
        self.length += 1

    def remove_nums(self):
        # 종료조건 : 같은 문자가 나오면 삭제하고 다시 처음으로 돌아가서 탐색
        # 만약 끝까지 탐색을 마치면 결과를 반환
        now = self.head
        prev = now
        now = now.next
        next = now.next

        while next.next is True:
            if now == next:
                prev.next = next.next
                now = self.head
                prev = now
                now = now.next
                next = now.next
                continue
            prev = now
            now = next
            next = now.next


for tc in range(1, 11):
    numbers = list(input())
    pwd = Linkedlist()
    for num in numbers:
        pwd.append(num)

    pwd.remove_nums()

    print(f'#{tc}', end=' ')
    node = pwd.head
    while node is True:
        print(node, end='')
        node = node.next

