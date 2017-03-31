import rabinMiller
f=open("al_sweigart_privkey.txt","r")
val=f.read()
f.close()
res=val.split(",")
keysize=int(res[0])

f=open("random_file.txt","w")
rsize=8
split=(keysize-rsize)/8

n=rabinMiller.generateLargePrime(rsize)
x=bin(n)[2:]
res=(x*(split/rsize))+x[:(split%rsize)]
G=int(res,2)
f.write(str(rsize)+","+str(n)+","+str(G))
f.close()
