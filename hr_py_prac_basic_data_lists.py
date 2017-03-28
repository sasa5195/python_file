if __name__ == '__main__':
    N = int(raw_input())
    arr=[]
    for i in range(N):
        a=raw_input()
        if "insert" in a:
            x,y,z=a.split(" ")
            print x,y,z
            arr.insert(int(y),int(z))
        elif "print" in a:
            print arr
        elif "remove":
            x,y=a.split(" ")
            print x,y
            arr.remove(int(y))
        elif "append":
            x,y=a.split(" ")
            print x,y
            arr.append(int(y))
        elif "sort":
            arr.sort()
        elif "pop":
            arr.pop()
        elif "reverse":
            arr.reverse()
        print arr,x,y
            
