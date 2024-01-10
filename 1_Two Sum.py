class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l,r = 0,1
        n = len(nums)
        for i in range(len(nums)-1):
            req = target-nums[i]
            if req in nums[i+1:]:
                req_index = nums.index(req, i+1)
                # print(req_index, nums[i+1:])
                return [i, req_index]

        