n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))
m=[]
for i in range(n-1):
    print m , i , a[i]
    if a[i] in a[i+1:]:
        m.append((a[i+1:].index(a[i])))
if len(m):
    print min(m)
else:
    print "-1"
