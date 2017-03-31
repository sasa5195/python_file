import heapq
def merge(generators):
    r"Perform a k-way merge of the data contained in the generators."
    heap = []

    # The last known value for a given generator
    values = [None for g in generators]

    # Initialize the heap with the first value from each generator
    for i, g in enumerate(generators):
        heapq.heappush(heap, (g.next(), g, i))

    while heap:
        # Peek and get the current timestamp
        tm = heap[0][0][0]

        # Pull off all of the data for now, saving the values along the way
        while heap and heap[0][0][0] == tm:
            (tm, value), g, i = heapq.heappop(heap)
            values[i] = value

            # Get the next data point for this generator and enqueue it
            try:
                next_tm, next_value = g.next()
                heapq.heappush(heap, ((next_tm, next_value), g, i))
            except StopIteration:
                # This generator is finished
                pass

        yield tm, values
n=map(int,raw_input().split())
a=map(int,raw_input().split())
b=map(int,raw_input().split())
c=map(int,raw_input().split())
d=map(int,raw_input().split())
e=map(int,raw_input().split())
a.sort()
b.sort()
c.sort()
d.sort()
e.sort()

ct=0
res=[x for x in heapq.merge(a,b,c,d,e)]
for i in set(res):
  if res.count(i)>=3:
    ct=ct+1
print ct
