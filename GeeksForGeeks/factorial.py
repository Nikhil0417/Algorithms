#code
loop = int(input())

for j in range(loop):
    n=int(input())
    if n>=0:
        fact = 1
        for i in range(1,n+1):
            fact = fact*i
    print(fact)
