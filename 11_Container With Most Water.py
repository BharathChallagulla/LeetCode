class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        maxWater = 0
        
        # initialize left and right pointer
        l, r = 0, len(height)-1

        while l < r:
            # max water is max area 
            maxWater = max(maxWater, (r-l)*min(height[l], height[r]))

            # if height[lrft] is lesser than right increase left pointer else decrease right
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxWater