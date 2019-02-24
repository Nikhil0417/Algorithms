class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        ppl = set()
        judges = []
        for i in range(len(trust)):
            a = trust[i][0]
            b = trust[i][1]
            ppl.add(a)
            judges.append(b)
        s = N*(N+1)/2
        judge = s-sum(ppl)
        #print(s)
        #print(ppl)
        #print(judges)
        #print(judge)
        #print(judges.count(judge))
        if((judge<=0) or (judge in ppl) or judges.count(judge) != (N-1)):
            return -1
        else:
            return int(judge)
