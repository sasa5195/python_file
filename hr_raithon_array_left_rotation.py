##a,b=map(int,raw_input().split())
##n=map(int,raw_input().split())
##print " ".join(map(str,n[b:]+n[:b]))


##t=int(raw_input())
##for i in range(t):
##    n,m,s=map(int,raw_input().split())
##    print s
##    x=list(xrange(1,n+1))
##    print x
##    x=x[(s-1):]+x[:(s-1)]
##    x=x*((m/n)+1)
##    print x[m-1]

##t=int(raw_input())
##for i in range(t):
##    n,m,s=map(int,raw_input().split())
##    v=m%n
##    if v==0:
##        print s-1
##    else:
##        if (n-s+1) >=v:
##            print s+v-1
##        else:
##            print v-(n-s+1)

def ix(a,n):
    s=sum(a)
    ls=0
    for j in range(n):
        s=s-a[j]
        if ls==s:
            return j
        ls=ls+a[j]
    return -1
        
t=int(raw_input())
for i in range(t):
    n=int(raw_input())
    a=map(int,raw_input().split())
    v=ix(a,n)
    if v==-1:
        print "NO"
    else:
        print "YES"
