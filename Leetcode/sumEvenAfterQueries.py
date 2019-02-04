class Solution:
    def sumEvenAfterQueries(self, A: 'List[int]', queries: 'List[List[int]]') -> 'List[int]':
        res = []
        sumEven = sum(x for x in A if x%2==0)
        for i in range(len(queries)):
            index = queries[i][1]
            val = queries[i][0]
            #print(val, index)
            old = A[index]
            A[index] += val
            new = A[index]
            if old%2==0:
                sumEven -= old
            if new%2==0:
                sumEven += new
            res.append(sumEven)
        return res
