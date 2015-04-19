for a in range(1,10):
    s=""
    for b in range(a,10):
        s+=str.format("{0:1}*{1:1}={2:<4}",a,b,i*j)
    print(s)
    for n in range(1,1+a):
        print(end='        ')
