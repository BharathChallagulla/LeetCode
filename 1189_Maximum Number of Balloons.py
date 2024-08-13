class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        totalLetters = {}
        balloonLetters = {}

        for i in text:
            if i in "balloon":
                totalLetters[i] = totalLetters.get(i, 0) + 1
        
        for i in "balloon":
            balloonLetters[i] = balloonLetters.get(i, 0) + 1
        
        if any(c not in totalLetters for c in "balloon"):
            return 0
        else:
            return min(totalLetters["b"], totalLetters["a"], totalLetters["l"] // 2, totalLetters["o"] // 2, totalLetters["n"])