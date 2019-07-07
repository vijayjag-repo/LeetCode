class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = dict()
        for i in strs:
            key = ''.join(sorted(i))
            if key in d:
                d.get(key).append(i)
            else:
                d[key] = [i]
        return d.values()
--------------------------------------------------------------
# time = O(NK)
ans = collections.defaultdict(list)
for s in strs:
    count = [0]*26
    for c in s:
        count[ord(c)-ord('a')]+=1
    ans[tuple(count)].append(s)
return(ans.values())
        
        
