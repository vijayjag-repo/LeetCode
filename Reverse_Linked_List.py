# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        Approach:
        Let's do a testcase
            head = 1->2->3->null, prev = None, current = 1->2->3->null
        1)
        while node exists in current,
            temp = 2->3->null
            current.next = null
            prev = 1->null
            current = 2->3->null
        prev = 1->null
        2)
        while node exists in current,
            temp = 3->null
            current.next = 1->null
            prev = 2->1->null
            current = 3->null
        prev = 2->1->null. After the while, prev looks like this 3->2->1->null
        """
        prev = None
        current = head
        while(current):
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return(prev)
            
            
