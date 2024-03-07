class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # 새로운 리스트 만들기
        d = dummy #d는 현재 처리중인 노드의 포인터
        carry = 0  # 올림수 저장할 변수

        while l1 or l2 or carry:  # 리스트 끝나도 올림수 남아있으면 체크

            val = 0
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next

            # 몫, 나머지
            carry, val = divmod(carry + val, 10)
            d.next = ListNode(val)  # 현재노드 뒤에 다른 노드 붙여주기
            d = d.next # d 뒤에 붙이기 위해 포인터 이동

        return dummy.next
