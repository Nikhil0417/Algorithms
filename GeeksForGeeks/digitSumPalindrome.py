#code
loop = int(input())

for i in range(loop):
    n = int(input())
    sum = 0
    while(n>0):
        r = int(n%10)
        sum += r
        n = n/10
    if str(sum)==str(sum)[::-1]:
        print("YES")
    else:
        print("NO")
