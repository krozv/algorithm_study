# 234. Palindrome Linked List

### 코드
305ms

linked list를 리스트 형태로 다시 만들어 준 다음 비교하였음

`print(head)`로 형태 확인 했을 때, 
`ListNode{val: 1, next: ListNode{val: 2, next: None}}`와 같이 나타남
```python
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        while head != None:
            arr.append(head.val)
            head = head.next
        
        for i in range(len(arr)//2):
            if arr[i] != arr[-1-i]:
                return False
        return True
```

### 데크를 이용하는 방법

```python
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q = collections.deque() #데크 자료형 선언
        if not head:            #헤드안에 아무것도 없으면 그냥 True 반환
            return True
        
        node = head
        while node is not None:
            q.append(node.val)
            node = node.next
        
        while len(q) > 1:       #q안의 요소가 1개 혹은 0개가 남을 때 까지
            if q.popleft() != q.pop():
                return False
        return True
```