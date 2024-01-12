class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, strs):
        # write your code here
        res = []
        i = 0
        while i<len(strs):
            j = i
            while strs[j] != '#':
                j += 1
            length = int(strs[i:j])
            res.append(strs[j+1 : j+length+1])
            i = j + length + 1
        return res

