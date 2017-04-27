for i in range(input()):
   n,k=map(int,raw_input().split())
   a=[0]*k
   cnt=0
   flg=0
   for j in range(n):
       x=map(int,raw_input().split())
       if flg==0:
           for l in x[1:]:
               if a[l-1]==0:
                   a[l-1]=1
                   cnt+=1
           if cnt==k:
               flg=1
               v=j+1
   if flg:
       if v==n:
           print "all"
       else:
           print "some"
   else:
       print "sad"