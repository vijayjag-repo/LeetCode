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
        while(l<r):
            if(height[l]<height[r]):
                if(height[l]>left_wall):
                    left_wall = height[l]
                else:
                    water+= left_wall - height[l]
                    l+=1
            else:
                if(height[r]>right_wall):
                    right_wall = height[r]
                else:
                    water+= right_wall - height[r]
                    r-=1
        return(water)
                    
                    
# O(N) Time and O(N) Space approach

# Here we just scan from left to right and the right to left.
# Then from the common region we just remove the height.
# Check LeetCode solution for images.

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = []
        right = []
        max_left = 0
        max_right = 0
        for i in range(0,len(height)):
            if(height[i]>max_left):
                max_left = height[i]
            
            left.append(max_left)
        
        for j in range(len(height)-1,-1,-1):
            if(height[j]>max_right):
                max_right = height[j]
            
            right.append(max_right)
        
        right = right[::-1]
        ans = 0
        
        for x in range(len(left)):
            ans+=min(left[x],right[x])-height[x]
        
        return(ans)
        
