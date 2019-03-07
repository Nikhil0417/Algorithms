#code
t = int(input())

for i in range(t):
    a = list(int(i) for i in input().strip().split(" "))
    b = list(int(i) for i in input().strip().split(" "))
    x = a[0]
    y = a[1]
    n = a[2]
    count = 0
    for j in range(n):
        if b[j]<=x:
            count += 1
        else:
            while(b[j]>(y)):
                b[j] = b[j]-x+y
                count += 1
    print(count)
    #print("this is x",x)
    #print("this is y",y)
