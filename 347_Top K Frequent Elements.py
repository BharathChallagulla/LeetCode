class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hash_map = {}
        for i in nums:
            hash_map[i] = 1 + hash_map.get(i, 0)
        final_arr = []

        hash_map_sorted = sorted(hash_map.items(), key=lambda x:x[1], reverse=True)
        print(hash_map_sorted)
        while k>0:
            final_arr.append(hash_map_sorted[k-1][0])
            k-=1
        return final_arr