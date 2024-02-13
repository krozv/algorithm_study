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
            # num_list를 뒤에서부터 연결리스트와 비교
            # 같을 경우 하나씩 제거
            if first == num_list[-1]:
                if node.next:
                    node = node.next
                    first = node.val
                    num_list.pop()
                # node 끝날 경우 True
                else:
                    return True
            # 다를 경우 False
            else:
                return False