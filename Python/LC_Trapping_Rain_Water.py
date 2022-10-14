
# Optimal approach using two pointers
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        left_wall = 0
        right_wall = 0
        water = 0

        while (l<r):
            if (height[l] < height[r]):
                if (height[l]>left_wall):
                    left_wall = height[l]
                else:
                    water+= left_wall - height[l]
                    l +=1
            else:
                if (height[r]>right_wall):
                    right_wall = height[r]
                else:
                    water += right_wall - height[r]
                    r -=1

        return water



# Naive approach
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_wall = [0] * len(height)
        right_wall = [0] * len(height)
        left_max = 0
        right_max = 0

        for i in range(len(height)):
            left_max = max(left_max, height[i])
            left_wall[i] = left_max

        for i in range(len(height)-1, -1, -1):
            right_max = max(right_max, height[i])
            right_wall[i] = right_max

        ans = 0
        for i in range(len(height)):
            ans += min(left_wall[i], right_wall[i]) - height[i]

        return ans
