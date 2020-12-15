import pgdb

def doQuery( conn ) :
    cur = conn.cursor()
    cur.execute(""" SELECT "Nom" FROM "Clients" """)
    
    for firstname, lastname in cur.fetchall() :
        print(firstname, lastname)

hostname='localhost'
username='ChaBoxxHF'
password='1702'
database='projet'

myConnection = pgdb.connect (host = hostname, user=username, password = password, database=database)
doQuery (myConnection)
myConnection.close()