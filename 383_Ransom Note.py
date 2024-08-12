class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazine_letters = {}

        for i in magazine:
            if i not in magazine_letters:
                magazine_letters[i] = 1
            else:
                magazine_letters[i] += 1
        
        for i in ransomNote:
            if i not in magazine_letters or magazine_letters[i] <= 0:
                return False
            else:
                magazine_letters[i] -= 1
        return True