class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        S = len(s)
        j = 0
        for i in t:
            if j<S and i == s[j]:
                j += 1
        return j==S