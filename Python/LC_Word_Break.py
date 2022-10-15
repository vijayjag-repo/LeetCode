class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool

        Pochmann!!

        """
        ok = [True]
        for i in range(1,len(s)+1):
            if(any(ok[j] and s[j:i] in wordDict for j in range(i))):
                ok.append(True)
            else:
                ok.append(False)
        return ok[-1]

# BFS based solution; Pretty intuitive
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        word_set = set(wordDict)
        q = deque()
        visited = set()
        q.append(0)

        while q:
            start = q.popleft()
            if start in visited:
                continue

            for end in range(start+1, len(s) + 1):
                if s[start:end] in word_set:
                    q.append(end)
                    if end == len(s):
                        return True
            visited.add(start)

        return False

# DP based Solution
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        word_set = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[len(s)]
