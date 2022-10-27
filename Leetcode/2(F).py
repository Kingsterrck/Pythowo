class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        count = 0
        num1 = 0
        num2 = 0
        while l1.next != None:
            num1 += l1.val * pow(10, count)
            count += 1
            l1 = l1.next
        count = 0
        while l2.next != None:
            num2 += l2.val * pow(10, count)
            count += 1
            l2 = l2.next
        sum = num1 + num2
        return sum;