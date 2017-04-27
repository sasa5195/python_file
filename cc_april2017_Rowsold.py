for i in range(input()):
    x=raw_input()
    count1=0
    count0=0
    time=0
    l=len(x)
    for i in range(l):
        if x[i]=='1':
            count1+=1
        elif i+1<l:
            if x[i+1]=='0':
                count0+=1
            else:
                count0+=1
                time += (count0 + 1) * count1
                count0=0
        else:
            count0+=1
            time+=(count0+1)*count1
            count0=0
    print(time)