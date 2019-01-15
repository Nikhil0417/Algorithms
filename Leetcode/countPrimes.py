import math
class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        primes = [True for i in range(n)]
        p = 2
        
        while(p*p<n):
            if(primes[p]==True):
                for i in range(p*p,n,p):
                    primes[i] = False
            p += 1
        #print(primes)
        return primes[2:].count(True)
