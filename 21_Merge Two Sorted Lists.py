# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1:
            return list2
        
        if not list2:
            return list1
        newList = None
        tempList = None
        while list1 and list2:
            minimList = None
            if list1.val <= list2.val:
                minimList = list1
                list1 = list1.next
            else:
                minimList = list2
                list2 = list2.next
            minimList.next = None
            if newList is None:
                    newList = minimList
                    tempList = newList
            else:
                tempList.next = minimList
                tempList = tempList.next

        if list1:
            tempList.next = list1
        
        if list2:
            tempList.next = list2
        
        return newList
