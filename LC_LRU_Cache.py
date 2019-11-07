class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self,capacity):
        self.capacity = capacity
        self.d = dict()
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove(self,node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
    
    def _add(self,node):
        prev = self.tail.prev
        prev.next = node
        self.tail.prev = node
        node.prev = prev
        node.next = self.tail
        
    def get(self,key):
        if key in self.d:
            node = self.d[key]
            self._remove(node)
            self._add(node)
            return(node.value)
        return(-1)
    
    def put(self,key,value):
        node = Node(key,value)
        if key in self.d:
            self._remove(self.d[key])
        
        self._add(node)
        self.d[key] = node
        if(len(self.d)>self.capacity):
            node = self.head.next
            self._remove(node)
            del self.d[node.key]
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

import collections
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.d = collections.OrderedDict()
        self.capacity = capacity
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.d:
            return -1
        else:
            val = self.d.pop(key)
            self.d[key] = val
            return self.d[key]
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.d:
            self.d.pop(key)
        
        if(len(self.d)>=self.capacity):
            self.d.popitem(last=False)
        self.d[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
