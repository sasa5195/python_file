##with open("samplepdf.pdf", "rb") as imageFile:
##  f = imageFile.read()
##  b = bytearray(f)
##res=""
##for i in b:
##    res=res+chr(i)
##f=open("message.txt","w")
##f.write(res)
##f.close()
f=open("final_decr.txt","r")
res=f.read()
f.close()
k=[]
for i in res:
    k=k+[ord(i)]
x=bytearray(k)
fh = open("test.pdf", "wb")
fh.write(x)
fh.close()
