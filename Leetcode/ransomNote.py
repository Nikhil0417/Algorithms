class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        t = True
        l = list(magazine)
        for i in ransomNote:
            if i not in l:
                t = False
                break
            else:
                l.remove(i)
                t = True
        return t
