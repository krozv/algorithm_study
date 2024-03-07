'''
Given the head of a singly linked list, reverse the list, and return the reversed list.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# 파이썬 알고리즘 인터뷰 책 풀이
# 그냥 이해한다는 마음으로 코드를 그대로 적어봄
# 근데 아무리 봐도 이해가 안되서 코드를 하나하나씩 갈라서 순서대로 그려봄
# 그러니까 시작점에서 다음 값을 정해주고, 시작점의 next를 이전 값으로 돌려주고, 이전값을 한 칸 땡기고 시작점을 한 칸 땡기는 그런 구조인 것 같다.
# 이제야 Leetcode 제출 방법이랑 연결 리스트 감이 좀 옵니다.
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node, prev = head, None

        while node:
            next = node.next
            node.next = prev
            prev = node
            node = next

        return prev