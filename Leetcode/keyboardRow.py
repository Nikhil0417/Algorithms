class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        r1 = 'qwertyuiop'
        r2 = 'asdfghjkl'
        r3 = 'zxcvbnm'
        finalList = []
        for word in words:
            w = word.lower()
            tf1 = []
            tf2 = []
            tf3 = []
            for i in w:
                tf1.append(i in r1)
                tf2.append(i in r2)
                tf3.append(i in r3)
            #print(tf1)
            #print(tf2)
            #print(tf3)
            if all(tf1) or all(tf2) or all(tf3):
                finalList.append(word)
        return finalList
