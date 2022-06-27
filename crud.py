from select import select
from db import *
email= "abc@gmail.com"
password= "1234"
name= "abc"

#sql="INSERT INTO person(email, password, name) VALUES (%s,%s,%s)"
# cursor.execute(sql,(email,password,name))
# conn.commit()
# conn.close()
def add_user(email,password,name):
    sql="INSERT INTO person(email, password, name) VALUES (%s,%s,%s)"
    cursor.execute(sql,(email,password,name))
    conn.commit()
    print("data inserted")
    
def getuser_fromdb(id):
    sql="select * from person where id=%s"
    cursor.execute(sql%id)
    record = cursor.fetchone()
    return record

