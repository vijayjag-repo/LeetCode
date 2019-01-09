# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        Not the ideal solution but one of the ways to solve it is by using conversion from str to int and int to str.
        Ideal methods will have a faster runtime
        
        Approach:
        Scan each element of the linkedlists and append it to a string.
        Reverse both the strings.
        Convert both the strings into integers and add it together and convert it back into string.
        Reverse the string.
        Now add each value from this string as an integer in a list and return it.
        
        """
        number = []
        a = ""
        b = ""
        while(l1):
            a = a + str(l1.val)
            l1 = l1.next
        while(l2):
            b = b + str(l2.val)
            l2 = l2.next
        
        a = a[::-1]
        b = b[::-1]
        
        a = str(int(a) + int(b))
        a = a[::-1]
        for i in a:
            number.append(int(i))
        return(number)
        
        
        
