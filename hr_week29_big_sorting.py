n=int(raw_input())
d={}
while n:
    x=raw_input()
    d[len(x)]=d.get(len(x),[])+[x]
    n=n-1
res=[]
for i in sorted(d.keys()):
    f=sorted(d[i])
    res=res+f
for i in res:
    print i
