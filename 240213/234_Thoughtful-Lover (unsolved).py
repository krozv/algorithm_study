# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q: my_list = []

        node = head

        while node is not None:
            q.append(node.val)
            node.val = node.next

        '''N = len(my_list)
        count = 0
        for i in range(N//2 + 1):
            if my_list[i] == my_list(-(i+1)):
                count += 1

        if count == N//2:
            return True
        else:
            return False'''

        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False
            else:
                return True