from collections import defaultdict
from heapq import *

def dijkstra(edges, f,t,n):
    g = defaultdict(list)
    for l,r,c in edges:
        g[l].append((c,r))
    result=[t]*n
    q, seen = [(0,f,())], set()
    result[f-1]=0
    while q:
        (cost,v1,path) = heappop(q)
        result[v1-1]=min(cost,result[v1-1])
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            for c, v2 in g.get(v1, ()):
                if v2 not in seen:
                    heappush(q, (cost+c, v2, path))
    return " ".join(map(str,result))
    #return float("inf")

for test in range(input()):
    n,k,x,m,s=map(int, raw_input().split())
    edges = []
    tot=x*k
    for i in range(1,k):
        for j in range(i+1,k+1):
            edges=edges+[(i,j,x)]
            edges=edges+[(j,i,x)]

    for mm  in range(m):
        i,j,w=map(int, raw_input().split())
        edges = edges + [(i, j, w)]
        edges = edges + [(j, i, w)]
        tot+=w
    res=[]
    print dijkstra(edges, s,tot+1,n)