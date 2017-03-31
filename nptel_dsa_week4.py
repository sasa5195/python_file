n,s,d=map(int,raw_input().split())
d={}
gr={}
inf=0
for i in range(n):
    a,b,c=map(int,raw_input().split())
    if (a,c) in d.keys() or (c,a) in d.keys():
        if (a,c) in d.keys():
            d[(a,c)]=min(b,d[(a,c)])
            gr[a]=gr.get(a,[])+[[c,b]]
            gr[c]=gr.get(c,[])+[[a,b]]
            inf=inf+b
        else:
            d[(c,a)]=min(b,d[(c,a)])
            gr[a]=gr.get(a,[])+[[c,b]]
            gr[c]=gr.get(c,[])+[[a,b]]
            inf=inf+b
    else:
        d[(a,c)]=b
        gr[a]=gr.get(a,[])+[[c,b]]
        gr[c]=gr.get(c,[])+[[a,b]]
        inf=inf+b
dis={}
for i in d.keys():
    print i[0],d[i],i[1]
for i in gr.keys():
    print i, gr[i]
    dis[i]=inf
d[s]=0
q.append(s)
while len(q):
    j=q[0]
    q=q[1:]
    for node in gr[j]:
        if node[0]o


