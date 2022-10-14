# DP hard problem
# For better understanding, check this - https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/discuss/2156486/Greedy-Failed-From-Level-Zero-or-Beginner-Friendly-or-Fully-Explained-or-Python-or-C

from functools import lru_cache
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        @lru_cache(2000)
        def df(i, left):
            if i == m:
                return 0

            val = multipliers[i]
            # Easy to derive if you take an example
            right = n - 1 - (i - left)

            # Left, right products
            left_product = val * nums[left] + df(i + 1, left + 1)
            right_product = val * nums[right] + df(i + 1, left)

            return max(left_product, right_product)

        n = len(nums)
        m = len(multipliers)

        return df(0,0)
