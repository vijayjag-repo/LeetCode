"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        
        Approach:
        
        Maintain a dictionary for visited nodes.
        Make a copy of the given node.
        If the given node has neighbors, add them to the node_copy
        If some nodes are seen already, append it from dictionary.
        Else, call dfs and append.
        """
        d = dict()
        
        def dfs(node):
            if not node:
                return
            else:
                node_copy = Node(node.val,[])
                d[node] = node_copy
                for n in node.neighbors:
                    if n in d:
                        node_copy.neighbors.append(d[n])
                    else:
                        node_copy.neighbors.append(dfs(n))
                return node_copy
        
        return dfs(node)
