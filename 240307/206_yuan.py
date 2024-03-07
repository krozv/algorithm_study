
'''
40ms

'''

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        #새로운 리스트 노드 만들 목적
        rev = None

        while head != None:
            # rev= head 로 두면 연결리스트 됨,
            # rev.next 를 바로 이전 rev로 바꾸면 head와 val는 동일하되 연결된 링크는 달라짐
            # head는 연결리스트 하나씩 삭제 head = head.next
            rev, rev.next, head = head, rev, head.next
        return rev
