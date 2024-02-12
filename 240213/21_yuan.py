# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:


        l1 = list1
        l2 = list2

        #l1이 없을때 or l1, l2 있고 l1이 더 작을떄  l1을 다른 걸로 연결
        if (not l1) or (l1 and l2 and l1.val>l2.val):
            l1,l2 = l2, l1

        #l1이 크거나 같으면 노드 하나씩 결정하고 next 불러옴
        if l1:
            l1.next = self.mergeTwoLists(l1.next,l2)

        return l1


    # class Solution:
    #     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    #         lst1 = []
    #         lst2 = []
    #         while list1.next != None:
    #             lst1.append(list1.val)
    #             list1 = list1.next
    #         lst1.append(list1.val)
    #
    #         while list2.next != None:
    #             lst2.append(list2.val)
    #             list2 = list2.next
    #         lst2.append(list2.val)
    #
    #         lst1.extend(lst2)
    #         lst1.sort()
    #         return lst1