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
temp에 순서대로 val다 넣은 후 거꾸로 linked list로 만듦

`A = B =ListNode()`에서 B에 값을 넣어도 A의 값도 바뀜.. 서로 참조를 한다? 이걸 뭐라 표현해야 하나...