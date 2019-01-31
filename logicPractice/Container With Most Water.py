class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Brute Force
        # maxArea = 0
        # for i in range(0, len (height)):
        #     for j in range(i+1,len(height)):
        #         maxArea = max(maxArea, (j-i) * min(height[i], height[j]))
        # return maxArea
    
        # Two Pointer Approach
        
        maxArea = 0 
        length = 0
        width = len(height) - 1
        while length < width:
            maxArea = max((width-length) * min(height[length], height[width]), maxArea)
            if height[length] < height[width]:
                length = length + 1 
            else:
                width = width - 1
        return maxArea
            