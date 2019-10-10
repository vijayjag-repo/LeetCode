import heapq
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        
        Approach:
        
        Have two heaps(min and max heap).
        Max heap will have the smaller half of elements and min heap will have the larger half of elements.
        """
        self.left = []
        self.right = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if(len(self.left)==len(self.right)):
            heapq.heappush(self.right,-heapq.heappushpop(self.left,-num))
        else:
            heapq.heappush(self.left,-heapq.heappushpop(self.right,num))
        
    def findMedian(self):
        """
        :rtype: float
        """
        if(len(self.left)==len(self.right)):
            return float(self.right[0]-self.left[0])/2
        else:
            return float(self.right[0])


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
