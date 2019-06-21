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
                    
                    
                
        
