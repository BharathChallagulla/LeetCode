class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        squares = []
        # initialize left and right pointer
        l, r = 0, len(nums)-1
        
        while l <= r:
            # if absolute of left > rigth appenf left value
            if abs(nums[l]) > abs(nums[r]):
                squares.append(nums[l]**2)
                l += 1
            else:
                squares.append(nums[r]**2)
                r -= 1
        # resultant array will be in descneding order
        return squares[::-1]
        