# 1234. 비밀번호
### 코드
156ms
```python
class ListNode:
    def __init__(self,data=0,next=None):
        self.data = data
        self.next = next

for tc in range(1, 11):
    N, nums = input().split()
    pre = linked_list = ListNode()
    for i in range(int(N)):
        linked_list.next = ListNode(nums[i])
        linked_list = linked_list.next
    result_linked = pre 
    node = pre.next
    
    while node.next is not None: #현 노드의 next가 None이 아닐 때ㄱ까지
        # print(f'현재 데이터 : {node.data}')
        next_temp = node.next
        if next_temp.data == node.data: #이번거랑 다음거 data가 같으면
            pre.next = next_temp.next #잇기
            node = result_linked.next
            pre = result_linked
        else:
            node = node.next
            pre = pre.next
        copied_linked = result_linked

    result_linked = result_linked.next
    print(f'#{tc}',end=' ')
    while result_linked:
        print(result_linked.data, end='')
        result_linked = result_linked.next
    print()
```
