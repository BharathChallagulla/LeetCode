class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        resArr = []
        
        for i in operations:
            if i == '+':
                resArr.append(resArr[-1] + resArr[-2])
            elif i == 'D':
                resArr.append(resArr[-1]*2)
            elif i == 'C':
                resArr.pop()
            else:
                resArr.append(int(i))
        return sum(resArr)