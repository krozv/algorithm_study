# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lst = []
        while head.next != None:
            lst.append(head.val)
            head = head.next
        lst.append(head.val)

        N = len(lst)
        left = 0
        right = N - 1

        while left < right:
            if lst[left] != lst[right]:
                return False
            else:
                left += 1
                right -= 1

        if left == right or left - right == 1:
            return True
        else:
            return False