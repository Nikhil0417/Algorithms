class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        i=0
        j=len(S)-1
        l = list(S)
        while i<j:
            if(l[i].isalpha() == False):
                i += 1
            elif(l[j].isalpha() == False):
                j -= 1
            else:
                l[i], l[j] = l[j], l[i]
                i += 1
                j -= 1
        return ''.join(l)
