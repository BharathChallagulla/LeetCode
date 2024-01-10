class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hash_map = {}
        for i in strs:
            sort_str = ''.join(sorted(i))
            if sort_str in hash_map:
                hash_map[sort_str].append(i)
            else:
                hash_map[sort_str] = [i]

        return hash_map.values()