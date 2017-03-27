import sys

class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        self.distance = sys.maxint       
        self.visited = False  
        self.previous = None

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous

def shortest(v, path):
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return

import heapq

def dijkstra(aGraph, start, target):
    dis={}
    start.set_distance(0)
    unvisited_queue = [(v.get_distance(),v) for v in aGraph]
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue):
        uv = heapq.heappop(unvisited_queue)
        current = uv[1]
        current.set_visited()
        for next in current.adjacent:
            if next.visited:
                continue
            new_dist = current.get_distance() + current.get_weight(next)
            
            if new_dist < next.get_distance():
                next.set_distance(new_dist)
                next.set_previous(current)
                dis[next.get_id()]=next.get_distance()
            else:
                dis[next.get_id()]=next.get_distance()
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        unvisited_queue = [(v.get_distance(),v) for v in aGraph if not v.visited]
        heapq.heapify(unvisited_queue)
    return dis



   
if __name__ == '__main__':
    n,s,di=map(int,raw_input().split())
    d={}
    gr={}
    for i in range(n):
        a,b,c=map(int,raw_input().split())
        if (a,c) in d.keys() or (c,a) in d.keys():
            if (a,c) in d.keys():
                d[(a,c)]=min(b,d[(a,c)])
                gr[a]=gr.get(a,[])+[[c,b]]
                gr[c]=gr.get(c,[])+[[a,b]]
            else:
                d[(c,a)]=min(b,d[(c,a)])
                gr[a]=gr.get(a,[])+[[c,b]]
                gr[c]=gr.get(c,[])+[[a,b]]
        else:
            d[(a,c)]=b
            gr[a]=gr.get(a,[])+[[c,b]]
            gr[c]=gr.get(c,[])+[[a,b]]

    g = Graph()
    for i in gr.keys():
        g.add_vertex(str(i))
    for i in d.keys():
        g.add_edge(str(i[0]), str(i[1]), d[i])

    shrt_dis=dijkstra(g, g.get_vertex(str(s)), g.get_vertex(str(di))) 

    target = g.get_vertex(str(di))
    if target==None:
        print "NO"
    else:
        print "YES"
        print shrt_dis[target.get_id()]
