import pypyodbc
connection = pypyodbc.connect('Driver={SQL Server};'
                                'Server=VRSQLWDEV20\APOLLO_DEV1;'
                                'Database=ReverseODS;'
                                )
#print connection
#connection.close()
cursor = connection.cursor()
sp_name=""
SQLCommand = ("SELECT OBJECT_DEFINITION(OBJECT_ID("+sp_name+"))")
cursor.execute(SQLCommand)
results = cursor.fetchone()
while results:
    print results[0],results[1]
    results = cursor.fetchone()
connection.close()
