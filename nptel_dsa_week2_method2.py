import bisect
d={}
n=map(int,raw_input().split())
for i in n:
    ipt=map(int,raw_input().split())
    for ele in ipt:
        d[ele]=d.get(ele,0)+1
val=d.values()
val.sort()
if 3 in val:
  print len(val)-val.index(3)
else:
  print len(val)-bisect.bisect(val,3)
