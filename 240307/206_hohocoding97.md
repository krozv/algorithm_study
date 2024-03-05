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

### 이것저것 찾아보고 재시도
35ms
```python
# 연결 리스트 노드 정의
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 연결 리스트 뒤집기 함수
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        node = head
        while node:
            next_temp = node.next
            node.next = prev #이전까지 저장된 녀석들을 node의 뒤에 붙여주기
            prev = node      #그 후 prev를 다시 갱신
            node = next_temp #node를 미리 저장해 두었던 다음 녀석들로 바꿔준다.
        return prev
```