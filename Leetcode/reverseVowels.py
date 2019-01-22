class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        j = len(s)-1
        l = list(s)
        sets = ['a','e','i','o','u','A','E','I','O','U']
        while(i<j):
            if(l[i] not in sets):
                i+=1
            elif(l[j] not in sets):
                j-=1
            else:
            #elif(i in sets and j in sets):
                l[i], l[j] = l[j], l[i]
                i += 1
                j -= 1
        #print(l)
        return ''.join(l)
