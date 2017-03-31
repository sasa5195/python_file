# Enter your code here. Read input from STDIN. Print output to STDOUT
t=int(raw_input())
while t:
    flg=1
    s=raw_input()
    b=raw_input()
    s.lower()
    b.lower()
    print s
    print b
    for i in b:
        if i in s:
            s=s[s.index(i)+1:]
        else:
            flg=0
            break
    if flg:
        print "YES"
    else:
        print "NO"
    t=t-1
