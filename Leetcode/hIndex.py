class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        arr = [0]*(n+1)
        #print(arr)
        for i in range(n):
            if(citations[i]>=n):
                arr[n] += 1
            else:
                arr[citations[i]] += 1
        print(arr)
        total = 0        
        for i in range(n,0,-1):
            #print(total)
            total += arr[i]
            if(total>=i):
                return i
        return 0
