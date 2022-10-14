class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1
        else:
            curr = self.head

            for _ in range(index):
                curr = curr.next
            return curr.val


    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(0, val)


    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index > self.size:
            return

        ele = ListNode(val)
        curr = self.head

        if index <= 0:
            ele.next = curr
            self.head = ele
        else:
            for _ in range(index-1):
                curr = curr.next
            ele.next = curr.next
            curr.next = ele

        self.size += 1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index >= self.size or index < 0:
            return
        
        curr = self.head

        if index == 0:
            self.head = self.head.next
        else:
            for _ in range(index-1):
                curr = curr.next
            curr.next = curr.next.next

        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
