t=int(raw_input())
for i in range(t):
    n=int(raw_input())
    a=map(int,raw_input().split())
    a.sort()
    if a[1]-a[0]!=1:
        print a[0]
    else:
        print a[-1]
