n,c = raw_input().strip().split(' ')
n,c = [int(n),int(c)]
crate = []
for crate_i in xrange(c):
    crate_temp = map(int,raw_input().strip().split(' '))
    crate=crate+[crate_temp[1]]*crate_temp[0]
crate.sort()
crate.reverse()
print sum(crate[:n])
