def mystery(l):
   if l == []:
      return (l)
   else:
      return (l[-1:] + mystery(l[:-1]))

print mystery([3,2,7,8,5])


