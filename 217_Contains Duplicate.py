class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_set = set(nums)
        if len(num_set)<len(nums):
            return True
        return False
