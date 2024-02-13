class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        node = head
        N = 0
        first = node.val
        num_list = []

        # node의 개수를 구함, 연결 리스트 안의 value 리스트 뽑음
        while node.next:
            num_list.append(node.val)
            node = node.next
            N += 1
        num_list.append(node.val)

        # 기존 node 원상복구
        node = head
        while node:
            if first == num_list[-1]:
                node = node.next
                first = node.val
                num_list.pop()
            else:
                return False
        else:
            return True