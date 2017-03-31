d={}
row,col=map(int,raw_input().split())
r=range(1,col+1)
c=range(col,row*col+1,col)
right=[]
down=[]
level=[-1]*(row*col)
q=[]
for i in range(row):
    arr=map(int,raw_input().split())    
    right=right+[arr]
for i in range(row):
    arr=map(int,raw_input().split())
    down=down+[arr]
k=1
for i in range(row):
    for j in range(col):
        d[i+j+k]=d.get(i+j+k,[])+[x+i+j+k for x in r[:right[i][j]] if x+i+j+k<=c[i]]
        d[i+j+k]=d.get(i+j+k,[])+[x+i+j+k for x in c[:down[i][j]] if x+i+j+k<=(row*col)]
    k=k+col-1
level[0]=0
q.append(1)
while len(q):
    j=q[0]
    q=q[1:]
    for node in d[j]:
        if level[node-1]==-1:
            level[node-1]=1+level[j-1]
            q.append(node)
print level[(row*col)-1]
