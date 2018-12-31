class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # print((bin(x^y)).count('1'))
        a = bin(x)
        b = bin(y)
        #print(a,b)
        p = a[2:]
        q = b[2:]
        z = ""
        count = 0
        #print(a[2:],b[2:])
        if(len(a)<len(b)):
            for i in range(len(b)-len(a)):
                z += "0"
            bin1 = z+a[2:]
            #print(bin1)
            for i in range(len(bin1)):
                if(q[i]!=bin1[i]):
                    count += 1
        elif(len(a)>len(b)):
            for i in range(len(a)-len(b)):
                z += "0"
            bin2 = z+b[2:]
            #print(bin2)
            for i in range(len(bin2)):
                if(p[i]!=bin2[i]):
                    count += 1
        else:
            for i in range(len(q)):
                if(p[i]!=q[i]):
                    count += 1
        return count
