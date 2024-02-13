### try 1
```py
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        node1 = list1
        node2 = list2

        while node1 and node2:
            if node2.val >= node1.val :
                node2.val, node2.next, node1.next = node1.val, node2.val, node1.next
            elif node2.val < node1.val :
                node2.val, node2.next, node1.next = node2.val, node1.val, node1.next

        return node2
```

> 다중 할당으로 해결 실패  
> 연결 리스트에 대한 이해 부족 !
> 0 또는 아무것도 입력되지 않았을 경우 생각


### try2

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        node = ListNode(0)
        current = node # 연결 리스트 끝 부분
        # list1과 list2 비교
        while list1 and list2 :
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            # 이동
            current = current.next
        # list1과 list2 중 하나가 0이 되었을 경우, 나머지 하나 추가
        current.next = list1 or list2
        # 생성된 연결리스트 반환
        return node.next

```

> 비교 논리는  `try 1`과 비슷  
> node, current 등 새로운 연결리스트 생성  
> 마지막 `return node.next` 헷갈렸음.  
> `return cuurent.next` 는 마지막 값만 가져옴.  
> `node`는 현재 head 와 마찬가지.  
> `node.next`를 해야 이후 생성된 연결리스트를 반환할 수 있음.