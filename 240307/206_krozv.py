"""
연결리스트를 뒤집어서 출력
list range 0 ~ 5000
"""
from typing import Optional
# 연결리스트 클래스 생성
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]):
        l2 = ListNode()
        head2 = l2
        if head:
            while head.next:
                node = head
                while node.next:
                    prev = node
                    node = node.next
                    prev.next = node
                prev.next = None
                l2.next = ListNode(node.val)
                l2 = l2.next
            l2.next = ListNode(head.val)
            head2 = head2.next
            return head2
        else:
            return head


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)

s = Solution()
l2 = ListNode()
result = s.reverseList(l1)