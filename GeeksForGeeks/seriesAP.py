#code
def seriesAP(a,b,n):
    d = b-a
    nTerm = a+(n-1)*d
    #print(nTerm)
    return nTerm
    
loop = int(input())
for i in range(0,loop):
    values = input()
    v = values.split(" ")
    a = int(v[0])
    b = int(v[1])
    n = int(input())
    
    result = seriesAP(a,b,n)
    print(result)
