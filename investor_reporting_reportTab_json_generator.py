f=open("../investor_reporting_columns_input.txt","r")
a=f.readlines()
f.close()
# print len(a)

f=open("../investor_reporting_column_description_input.txt","r")
b=f.readlines()
f.close()
# print b
# print len(b)
for i in b:
    print i
k=0
for j in range(0,len(b),2):
    x=b[j].split("*")
    print x
    b[k]=x[1]
    k+=1
# print k
# print b
res1='''{
         "columnName": '''
res2=''',
         "columnDescription": '''
res3=''',
         "columnType": "HARDCODED",
         "sqlColumnName": "",
         "mapperClassName": "",
         "calculationMapper": "",
         "hardCodedValue": "123123123"
       },'''
res=''
for i in range(len(a)):
    res+=res1+'\"'+a[i].strip()+'\"'+res2+'\"'+b[i].strip()+'\"'+res3+"\n"
f=open("investor_reporting_columns_json_output.txt","w")
f.write(res)
f.close()
print res