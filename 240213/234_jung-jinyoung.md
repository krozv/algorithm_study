### try1
```py
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def isPalindrome(self, head) :
        result = []

        # 연결 리스트가 비어있는지 확인
        if not head:
            return True

        # 연결 리스트 변환
        node = ListNode(head[0])
        current = node
        for val in head[1:]:
            current.next = ListNode(val)
            current = current.next

        # 연렬 리스트 순회, 값 저장
        node = node
        while node:
            result.append(node.val)
            node = node.next

        return result == result[::-1]

sol = Solution()
head = [1,2,2,1]
result = sol.isPalindrome(head)
print(result)
```
- 파이참에서 다시 연결리스트로 변환하는 코드 작성
- 리트코드에서는 연결리스트로 제공
- 연결 리스트의 기본 개념 파악 



### try2
```py
class Solution:

    def isPalindrome(self, head) :
        result = []

        # 연결 리스트가 비어있는지 확인
        if not head:
            return True

        node = head
        # 연렬 리스트 순회, 값 저장
        while node:
            result.append(node.val)
            node = node.next

        # 팰린드롬 판별
        while len(result) > 1:
            if result.pop(0) != result.pop():
                return False
        return True
```

- 연결리스트의 각 데이터를 새로운 연결 리스트에 저장
- 처음엔 `result == result[::-1]` 로 확인하려고 했으나 실패  
    -> 연결리스트 객체로 저장 -> type(linked list object)   
- 연결리스트의 데이터 확인은 pop으로 해야한다는 것을 알았음.
- 시간 많이 걸림



### try 3 
```py
class Solution:

    def isPalindrome(self, head) :
        #Deque 선언 : 리스트로 처리시, 효율성 개선
        # 양방향 모두 O(1)
        # 리스트 양방향 O(n)
        result: Deque = collections.deque()

        # 연결 리스트가 비어있는지 확인
        if not head:
            return True

        node = head
        # 연렬 리스트 순회, 값 저장
        while node :
            result.append(node.val)
            node = node.next

        # 팰린드롬 판별
        while len(result) > 1:
            if result.popleft() != result.pop():
                return False
        return True

```

> `Deque` 활용
- 문자열에서 나왔던 deque 활용
- pop을 사용시 양방향을 모두 확인하고, 순번이 다시 정해지기 때문에 시간이 오래걸림  
- `deque` -> `collections.deque()` => 시간복잡도 O(1)
- 리스트로 작성하는 코드의 효율성을 개선할 수 있는 방법 

### try4 
```py
lass Solution:

    def isPalindrome(self, head) :
        rev = None
        slow = fast = head
        # 런너를 이용해 역순 연결 리스트 구성
        while fast and fast.next:
            fast = fast.next.next # 두 칸씩 이동
            rev, rev.next, slow = slow, rev, slow.next

        # 홀수인 경우 한칸 이동
        if fast:
            slow = slow.next

        # 팰린드롬 확인
        while rev and rev.val == slow.val :
            slow, rev = slow.next, rev.next

        return not rev
```
>연결 리스트에서 가장 많이 활용되는 `런너`
- slow, fast : 한 칸씩 이동하는 slow, 두 칸씩 이동하는 fast 설정 
- 중간까지 slow의 val을 역순으로 저장 :  
`rev, rev.next, slow = slow, rev, slow.next`
- 홀수인 경우 fast를 활용하여 한칸 이동
- 팰린드롬 확인 : pop 함수 안써도 됨. 

