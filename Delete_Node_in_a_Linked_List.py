# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        
        First change current value to the next value(5->1)
        Then change the link from 1->1->9 as 1->9
        
        """
        node.val = node.next.val
        node.next = node.next.next
        
