# 2. Add Two Numbers

### 코드
58ms
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp_str1 = ''
        temp_str2 = ''
        while l1:
            temp_str1 = str(l1.val) + temp_str1
            l1 = l1.next
        while l2:
            temp_str2 = str(l2.val) + temp_str2
            l2 = l2.next
        sum_str = list(str(int(temp_str1)+int(temp_str2)))
        A = B = ListNode()
        while sum_str:
            B.next = ListNode(sum_str.pop())
            B = B.next
        return A.next
```