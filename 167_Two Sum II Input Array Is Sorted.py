class Solution(object):
    def twoSum(self, nums, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(nums)-1
        # simple
        # while i<j:
        #     if nums[i] + nums[j] < target:
        #         i += 1
        #     elif nums[i] + nums[j] > target:
        #         j-=1
        #     else:
        #         return [i+1, j+1]

        while l < r:
            m = l + (r-l)//2
            if ( nums[l] + nums[r] > target ) : 
                if ( nums[m ] + nums[l] > target ):
                    r = m -1
                else : r -= 1
            elif (nums[l] + nums[r]  < target ) : 
                if (nums[m] + nums[r] <  target):
                    l= m + 1
                else : l  += 1 
            else : return [l + 1, r + 1]

