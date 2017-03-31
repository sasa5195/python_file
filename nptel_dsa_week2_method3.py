a=map(int,raw_input().split())
res=[]
for i in range(len(a)):
  x=map(int,raw_input().split())
  x.sort()
  res=res+x
  res.sort()
c=0
for i in set(res):
  if res.count(i)>=3:
    c=c+1
print c