class Solution(object):
    def maximumStrongPairXor(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxXor = 0
        numsLen = len(nums)
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if(abs(nums[i]-nums[j]) <= min(nums[i], nums[j])):
                    maxXor = max(maxXor, nums[i]^nums[j])
        return maxXor
        