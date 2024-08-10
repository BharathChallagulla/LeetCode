class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ranges = []
        i = 0
        while i < len(nums):
            start = nums[i]
            end = start
            while i < len(nums)-1 and nums[i+1] == nums[i]+1:
                end = nums[i+1]
                i += 1
            
            if end == start:
                ranges.append("{0}".format(start))
            else:
                ranges.append("{0}->{1}".format(start, end))
            i += 1

        return ranges