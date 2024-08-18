class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        hash_map = {')': '(', '}': '{', ']': '['}
        for i in s:
            if i in hash_map:
                if not stack:
                    return False
                else:
                    popEle = stack.pop()
                    if popEle != hash_map[i]:
                        return False
            else:
                stack.append(i)
        return not stack
