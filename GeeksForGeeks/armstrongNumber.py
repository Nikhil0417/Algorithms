#code
loop = int(input())

for i in range(0,loop):
    n = int(input())
    m = n
    sum = 0
    while(m>0):
        r = m%10
        #print(r)
        sum += int(r**3)
        m = int(m/10)
        #print(m)
    #print(sum)
    if sum==n:
        print("Yes")
    else:
        print("No")
