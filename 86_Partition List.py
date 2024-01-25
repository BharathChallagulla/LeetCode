# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        
        less_list_head = ListNode()
        more_list_head = ListNode()
        
        less_list = less_list_head
        more_list = more_list_head
        temp = head
        while temp is not None:
            if temp.val < x:
                less_list.next = ListNode(temp.val)
                less_list = less_list.next
            else:
                more_list.next = ListNode(temp.val)
                more_list = more_list.next
            temp = temp.next
        less_list.next = more_list_head.next
        return less_list_head.next