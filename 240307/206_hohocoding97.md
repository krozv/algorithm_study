# 206. Reverse Linked List

### 코드
34ms
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = []
        tempListNode = ListNode()
        while head:
            temp.append(head.val)
            head = head.next
        #print(temp) #[1,2,3,4,5]
        A = B =ListNode()
        while temp:
            B.next = ListNode(temp.pop())
            B=B.next
        # A는 0->5->4->3->2->1 순으로 연결되어 있을 거임    
        return A.next
```
근데 아무리 생각해도 위에 방법으로 풀면 안될 것 같아 다시 품

### 재시도