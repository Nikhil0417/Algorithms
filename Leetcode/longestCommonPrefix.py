class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        #least = ""
        if len(strs)>=1:
            mi = len(strs[0])
            for i in strs:
                if len(i)<=mi:
                    mi = len(i)
                    least = i
            s = ""
        
            for i in range(mi):
                count = 0
                for j in range(len(strs)):
                    if strs[j][i]==least[i]:
                        count += 1
                if(count==len(strs)):
                    s += least[i]
                else:
                    break
            return s
        else:
            return ""
                    
