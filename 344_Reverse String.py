class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # initialize left, right
        l, r = 0, len(s)-1

        while l < r:
            # swap left and right
            s[l], s[r] = s[r], s[l]
            l, r = l+1, r-1