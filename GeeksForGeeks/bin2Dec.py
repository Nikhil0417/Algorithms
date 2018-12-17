#code
loop = int(input())

for i in range(loop):
    n = input()
    dec = 0
    for j in range(len(n)):
        dec += int(n[j])*(2**(len(n)-1-j))
        #print(dec)
    print(dec)
