# 2. Add Two Numbers

### 내 코드
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

### AI의 도움을 받은 코드

56ms
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()  # 더미 노드 생성
        curr = dummy  # 현재 노드를 더미 노드로 초기화
        carry = 0  # 올림 수 초기화

        while l1 or l2 or carry:
            total = carry  # 현재 자릿수의 합
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
                
            carry, val = divmod(total, 10)  # 올림 수와 현재 자릿수의 값 계산
            curr.next = ListNode(val)  # 현재 노드에 새로운 노드 추가
            curr = curr.next  # 현재 노드 이동

        return dummy.next  # 더미 노드 다음부터 결과 반환
```