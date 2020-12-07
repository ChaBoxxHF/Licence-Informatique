import pgdb

hostname='localhost'
username='USERNAME'
password='PASSWORD'
database='DBNAME'

myConnection = pgbd.connect (host = hostname, user=username, password = password, database=database)
doQuery (myConnection)
myConnection.close()