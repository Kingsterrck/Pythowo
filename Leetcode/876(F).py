# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        values = []
        head2 = head
        while head2.next != None:
            values.append(head.val)
            head2 = head2.next
        med = values[int(len(values) / 2)]

        while True:
            if head.val == med:
                return head
            else:
                head = head.next