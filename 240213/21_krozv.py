# 21. Merge Two Sorted Lists
class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list_1st = []
        list_2nd = []
        while list1:
            list_1st.append(list1.val)
            list1 = list1.next
        while list2:
            list_2nd.append(list2.val)
            list2 = list2.next
        total = (list_1st + list_2nd)

        if total:
            total.sort()
            head = ListNode(total[0])
            node = head
            for i in range(1, len(total)):
                node.next = ListNode(total[i])
                node = node.next
            return head
        else:
            return list1

