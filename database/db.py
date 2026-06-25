
import sqlite3




conn=sqlite3.connect(

"database/complaints.db"

)



cursor=conn.cursor()




cursor.execute(

'''

CREATE TABLE IF NOT EXISTS complaints(


id INTEGER PRIMARY KEY AUTOINCREMENT,



complaint TEXT,



category TEXT,



sentiment TEXT,



priority TEXT,



solution TEXT


)

'''


)




conn.commit()



conn.close()



print(

"Database Created"

)
