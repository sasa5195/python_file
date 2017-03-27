n,s,di=map(int,raw_input().split())
d={}
distances={}
for i in range(n):
    a,b,c=map(int,raw_input().split())
    if (a,c) in d.keys() or (c,a) in d.keys():
        if (a,c) in d.keys():
            d[(a,c)]=min(b,d[(a,c)])
            if a in distances.keys():
                distances[a].update({c:d[(a,c)]})
            else:
                distances[a]={c:d[(a,c)]}
            if c in distances.keys():
                distances[c].update({a:d[(a,c)]})
            else:
                distances[c]={a:d[(a,c)]}
        else:
            d[(c,a)]=min(b,d[(c,a)])
            if a in distances.keys():
                distances[a].update({c:d[(a,c)]})
            else:
                distances[a]={c:d[(a,c)]}
            if c in distances.keys():
                distances[c].update({a:d[(a,c)]})
            else:
                distances[c]={a:d[(a,c)]}
    else:
        d[(a,c)]=b
        if a in distances.keys():
            distances[a].update({c:d[(a,c)]})
        else:
            distances[a]={c:d[(a,c)]}
        if c in distances.keys():
            distances[c].update({a:d[(a,c)]})
        else:
            distances[c]={a:d[(a,c)]}
nodes=tuple(distances.keys())
unvisited = {node: None for node in nodes} #using None as +inf
visited = {}
current = s
currentDistance = 0
unvisited[current] = currentDistance

while True:
    for neighbour, distance in distances[current].items():
        if neighbour not in unvisited: continue
        newDistance = currentDistance + distance
        if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
            unvisited[neighbour] = newDistance
    visited[current] = currentDistance
    del unvisited[current]
    if not unvisited: break
    candidates = [node for node in unvisited.items() if node[1]]
    current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]

if di in visited.keys():
    print "YES"
    print visited[di]
else:
    print "NO"
