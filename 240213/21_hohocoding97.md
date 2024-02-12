# 21. Merge Two Sorted Lists


### 외국 똑똑이 코드
34ms
```python
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newHead = dummyHead = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                dummyHead.next = list1
                list1 = list1.next
            else:
                dummyHead.next = list2
                list2 = list2.next
            dummyHead = dummyHead.next
        
        if list1:
            dummyHead.next = list1
        if list2:
            dummyHead.next = list2
        return newHead.next
```

### 좀 더 이해하기 쉽게 혼자 푼 코드
35ms
```python
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy  =ListNode()
        print(list1)
        while list1 and list2:               
            if list1.val < list2.val:
                cur.next =  ListNode(val=list1.val)
                list1, cur = list1.next, cur.next
            else:
                cur.next = ListNode(val=list2.val)
                list2, cur = list2.next, cur.next
                
        if list1 or list2:
            cur.next = list1 if list1 else list2

        return dummy.next
```