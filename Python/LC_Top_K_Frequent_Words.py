class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        Approach:
        
        Counter approach
        Time: O(nlogn)
        Space: O(n)
        """
        count = collections.Counter(words)
        candidates = count.keys()
        candidates.sort(key = lambda w: (-count[w],w))
        return(candidates[:k])
#Approach 2 - Heap        
import heapq
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        
        Time: O(nlogk)
        Space: O(n)
        """
        count = collections.Counter(words)
        heap = [(-freq,word) for word,freq in count.items()]
        heapq.heapify(heap)
        return([heapq.heappop(heap)[1] for i in range(k)])
    
        
